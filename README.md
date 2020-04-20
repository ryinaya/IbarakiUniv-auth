# IbarakiUniv-auth
茨城大学の学内有線LANの認証スクリプト<br>
**ダウンロードは[releases](https://github.com/ryinaya/IbarakiUniv-auth/releases/latest)から行ってください。右上の緑のボタンではスクリプトはダウンロードできません。**

## 機能
再起動、ネットワーク障害などで学内LANの認証情報が外れたときに、自動で認証するスクリプトです。<br>
pingを行って疎通が確認できない場合に、認証フォームをサーバーに送信します。<br>
定期的な実行機能は含まれていないので、crontabなどを使用してください。<br>

**いつもインターネットに接続する時、認証ページでログインしている環境でのみ有効です。**<br>
*（IbarakiUniv-g/IbarakiUniv-n/eduroamなどでは機能しません。）*<br>

「コロナ対策でテレワークになったけど、研究室のサーバーの認証が切れてリモートから接続できない」を防ぎます。<br>

## 動作環境
- Linux
- Mac (多分HighSierra以降)
- Windows

## ダウンロードと設定
1. 実行ファイル形式の入ったzipを[releases](https://github.com/ryinaya/IbarakiUniv-auth/releases/latest)からダウンロードする
2. zipファイルを展開後、IbarakiUniv-authのディレクトリごと任意の場所に配置する
3. 配置後、config.txtの\<YourID\>と\<YourPassword\>をあなたの大学アカウントの情報に書き換える

## 使い方

### コマンドラインで実行する
一回だけ実行されます。

```
$ cd IbarakiUniv-auth
$ ./auth-request
```

この時、同じディレクトリにauth-request.logというログファイルが生成されます。<br>
pingを行って疎通が確認できない場合に、認証フォームをサーバーに送信し、その旨をログファイルに書き込みます。<br>

### 便利なオプション
`auth-request`の後に引数として`-n`や`-a`などを追加することで、<br>
ログファイルの生成・書き込みなど実行時の動作が変化します。<br>
- `./auth-request -n`: ログファイルに記述しない
- `./auth-request -a`: ログファイルにpingの成功も記述する
- `./auth-request -c`: 実行する前にログファイルの中身を消去する
- `./auth-request -h`: 実行せずスクリプトのヘルプを表示する

### 定期的に実行する
「定期的に認証を確認して、切れたら認証する」といったことをやりたい場合、<br>
cron(Linux/Mac)またはタスクスケジューラ(Win)など各OSの自動実行機能を利用してください。<br>

以下はcron(Linux/Mac)の記述例です。(`~/path_to/IbarakiUniv-auth`の部分を適宜書き換えてください。)<br>
```
@reboot bash -l -c "~/path_to/IbarakiUniv-auth/auth-request -c" #システム起動時にログファイルを消去して実行する
15 * * * * bash -l -c "~/path_to/IbarakiUniv-auth/auth-request -a" #毎時15分に実行する。pingが成功した場合も記述する。
```
cronの設定方法は[「cronの設定方法 - Qiita.com」](https://qiita.com/hikouki/items/e744b3a4d356d2af12cf)などを参照してください。<br>
必ず一回は正常に動作した確認をおすすめします。（[環境変数が原因でうまく動かないこともあるので](https://www.greptips.com/posts/790/)、`bash -l -c "コマンド"`か絶対パスで記述するほうがいいと思います。）<br>

Windowsの場合は[「タスクスケジューラで定期的な作業を自動化する - @IT」](https://www.atmarkit.co.jp/ait/articles/1305/31/news049.html)、[「Windowsでログオフ中でもタスクを起動させる方法 - @IT」](https://www.atmarkit.co.jp/ait/articles/1307/08/news101.html)などを参考にしてください。


## パスワード等の取り扱い
パスワードが記載されてるconfig.pyは権限を600等の自分以外閲覧不可に設定することを推奨します。<br>

```bash
chmod 600 IbarakiUniv-auth/config.py
```

## すでに学内の目的のサーバーに接続できない場合
このスクリプトだけではどうすることもできません。<br>
~~他に認証できているサーバーがあれば、それ経由で接続できるかもしれません...~~<br>
手遅れだと思われます。仕方がないので、何かのついでに学内で認証してからインストールしてください。

## なんか実行できなかった場合
[issues](https://github.com/ryinaya/IbarakiUniv-auth/issues)タブから新しいissueを作成し報告してくれると嬉しいです。(要githubアカウント)<br>
報告は日本語でいいので、実行した環境、出てきたエラーなども内容に含めてください。

## このgitリポジトリをcloneしたとき
自分でbuildするとき、ソースコードを改変するとき、またはpython環境が十分に揃っている場合など。
### Requirements
- Python3
- requests

pipenvを使用する場合は、`pipenv install`を実行することで、環境の再現ができます。<br>
使用しない場合はpip等でインストールしてください。

## ライセンス
このソースコードはMITライセンスで公開しています。
