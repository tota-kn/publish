# flutter 静的解析でfreezedの生成ファイルを外す
`analysis_options.yaml`
```yaml
analyzer:  
  exclude:  
    - "lib/datasource/model/**.g.dart"  
	- "lib/datasource/model/**.freezed.dart"
```

---
### Related Notes
- 

### References
- 

### Tags
- `#flutter` 