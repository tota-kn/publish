# git push --forceではなく--force-with-leaseを利用する
[[git push -f で強制的にプッシュする]]はは他人の作業を破壊する可能性があるため、`--force` の代わりに `--force-with-lease` を利用することが推奨される。
`--force-with-lease` はローカルの変更日時がリモートの変更日時よりも新しい場合にのみプッシュが成功する。
注意点として、ただし直前にgit fetchしている場合はプッシュが必ず成功してしまう

## 参考
[git push -f をやめて --force-with-lease を使おう - Qiita](https://qiita.com/wMETAw/items/5f47dcc7cf57af8e449f)