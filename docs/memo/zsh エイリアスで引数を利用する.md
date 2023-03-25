# zsh エイリアスで引数を利用する
```sh:zshrc
alias hoge='(){echo $1 $2!!}'
## $ hoge hello world
## > hello world
```

## 参考
- [zsh環境で引数を持ったコマンドを作る - Qiita](https://qiita.com/sayama0402/items/46241c07c30e431fe38f)