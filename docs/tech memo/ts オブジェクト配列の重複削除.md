# ts オブジェクト配列の重複削除
lodash使えるならuniqby
[Lodash Documentation](https://lodash.com/docs/4.17.15`#uniqBy)`

全プロパティがdeep equalsな場合だと、uniqWith
第2引数はisEqual
[Lodash Documentation](https://lodash.com/docs/4.17.15`#uniqWith)`

lodash使えない場合は以下
```ts
export function uniqBy<T>(values: T[], fn: (x: T) => string | number): T[] {
  const m = new Map<string | number, T>();
  values.forEach((x) => {
    const k = fn(x);
    if (!m.has(k)) {
      m.set(k, x);
    }
  });
  return Array.from(m.values());
}
```

----
### Related Notes
- 

### References
- 

### Tags
- 