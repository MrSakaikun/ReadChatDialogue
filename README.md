# ReadChatDialogue

[雑談対話コーパス](https://sites.google.com/site/dialoguebreakdowndetection/chat-dialogue-corpus)
のjson形式のファイルから，UserとSystemの発話内容を組みのデータとして変換し，発話内容を表示したり，csv形式，もしくはbinaryfile形式に変換して保存するプログラムです．

以下は保存形式のイメージ
```
ユーザ発話1，システム発話1，ユーザ発話2，システム発話2・・・

↓

[[ユーザ発話1，システム発話1，（アノテーション）],
 [システム発話1，ユーザ発話2],
 [ユーザ発話2，システム発話2，（アノテーション）],
...
]

```
以下の形式で保存することも可能です．（使い方の5の末尾を参照してください）
```
ユーザ発話1，システム発話1，ユーザ発話2，システム発話2・・・

↓

[[ユーザ発話1，システム発話1，アノテーション1],
 [ユーザ発話2，システム発話2，アノテーション2],
 [ユーザ発話3，システム発話3，アノテーション3],
...
]
```

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
  * 通常ではall_pairが選択されています（User→SystemとSystem→Userの両方のデータが取得できます）．
  * System→Userのデータはアノテーションは含まれていません
  * User→Systemのみの組データが欲しい場合は，get_pair_chatdata.py の最後の行を，以下に書き換えてください．
  ```python
  if __name__ == '__main__':
      if len(sys.argv) != 2:
          print('保存形式(format)を指定してください')

      #outputDataフォルダがまだ存在していない場合はフォルダを作成
      if not os.path.isdir('./outputData'):
          os.mkdir('./outputData')

      #形式を指定して保存
      format = sys.argv[1]

      #User→SystemとSystem→Userの両方がセットとなったデータを取得する場合
      save_dataset_all_pair_chatdata(format=format)
      #User→Systemのデータのみを取得する場合
      save_dataset_user_to_system_chatdata(format=format)
  ```



## 保存形式について
#### csvの場合

csv形式で保存した場合は，

ユーザ発話，システム発話，各アノテーションの割合（O,T,X,ungrammatical-sentence の順に並ぶ）

という1発話1返答という形式が1行ずつ保存されている．

#### binaryfileの場合

binaryfile形式で保存した場合は，

* User→Systemの発話の時
```python
dialogue = {"user"        : userUtterance,
            "system"      : systemUtterance,
            "annotation"  :{"O":rate_O,
                            "T":rate_T,
                            "X":rate_X,
                            "G":rate_G}}
```
* System→Userの発話の時
```python
dialogue = {"system"	:systemUtterance,
            "user"    :userUtterance}
```



という1発話1返答のデータが辞書型として格納されている．このdialogue形式のデータが交互にいくつものlist型の配列として保存されている．


## 注意
プログラムの作成者とコーパスの著作者は異なります．そのため，このレポジトリには雑談対話コーパスは含まれていません．コーパスは

雑談対話コーパス:
<https://sites.google.com/site/dialoguebreakdowndetection/chat-dialogue-corpus>

からダウンロードしてください．また，コーパス利用時のライセンス等は[コーパス取得元のライセンス](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxkaWFsb2d1ZWJyZWFrZG93bmRldGVjdGlvbnxneDo3N2RkODA3Y2FjODgyNGI3)に従ってください.

また，通常ではall_pair（User→Systemの発話とSystem→Userの発話のデータを両方取得する）となっています．ただしSystem→Userの発話データにはアノテーションは付いていません．アノテーションが付いているデータのみを取得したい場合は「使い方」の5の末尾に書かれてある内容に従ってください．

## プログラム作成者
Yuya Sakai [MrSakaikun](https://github.com/MrSakaikun)

E-Mail:
yuyasakai1002[at]gmail.com

↑[at]を@に変えてください


## LICENSE
Please check [here](https://github.com/MrSakaikun/ReadChatDialogue/blob/master/LICENSE)

MIT License

Copyright (c) 2020 Yuya Sakai
