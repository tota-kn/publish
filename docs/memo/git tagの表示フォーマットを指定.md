# git tagの表示フォーマットを指定
`git tag --format="%(authordate:short) %(refname:short)"`のようにフォーマットを指定できる。

表示できる値は以下

| キー             | 表示内容 |
| ---------------- | -------- |
| refname          | タグ名         |
| refname:short    | タグ名（短縮形式）         |
| authordate       | 日付         |
| authordate:short | 日付（YYYY-MM-DD形式）         |
