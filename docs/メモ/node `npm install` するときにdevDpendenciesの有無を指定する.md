# node `npm install` するときにdevDpendenciesの有無を指定する
```sh
## devDependencies無しの指定
npm install --omit=dev

## devDependencies有りの指定（NODE_ENV=producitonの場合に利用）
npm install --include=dev 
```

## 参考
[npm-install | npm Docs](https://docs.npmjs.com/cli/v8/commands/npm-install`#omit)`