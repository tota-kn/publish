# git commit --amendで直前のコミットを変更する
`--amend` オプションを利用すると直前のコミットを修正（上書き）できる
コミットIDは変更される。

```sh
git commit --amend -m "直前のコミットを修正する"
```

すでにpush済みのコミットを修正して`git push`するとエラーが発生する。
その場合は`git push --force-with-lease`（[[git push --forceではなく--force-with-leaseを利用する]]）を利用する。