[VueでChrome extensionを開発する](https://zenn.dev/iwatos/scraps/4e150827d8fac4)

---
# Chrome拡張の機能
公式ドキュメント： [Extensions - Chrome Developers](https://developer.chrome.com/docs/extensions/)
サンプル集： [GitHub - GoogleChrome/chrome-extensions-samples: Chrome Extensions Samples](https://github.com/GoogleChrome/chrome-extensions-samples)
## Manifest V2 と V3について
Chrome extensionで現在利用できる仕様は`Manifest V2`と`Manifest V3`がある
`Manifest V2`は近々廃止される予定なので新規でextensionを作る場合は`Manifest V3`
を利用する
chrome extensionについて調べるとmanifestv2の情報が混在してるので注意

## 機能
大きく分けて
- ポップアップ画面
- オプション画面
- Service worker（ブラウザ画面などを対象とした処理に対する処理）
がある

# CRX JSを利用してプロジェクトを作成する
## 環境構築
[Create a project | CRXJS Vite Plugin](https://crxjs.dev/vite-plugin/getting-started/vue/create-project)

```
npm init vite@latest
Need to install the following packages:
  create-vite@4.2.0
Ok to proceed? (y) y
✔ Project name: … vite-project
✔ Select a framework: › Vue
✔ Select a variant: › TypeScriptcd
```

```
cd vite-project
npm i @crxjs/vite-plugin@beta -D
```

vite.configをの内容を以下に変更
`Cannot find module './manifest.json'. Consider using '--resolveJsonModule' to import module with '.json' extension.ts(2732)`
のエラーが出るが解決法がわからない。一旦無視でも動く
```vite.config
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { crx } from '@crxjs/vite-plugin'
import manifest from './manifest.json' assert { type: 'json' }

export default defineConfig({
  plugins: [
    vue(),
    crx({ manifest }),
  ],
})
```


manifest.jsonを作成する
```json
{
    "manifest_version": 3,
    "name": "CRXJS Vue Vite Example",
    "version": "1.0.0",
    "action": { "default_popup": "index.html" }
}
```


`npm run dev`を実行してローカルで以下の画面が出る
![[Pasted image 20230318200855.png]]



chromeで`chrome://extensions/`を開く
Finderから `vite-project/dist`フォルダを画面にドラッグドロップするとchrome拡張が追加される
![[Pasted image 20230318201111.png]]

拡張機能欄からクリックすると、ポップアップで先ほどの画面が開く
![[Pasted image 20230318201323.png]]

## ポップアップ
distフォルダ内にポップアップ用のhtml`src/pages/popup/index.html`を作成するため以下の設定をする

manifest.jsonの action でポップアップページで参照するhtmlを指定
```json
{
    "action": { 
        "default_popup": "src/pages/popup/index.html"
    }
}
```

`npm install @types/node -D`を実行後
vite.configの内容を以下に変更
```config
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { crx } from '@crxjs/vite-plugin'
import { resolve } from 'path'
import manifest from './manifest.json' assert { type: 'json' } // Node >=17


export default defineConfig({
  plugins: [
    vue(),
    crx({ manifest }),
  ],
  build: {
    rollupOptions: {
      input: {
        popup: resolve(__dirname, 'src/pages/popup/index.html'),
      },
    },
  }
})
```


src/pages/popupフォルダを作り以下を追加する。
App.vue
```vue:App.vue
<script setup lang="ts">
import HelloWorld from '../../components/HelloWorld.vue';
</script>

<template>
    <HelloWorld msg="popup page" />
</template>
```

index.html
```html:index.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>chrome extension template</title>
</head>

<body>
    <div id="app"></div>
    <script type="module" src="./main.ts"></script>
</body>

</html>
```

main.ts
```ts:main.ts
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

これでビルド時にdist/src/pages/popup/index.htmlが作成される

npm run devを再実行後、リロードしてポップアップ内に以下の画面が出ればOK
![[Pasted image 20230321211433.png]]


## オプションページ
ポップアップと同様の手順で作成する

vite.configに静的html作成の設定を追加
```config
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { crx } from '@crxjs/vite-plugin'
import { resolve } from 'path'
import manifest from './manifest.json' assert { type: 'json' }

export default defineConfig({
  plugins: [
    vue(),
    crx({ manifest }),
  ],
  build: {
    rollupOptions: {
      input: {
        popup: resolve(__dirname, 'src/pages/popup/index.html'),
        option: resolve(__dirname, 'src/pages/option/index.html'),
      },
    },
  }
})
```

src/pages/option配下にApp.vue,index.html,main.tsを作成する。
App.vue
```vue:App.vue
<script setup lang="ts">
import HelloWorld from '../../components/HelloWorld.vue';
</script>

<template>
    <HelloWorld msg="option page" />
</template>
```

index.html
```html:index.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>chrome extension template</title>
</head>

<body>
    <div id="app"></div>
    <script type="module" src="./main.ts"></script>
</body>

</html>
```

main.ts
```ts:main.ts
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```


manifest.jsonにoptions_page項目を追加
```json
{
    "manifest_version": 3,
    "name": "CRXJS Vue Vite Example",
    "version": "1.0.0",
    "action": { "default_popup": "src/pages/popup/index.html" },
    "options_page": "src/pages/option/index.html"
}
```

npm run devを再実行し、リロード後右クリックからオプションを選択して画面が開けばOK
![[Pasted image 20230321211716.png]]
![[Pasted image 20230322205851.png]]

## Service Worker
## 完成時
npm run buildでdistファイルを作成し、chromeにドラッグドロップ

---
## Link

- https://www.memory-lovers.blog/entry/2022/11/22/163000
- [Create a project | CRXJS Vite Plugin](https://crxjs.dev/vite-plugin/getting-started/vue/create-project)
- [Building for Production | Vite](https://vitejs.dev/guide/build.html#multi-page-app)
- [vite-plugin-mpa/main.ts at main · IndexXuan/vite-plugin-mpa · GitHub](https://github.com/IndexXuan/vite-plugin-mpa/blob/main/examples/vue3-mpa-app/src/pages/subpage/main.ts)
- [Chrome拡張機能を作ってみる | 2. 登場人物編 - くらげになりたい。](https://www.memory-lovers.blog/entry/2022/11/23/170000)
- [【Vue3+TypeScript+Vuetify+Vite】動的なテーマの切り替え - Qiita](https://qiita.com/kyonc5/items/bd7b9d887c81f1b6a598)