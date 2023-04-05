# docker DockerDesktopをRancherDesktopに移行
## 環境
Mac(intel)

## 手順
1. DockerDesktopを起動していたら終了する
2. DockerDesktopをアンインストール（Finderでアプリケーションフォルダから削除）
3. `~/.docker`フォルダを削除（この手順を実行しないと[このエラー](https://github.com/rancher-sandbox/rancher-desktop/issues/2534`#issuecomment-1485193048)が発生する）`
4. [Rancher Desktop](https://rancherdesktop.io/)からRancherDesktopをダウンロード、インストールする
5. RancherDesktopを起動するとダイアログが出るので以下で設定してAccept
	1. dockered(moby)
	2. Automatic
6. 再びダイアログが出るので`Always run without administrative acces`にチェックを入れてOK
7. 起動が完了したら移行完了　`docker-compose build`, `docker compose up`コマンドなどが動くか確認する