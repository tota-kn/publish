# node npmのscriptで引数を利用する

package.json
```json
{
	"scripts": {
		"hoge": "echo ${npm_config_fuga}"
	}
}
```

```sh
npm run hoge --fuga="Hello World"
## Hello World!
```
## 参考
[npm run スクリプトに引数を渡す方法 - Nodachisoft](https://nodachisoft.com/common/jp/article/jp000171/)
[package.jsonのscriptsに引数を渡す方法](https://zenn.dev/jojojo/articles/df1ff83890f83b)

