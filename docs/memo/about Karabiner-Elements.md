# about Karabiner-Elements
キーマップを変更できるソフト
https://karabiner-elements.pqrs.org/


## 設定方法
 ~/.config/karabiner/karabiner.json
 に直接記載する。
 
```json
{
	"profiles": [
    {
            "complex_modifications": {
                "rules": [
                    {
                        "description": "left_control+h to left",
                        "manipulators": [
                            {
                                "from": {
                                    "key_code": "h",
                                    "modifiers": {
                                        "mandatory": [
                                            "left_control"
                                        ],
                                        "optional": [
                                            "any"
                                        ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "left_arrow"
                                    }
                                ],
                                "type": "basic"
                            }
                        ]
                    }
                ]
            }
        }]
}
```

もしくは`~/.config/karabiner/assets/complex_modifications/<任意のファイル名>.json`に以下のように書いて、Settings > Complex Modifications > Add ruleから設定する
```json
{
	"title": "これだけでもAdd rulesに表示されます。",
	"rules": [
		{ 
			"description": "descriptionだけ記述",
			"manipulators": [{}]
		}
	]
}
```