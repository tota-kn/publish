# html div要素全体にリンクをつける方法
div要素全体にリンクをつけたい時の方法メモ
自分用に簡潔にまとめる。

```html
<!-- divにclass要素を付与する-->
<div class="linkbox">
  <p>sample 文章なり画像なり</p>
  <a href="https://www.google.co.jp"></a>
  <p>sample 文章なり画像なり</p>
</div>
```

```
/*div要素全体にリンクをつけるために必要な要素*/
.linkbox {
    position: relative;
}
.linkbox a {
    position: absolute;
    top: 0;
    left: 0;
    height:100%;
    width: 100%;
}

/* 以下見た目をわかりやすくするための設定*/
.linkbox {
    border: solid 2px `#000000;`
}
.linkbox a:hover{/* マウスオーバー時に色変更*/
    opacity: 0.1;
    background-color: `#000000;`
}
```

<p class="codepen" data-height="279" data-theme-id="0" data-default-tab="html,result" data-user="iwato" data-slug-hash="moJwZV" style="height: 279px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid black; margin: 1em 0; padding: 1em;" data-pen-title="div要素全体にリンクをつける方法">
  <span>See the Pen <a href="https://codepen.io/iwato/pen/moJwZV/">
  div要素全体にリンクをつける方法</a> by iwato (<a href="https://codepen.io/iwato">@iwato</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>
