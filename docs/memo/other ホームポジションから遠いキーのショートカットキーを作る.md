[[about Karabiner-Elements]]を利用して以下の設定を行う。

# 対応表
emacsキーバインディングに従って設定した。

| 変更前                  | 変更後      |
| ----------------------- | ----------- |
| ↑                       | control + p |
| ↓                       | control + n |
| →                       | control + f |
| ←                       | control + b |
| enter(return)           | control + m |
| backspace(delete)       | control + h |
| fn +  backspace(delete) | control + d |

# karabiner設定
矯正のために変更前のキーは動作しないようにした。
```json
{
    "profiles": [
        {
            "complex_modifications": {
                "rules": [
                    {
                        "description": "emacs key binding",
                        "manipulators": [
                            {
                                "from": {
                                    "key_code": "b",
                                    "modifiers": {
                                        "mandatory": [
                                            "control"
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
                            },
                            {
                                "from": {
                                    "key_code": "f",
                                    "modifiers": {
                                        "mandatory": [
                                            "control"
                                        ],
                                        "optional": [
                                            "any"
                                        ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "right_arrow"
                                    }
                                ],
                                "type": "basic"
                            },
                            {
                                "from": {
                                    "key_code": "p",
                                    "modifiers": {
                                        "mandatory": [
                                            "control"
                                        ],
                                        "optional": [
                                            "any"
                                        ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "up_arrow"
                                    }
                                ],
                                "type": "basic"
                            },
                            {
                                "from": {
                                    "key_code": "n",
                                    "modifiers": {
                                        "mandatory": [
                                            "control"
                                        ],
                                        "optional": [
                                            "any"
                                        ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "down_arrow"
                                    }
                                ],
                                "type": "basic"
                            },
                            {
                                "from": {
                                    "key_code": "m",
                                    "modifiers": {
                                        "mandatory": [
                                            "control"
                                        ],
                                        "optional": [
                                            "any"
                                        ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "return_or_enter"
                                    }
                                ],
                                "type": "basic"
                            },
                            {
                                "from": {
                                    "key_code": "h",
                                    "modifiers": {
                                        "mandatory": [
                                            "control"
                                        ],
                                        "optional": [
                                            "any"
                                        ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "delete_or_backspace"
                                    }
                                ],
                                "type": "basic"
                            },
                            {
                                "from": {
                                    "key_code": "d",
                                    "modifiers": {
                                        "mandatory": [
                                            "control"
                                        ],
                                        "optional": [
                                            "any"
                                        ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "delete_forward"
                                    }
                                ],
                                "type": "basic"
                            }
                        ]
                    }
                ]
            },
            "simple_modifications": [
                {
                    "from": {
                        "key_code": "delete_or_backspace"
                    },
                    "to": [
                        {
                            "key_code": "vk_none"
                        }
                    ]
                },
                {
                    "from": {
                        "key_code": "down_arrow"
                    },
                    "to": [
                        {
                            "key_code": "vk_none"
                        }
                    ]
                },
                {
                    "from": {
                        "key_code": "left_arrow"
                    },
                    "to": [
                        {
                            "key_code": "vk_none"
                        }
                    ]
                },
                {
                    "from": {
                        "key_code": "return_or_enter"
                    },
                    "to": [
                        {
                            "key_code": "vk_none"
                        }
                    ]
                },
                {
                    "from": {
                        "key_code": "right_arrow"
                    },
                    "to": [
                        {
                            "key_code": "vk_none"
                        }
                    ]
                },
                {
                    "from": {
                        "key_code": "up_arrow"
                    },
                    "to": [
                        {
                            "key_code": "vk_none"
                        }
                    ]
                }
            ]
        }
    ]
}
```
----
## Related Notes
- 

## References
- 

## Tags
- 