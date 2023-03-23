```json:package.json
{
  "engines": {
    "node": "16.x"
  }
}
```

npmの場合は以下の設定をした.npmrcも配置すると、npmが指定したバージョンで無いときはエラーになる
```.npmrc:.npmrc
engine-strict=true
```

----
## Related Notes
- 

## References
- [package.jsonに"engines"を設定すると「このバージョンのNode.jsでしか動かない」を表明できる - Qiita](https://qiita.com/suin/items/994458418c737cc9c3e8)

## Tags
- 