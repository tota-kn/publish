# android インストールアプリのパッケージ名を確認する
端末をPCと繋いだ状態で以下のコマンドを実行する
```sh
## 一覧
adb shell pm list package

## 検索するとき
adb shell pm list package | grep <id>
```
