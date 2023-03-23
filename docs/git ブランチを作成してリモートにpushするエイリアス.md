[[git エイリアスで引数を使う]]を利用してブランチ作成とpushを同時に行う

```~/.gitconfig
[alias]
cobp = "!f(){ git checkout -b $1 && git push -u origin $1;};f"` 
```

