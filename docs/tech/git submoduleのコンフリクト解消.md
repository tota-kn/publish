# git submoduleのコンフリクト解消
1. コンフリクトしているサブモジュールごとに、`git reset -- path/to/submodule` を実行する
1. サブモジュールのディレクトリに移動して、必要な変更をプルまたはチェックアウトします1。
1. 上位のリポジトリに戻って、`git add path/to/submodule` を実行して、サブモジュールの変更をステージングする
1. `git commit -m "Resolve submodule conflict"` などとして、コンフリクトを解決したことをコミットする