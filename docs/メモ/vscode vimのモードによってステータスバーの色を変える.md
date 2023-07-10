# vscode vimのモードによってステータスバーの色を変える
[[vscode vimを利用する]]の設定を入れている前提

`settings.json`に以下の設定を入れる
```json
"vim.statusBarColorControl": true
````

上記設定だけで色が変わる用になるが、色を指定したい場合は更に以下設定を入れる  
```json
"vim.statusBarColors.normal": [
    "`#161821",` // 背景色
    "`#818596"` // 文字色
]
```


## 参考
[VimmerのVimmerによるVimmerのためのVSCode環境構築(Part2) – Freaky Engineer Notes](https://fe-notes.work/posts/20200712_vsvim02/)
[https://qiita.com/karlley/items/8c6e1c2637be283e6b4d](https://qiita.com/karlley/items/8c6e1c2637be283e6b4d)
