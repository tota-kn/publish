# git tagを新しい順で表示する
セマンティックバージョンの場合　`git tag --sort=-v:refname`　とする。
`refname`はタグ名、`-v:`は逆順にすることを意味している