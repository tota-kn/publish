[[git エイリアスを作成する]]で引数を使う
```.gitconfig
[alias]
hoge = "!f(){ echo $1;};f"` 

# $ git hoge hello
# > hello
```

# 参考
- [Gitのエイリアスで引数を使う](https://rcmdnk.com/blog/2013/12/20/computer-git/)
- [gitのaliasコマンドに引数を渡す方法 - Qiita](https://qiita.com/yatemmma/items/22aa62e232776f4f330b)