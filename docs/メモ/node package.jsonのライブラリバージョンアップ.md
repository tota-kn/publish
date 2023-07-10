# node package.jsonのライブラリバージョンアップ
## ひとつずつ
```
npm install {PACKAGE} {VERSION}
```

## 一度にすべて上げたい場合
```
npx -p npm-check-updates -c "ncu" // 最新バージョンの確認
npx -p npm-check-updates -c "ncu -u" // package.jsonの記載更新
npm install // インストール
```


## 参考
[GitHub - raineorshine/npm-check-updates: Find newer versions of package dependencies than what your package.json allows](https://github.com/raineorshine/npm-check-updates)
[package.json に記載されているパッケージのバージョンアップ方法 【 npm-check-updates, outdated 】 - Qiita](https://qiita.com/sugurutakahashi12345/items/df736ddaf65c244e1b4f)