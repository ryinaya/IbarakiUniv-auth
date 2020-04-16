# IbarakiUniv-auth
茨城大学の学内有線LANの認証スクリプト

## 機能
再起動などで学内LANの認証情報が外れたときに、自動で認証するスクリプトです。
pingを行って疎通が確認できない場合に、認証フォームをサーバーに送信します。
定期的な実行機能は含まれていないので、crontabなどを使用してください。

いつもインターネットに接続する時、認証ページでログインしている環境に有効です。
（IbarakiUniv-g/IbarakiUniv-n/eduroamなどでは機能しません。）

「コロナウイルス蔓延防止でテレワークになったけど、研究室のサーバーの認証が切れてリモートから接続できない」を防ぎます。

## インストール
実行ファイル形式は以下からダウンロードしてください。
- Linux
- Mac
- Windows (動作未確認)

1. zipファイルを展開後、IbarakiUniv-authのディレクトリごと任意の場所に配置してください。
2. 配置後、config.pyの<YourID>と<YourPassword>を個々の統一アカウントの情報に書き換えてください。

## 使い方
### 自動実行の設定例
crontab(Linux/Mac)またはタスクスケジューラ(Win)で起動時や30分ごとなどに実行するよう設定します。
以下はcrontabの記述例です。
```crontab(このコードのコピペでは動きません。)
@reboot /home/example/IbarakiUniv-auth/auth-request #起動時に実行する
*/60 * * * * /home/example/ユーザー名/IbarakiUniv-auth/auth-request #60分ごとに実行する

```
詳しくは各自の環境に合わせて検索してください。

### パスワード等の取り扱い
パスワードが記載されてるconfig.pyは権限を600等の自分以外閲覧不可に設定することを推奨します。
```bash
chmod 600 IbarakiUniv-auth/config.py
```

### すでに学内の目的のサーバーに接続できない場合
このスクリプトだけではどうすることもできません。
他に認証できているサーバーがあれば、それ経由で接続できるかもしれません...

## このgitリポジトリをcloneしたとき
自分でbuildするとき、ソースコードを改変するとき、またはpython環境が十分に揃っている場合など。
### 要求環境
- Python3
- requests
pipenvを使用する場合は、`pipenv install`を実行してください。
それ以外の場合はpipでインストールしてください。
