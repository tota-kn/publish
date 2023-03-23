# はじめに
ローンチしたサービス：[縦ったー](https://tatetter.netlify.com)
ソースコード：[GitHub](https://github.com/iwatos/tatetter)

ログイン不要で縦書きツイートができるサービスを作成しました！いえーい！
![スクリーンショット 2019-03-28 22.55.01.png](https://qiita-image-store.s3.amazonaws.com/0/230281/7e7abd28-dd8b-7cbe-1a67-0d52d2af3cca.png)

...と思ったらn番煎じでした。
そのままにしておくのも悔しいのでどうやって作成したかを書いていきます。

### 縦書きツイートサービスの先人たち
* [ツイッター縦書きヘルパー](https://tategaki.yanoshin.jp)
* [縦つい。](https://yubais.net/tools/tatetwi/)
* [縦書きったー](https://tategakitter.netlify.com)

### 先人に比べた本サービスの強み
* 入力文字が即座に縦書きに変換されて表示される。
* 半角文字を入れても形が崩れない

# 開発環境
Vue.js + Netlify
サーバレスです。DBもAPIも使わないからね。

# 利用の流れと仕組み
1. テキストボックスにツイートしたい内容を入力
2. 1の文章を縦書きに変換
3. 2の結果をもう一つのテキストボックスに出力
4. つぶやくボタンを押下
5. 3の結果が記入されたtwitterのツイートするページが開く
6. 内容を確認後ツイート。

# 解説
## 縦書きの変換
以下の流れで変換しました
1. 半角文字を全角文字に変換
2. 入力テキストを一文字ごとの二次元配列に変換
3. 二次元配列を右90度回転
4. 3結果の二次元配列を改行を足しながらつなげて文字列に戻す。

コードは要点のみ記載するので詳しい部分はgithubの
src/components/Content.vue を参照ください。

### 半角文字を全角文字に変換
半角文字と全角文字が混ざると縦書きにした時に形が崩れるので、
半角文字を全て全角文字に変換します。

```js
       let fullText = halfText.replace(/[!-~]/g, function(s) {return String.fromCharCode(s.charCodeAt(0) + 65248)})
       fullText = fullText.replace(/ /g,"　")
```

半角文字（英数字記号）は正規表現で/[!-~]/g(文字コードが!から~までの文字を指定)で表現できます。
半角文字の文字コード値に65248を足すと対応した全角文字になるので、それらに置換します。
また、半角スペースは上記では全角スペースにならないので、半角スペースを全角スペースに置換する処理も記述します。

### 文字列を一文字ごとの二次元配列に変換
文字列の高さ×幅の長方形の二次元配列に文字列を一文字ずつ入れていきます。
改行があった場合は配列の次の行に格納します。

```js
       //一字ずつ二次元配列に格納  
       str.split("\n").forEach(function(e, i){
         e.split("").forEach(function(f, j){
           matrix[i][j] = e[j]
```

### 二次元配列を右90度回転
先ほど作成した二次元配列を右90度分回転させます。
これで縦書きの配置になります。

```js
for (let i = 0; i < height; i++) {
            for (let j = 0; j < width; j++) {                
                rotatedMatrix[j][i] = matrix[height-i-1][j];
            }
        }
```

### 二次元配列を結合して文字列にする
各行ごとに文字を結合し、
行と行は、間に改行を入れて繋げます。

```js
 matrix.forEach(function (e,i,v) {
        v[i] = e.join("")
      })
      let str = matrix.join("\n")
```

以上で縦書きに変換されました。

## つぶやくボタンの設置
単純に呟けるページを開くだけなら

```html
<a href="https://twitter.com/share">Tweet</a>
```
でも可

今回はツイートページを開く時に末尾に`【縦書き本文】(縦ったーURL) #縦ったー` と表示させたかったので以下のように記述

```html
<a href="https://twitter.com/share" 
data-url="https://tatetter.netlify.com" 
data-text="【縦書き本文】"
data-hashtags="縦ったー"
>つぶやく</a> 
```
【縦書き本文】については改行をURLエンコードに変換させる必要があるため以下を記述

```js

let text = this.verticalText.replace(/\n/g, "%0A")
```
## 補足
twitterは文字列の先頭が空白でつぶやくと、空白がトリミングされるので
先頭文字が空白の場合"."に変換するようにします。

```js
let s = str.slice(0, 1)
      if(s == "　"){
        return "．" + str.slice(1) 
      }
      return str
```

# 公開
1. GitHubにコミット
2. Netlifyで公開！

とても簡単
Netlifyの使い方は以下
[基礎から学ぶVue.js：Vue.js + Netlifyで自動デプロイ](https://cr-vue.mio3io.com/tutorials/netlify.html#ビルド設定)

# 感想
DBがいらないものならVue.js + Netlifyでかなり簡単にこんなページが作れて楽しい！
ただアイデアはなかなか出なかったり、今回みたいに先人がいたりするので厳しい。

# 参考
[JavaScriptで英数を全角/半角に変換する方法](https://qiita.com/yamikoo@github/items/5dbcc77b267a549bdbae)
[Twitterシェアボタンの設置](https://qiita.com/dora_____emon/items/4230d28086c5913622bd)
