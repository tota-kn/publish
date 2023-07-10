# git 複数コミットのrevert
## 複数コミットのrevert
```sh
## --no-commitをつけないと各コミットごとにrevertコミットされる
git revert --no-commit <戻したい一番古いコミットID>..HEAD
```

---