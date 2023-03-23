# git submoduleのssh-http接続を変更する
1. `.gitmodules`のurlを変更  
```
[submodule "src/common"]
	path = src/submodule
	url = https~~~~
```

2. `git submodule sync`を実行