```ad-note
Macの場合は動作が異なるのでgsedを利用する
[[cli macOSでGNU版sedを利用する]]
```

```sh
sed "s/aaaa/AAA/g" -i input.txt
```

Mac版sedの場合は`-i`オプションの後ろに空文字`""`を指定する

```sh
sed -i "" "s/line/after/" in.txt
```