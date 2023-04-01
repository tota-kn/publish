# karabiner "Please allow Karabiner-virtualHDDevice-Manager system software"の表示が出て動作しない
## 環境
MacOS : Ventura 13.2.1
Karabiner-Elements : 14.11.0

## 事象
いつのまにかKarabinerで設定したキーバインドが動作しなくなっていた。
再起動すると以下のダイアログが一瞬だけ現れる。

![[Pasted image 20230401220142.png]]

## 対処法
`システム環境設定 > プライバシーとセキュリティ > フルディスクアクセス` を開き、karabiner_grabberを有効にする。
その後PCを再起動したら直った。

## 参考
[「Karabiner-Elements Alert」のダイアログが出てきて、Karabiner-Elementsが使えない場合の対処法 – Webrandum](https://webrandum.net/karabiner-elements-alert/)