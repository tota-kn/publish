# js falsyな値
## false
```js
var bNoParam = Boolean();
var bZero = Boolean(0);
var bNull = Boolean(null);
var bEmptyString = Boolean('');
var bFalse = Boolean(false);
var bUndefined = Boolean(undefined);
```
## true
```js
var btrue = Boolean(true);
var btrueString = Boolean('true');
var bfalseString = Boolean('false');
var bSuLin = Boolean('Su Lin');
var bArrayProto = Boolean([]);
var bObjProto = Boolean({});
```

## 参考
- [Falsy (偽値) - MDN Web Docs 用語集: ウェブ関連用語の定義 | MDN](https://developer.mozilla.org/ja/docs/Glossary/Falsy)
- [Boolean - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
