# git 現在のブランチ名を自動で取得してremote pushする
[[git]現在のブランチをプッシュするエイリアス](https://rb-station.com/blogs/software/git-branch-push) より引用

```.gitconfig
[alias]
po = "!git push --set-upstream origin \"$(git rev-parse --abbrev-ref HEAD)\""
```