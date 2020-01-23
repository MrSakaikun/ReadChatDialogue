# ReadChatDialogue

[雑談対話コーパス](https://sites.google.com/site/dialoguebreakdowndetection/chat-dialogue-corpus)
のjson形式のファイルから，対話内容を表示したり，csv形式，もしくはbinaryfile形式に変換して保存するプログラムです．

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

**注：コーパス利用時のライセンス等はコーパス取得元のライセンスに従ってください**

3. 解凍したフォルダ内の「json」フォルダを「ReadChatDialogue」フォルダに移動orコピーする

4. 対話コーパスの対話内容を見たい場合
  * show_oneJsonFile.py を以下の形式で実行（aaaaは一例）
  ```bash
  python show_oneJsonFile.py json/init100/aaaa.json
  ```

5. 対話コーパスをcsv or binaryfile 形式で保存したい場合
  * get_pair_chatdata.pyを以下の形式で実行
  ```bash
  python get_pair_chatdata.py csv
  python get_pair_chatdata.py binaryfile
  ```
  * outputDataフォルダが作成され，指定した形式のファイルが作成されます



## 保存形式について
#### csvの場合

csv形式で保存した場合は，

ユーザ発話，システム発話，各アノテーションの割合（O,T,X,ungrammatical-sentence の順に並ぶ）

という1発話1返答という形式が1行ずつ保存されている．

#### binaryfileの場合

binaryfile形式で保存した場合は，

```python
dialogue = {"user"        : userUtterance,
            "system"      : systemUtterance,
            "annotation"  :{"O":rate_O,
                            "T":rate_T,
                            "X":rate_X,
                            "G":rate_G}}
```

という1発話1返答のデータが辞書型として格納されている．このdialogue形式のデータがいくつものlist型の配列として保存されている．


## 注意
プログラムの作成者とコーパスの著作者は異なります．そのため，このレポジトリには雑談対話コーパスは含まれていません．コーパスは

雑談対話コーパス:
<https://sites.google.com/site/dialoguebreakdowndetection/chat-dialogue-corpus>

からダウンロードしてください．また，コーパス利用時のライセンス等は[コーパス取得元のライセンス](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxkaWFsb2d1ZWJyZWFrZG93bmRldGVjdGlvbnxneDo3N2RkODA3Y2FjODgyNGI3)に従ってください.


## プログラム作成者
Yuya Sakai [MrSakaikun](https://github.com/MrSakaikun)

E-Mail:
yuyasakai1002[at]gmail.com

↑[at]を@に変えてください


## LICENSE
Please check [here](https://github.com/MrSakaikun/ReadChatDialogue/blob/master/LICENSE)

MIT License

Copyright (c) 2020 Yuya Sakai
