# ts リスト内に重複する要素があるかを判定
``` ts
export const hasDuplicatedElements = (_list: string[]) => {  
  const _set = new Set(_list)  
  return _list.length !== _set.size  
}
```

----
### Related Notes
- 

### References
- 

### Tags
- 