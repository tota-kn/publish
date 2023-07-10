# git status, git diffで日本語を表示する
git statusコマンドで日本語を表示する場合、`\302\265`のような表示になってしまう。

以下の設定をすることで日本語のまま表示できる。
```sh
git config --global core.quotepath false
```

`core.quotepath`はパス名に含まれる特殊文字（バイト数が大きい文字）をエスケープするかの設定。

## 参考
[Git - git-config Documentation](https://git-scm.com/docs/git-config`#Documentation/git-config.txt-corequotePath)`
[git diff や git status での日本語の文字化けを防ぐ (core.page, core.quotepath) - まくまくGitノート](https://maku77.github.io/git/settings/garbling.html)