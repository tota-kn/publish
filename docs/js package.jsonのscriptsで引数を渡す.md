[^1]
`-{key}` オプションをつけると `$npm_config_{key}` で取得できる

```json
{
	"scripts": {
		"test": "echo $npm_config_value" 
	 }
}
```

```sh
npm run test -value='TestValue'
# TestValue
```


[^1]: [package.jsonのscriptsに引数を渡す方法](https://zenn.dev/jojojo/articles/df1ff83890f83b)