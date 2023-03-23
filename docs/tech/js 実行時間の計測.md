# js 実行時間の計測
[console.time() - Web API | MDN](https://developer.mozilla.org/ja/docs/Web/API/console/time)
```js
console.time("hoge time")
hoge();
console.timeEnd("hoge time") // "INFO hoge time: XXms"がコンソール上に出力
```
