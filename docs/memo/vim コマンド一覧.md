# vim コマンド一覧

[https://gihyo.jp/assets/files/magazine/SD/2015/201510/download/Furoku_CheatSheet_Vim.pdf](https://gihyo.jp/assets/files/magazine/SD/2015/201510/download/Furoku_CheatSheet_Vim.pdf)

## 基本

| key                      | operation |
| ------------------------ | --------- |
| back                     | u         |
| forward                  | ctrl + r  |
| repeat                   | .         |

## insert mode

| key                      | operation |
| ------------------------ | --------- |
| insert mode (カーソル右  | a         |
| insert mode (カーソル左) | i         |
| insert mode (行末)       | A /$a        |
| insert mode (行頭)       | I / ^i        |
| insert mode (上に行追加) | O / ko        |
| insert mode (下に行追加) | o         |
| 行を削除                 | S / cc / ^C         |
| 文字を削除               | s / cl      |
| 単語を削除               | cw          |


## 削除

一文字消す　x

一単語消す（空白も削除する）　dw
一単語消す（空白は削除しない）　de
行末まで消す　d$
行全体を削除　dd

単語の末尾まで削除して入力 ce
行末まで消す　c$
行全体を削除して入力　cc


## 移動
行頭に移動　0
行末に移動 $

1単語先に移動　w
1単語前に移動　b

## コピペ
行切り取り　dd
貼り付け p

## 入力
文字の置き換え r*