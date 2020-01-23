# ReadChatDialogue

雑談対話コーパス　<https://sites.google.com/site/dialoguebreakdowndetection/chat-dialogue-corpus>
のjson形式のファイルから，chat内容を表示したり，csv形式，もしくはbinaryfile形式に変換して保存するプログラムです．

## 動作環境

### 確認した動作環境
* Python 3.6.9 (anaconda3-5.0.0)

### 使用したパッケージ
* sys
* json
* glob
* csv
* pickle
* os

## 使い方

1. このレポジトリをクローンする
```bash
git clone https://github.com/MrSakaikun/ReadChatDialogue.git
cd ReadChatDialogue
```

2. [雑談対話コーパス](https://sites.google.com/site/dialoguebreakdowndetection/chat-dialogue-corpus)をダウンロードし，解凍する

**注：コーパス利用時のライセンス等はリンク先のライセンスに従ってください**

3. 解凍したフォルダ内の「json」フォルダを「ReadChatDialogue」フォルダに移動orコピーする

4. 対話コーパスの対話内容を見たい場合
  * show_oneJsonFile.py を以下の形式で実行

  ```bash
  python show_oneJsonFile.py JsonファイルのPath指定
  ```

5. 対話コーパスをcsv or binaryfile 形式で保存したい場合
  * get_pair_chatdata.pyを以下の形式で実行(以下はcsv形式で保存する場合)
  ```bash
  python get_pair_chatdata.py csv
  ```
  * outputDataフォルダが作成され，指定した形式のファイルが作成されます

## 注意
コーパス利用時のライセンス等はコーパス取得元のライセンスに従ってください

## 作成者
Yuya Sakai [MrSakaikun](https://github.com/MrSakaikun)

E-Mail:
mr.sakaikun[at]gmail.com

↑[at]を@に変えてください
