# cli sed 文字列置換
```ad-note
Macの場合は動作が異なるのでgsedを利用する
[[cli macOSでGNU版sedを利用する]]
```

```sh
// 最初に出てくるものを置換
sed -e 's/<置換前>/<置換後>/' <file_path>

// 当てはまるものすべてを置換
sed -e 's/<置換前>/<置換後>/g' <file_path>
```

## References
https://bi.biopapyrus.jp/os/linux/sed.html

---
## Related Notes
- 

## References
- 

## Tags
- `#cli` 