# cli watchを利用して特定コマンドを定期実行する
## インストール
```sh
brew install watch
```

## 利用
`-n`オプションを付けない場合は2秒毎に実行 
```sh
watch -n <実行間隔(秒)> "echo HelloWorld!"
```


## 参考
[curlコマンドを1秒ごとに実行する - Qiita](https://qiita.com/Cesaroshun/items/232bed49ba682afcf76f)
[定期実行するwatchコマンドの使い方まとめ - Qiita](https://qiita.com/shtnkgm/items/2aa204f2b52f24d02ff3)