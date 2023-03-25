# cli 変数が定義されているか確認
```sh
[ -v HOGE] && echo "変数がsetされている"
[ -z HOGE] && echo "変数が長さが0である"
[ -n HOGE] && echo "変数の長さが0でない"
```

----
### Related Notes
- 

### References
- [<Bash, zsh> シェル変数が定義されているかを判定する方法 - ねこゆきのメモ](https://nekoyukimmm.hatenablog.com/entry/2018/01/21/101828)
- [シェルスクリプトで変数が未定義かを確認する](https://blog.n-t.jp/post/tech/bash-non-zero-variable/)

### Tags
- 