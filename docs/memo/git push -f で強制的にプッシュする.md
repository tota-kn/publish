# git push -f で強制的にプッシュする
リモートリポジトリにプッシュ済みの内容を`git rebase`や[[git commit --amendで直前のコミットを変更する]]などで変更した場合、その変更を`git push`しようとするとエラーが発生する。
この場合は`git push --force` または`git push -f` を利用するとプッシュができる。ただしこれは他人の作業を上書きする可能性があるので基本的に利用すべきでない。
[[git push --forceではなく--force-with-leaseを利用する]]