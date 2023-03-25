# cli sed 文字列を連続で置換
```ad-note
Macの場合は動作が異なるのでgsedを利用する
[[cli macOSでGNU版sedを利用する]]
```

```sh
sed -e "s/aaa/AAA/g" -e "s/bbb/BBB/g" input.txt > output.txt
```
