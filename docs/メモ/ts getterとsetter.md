# ts getterとsetter
```ts
class Me {
  private hoge: number = 0;

  //getter
  get hoge(): number {
    return this.hoge;
  }

  //setter
  set hoge(value: number) {
    this.hoge = value;
  }
}

```

----
### Related Notes
- [typescriptにおけるgetterとsetterを理解する - Qiita](https://qiita.com/kuropp/items/ebefeec110ea6a2beb62)

### References
- 

### Tags
- 