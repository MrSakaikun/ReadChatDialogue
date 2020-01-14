from get_from_oneJsonFile import get_from_oneJsonFile
import glob

def get_pair_chatdata():
    #読み込むjsonFileのリスト取得
    path_list = glob.glob('./json/*/*.json')

    #pairになっているchatデータを格納
    pair_chatdata = []

    #各pathに対してchatdataを取得
    for path in path_list:
        read_data = get_from_oneJsonFile(filepath=path)
        for data in read_data:
            pair_chatdata.append(data)

    #chatデータが1次元配列になっているものを返す
    return pair_chatdata

#データセットのcsvファイルを出力
def make_dataset_pair_chatdata():
    pass
