# js Null合体演算子と論理OR演算子との違い
Null合体演算子`??`は左辺値の結果が `null`または`undefined`の場合に右辺値を返却する。
論理OR演算子`||`は左辺値の結果がfalsy([[js falsyな値]])なときに右辺値を返却する。


```js
//Null合体演算子
console.log(null ?? "Default Value"); // "Default Value"
console.log(undefined ?? "Default Value"); // "Default Value"
console.log(0 ?? "Default Value"); // "0" 
console.log('' ?? "Default Value"); // "" 
console.log(false ?? "Default Value"); // "false" 

// 論理OR演算子
console.log(null || "Default Value"); // "Default Value"
console.log(undefined || "Default Value"); // "Default Value"
console.log(0 || "Default Value"); // "Default Value"
console.log('' || "Default Value"); // "Default Value"
console.log(false || "Default Value"); // "Default Value"
```


## 参考
[論理和 (||) - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/Logical_OR)
[Null 合体演算子 (??) - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)