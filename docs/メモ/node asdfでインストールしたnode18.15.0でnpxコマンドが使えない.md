# node asdfでインストールしたnode18.15.0でnpxコマンドが使えない
## 環境
MacOS（intel）

## 事象
asdfでインストールしたnode18.15.0でnpxコマンドを実行すると`.npm`が存在しないと怒られる
```sh
❯ npx depcheck
npm ERR! code ENOENT
npm ERR! syscall lstat
npm ERR! path /Users/USER_NAME/.asdf/installs/nodejs/18.15.0/.npm
npm ERR! errno -2
npm ERR! enoent ENOENT: no such file or directory, lstat '/Users/USER_NAME/.asdf/installs/nodejs/18.15.0/.npm'
npm ERR! enoent This is related to npm not being able to find a file.
npm ERR! enoent

npm ERR! A complete log of this run can be found in:
npm ERR!     /Users/USER_NAME/.npm/_logs/2023-04-21T09_06_20_636Z-debug-0.log
```
## 対応
一度グローバルで何かしらをインストールする
`npm install -g depcheck`  
すると.npmが作成されてnpxコマンドが動くようになった