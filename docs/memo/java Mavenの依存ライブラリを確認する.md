# java Mavenの依存ライブラリを確認する
1. `pom.xml`が配置してあるディレクトリに移動する
2.  `mvn  -DoutputFile=output.txt dependency:tree`  コマンドを実行する
3. `output.txt`が出力され、依存ライブラリの内容が記載されているので確認する

## 参考
- [Java: Mavenプロジェクトの依存ライブラリを確認する(dependency:tree) - Qiita](https://qiita.com/flyaway/items/1df3ce9b4dae6f6e5e28)