#! python coding:utf-8

from get_from_oneJsonFile import get_user_to_system_dialogue_from_oneJsonFile
import glob
import csv
import pickle
import os
import sys

#ユーザに対するシステムの発話とアノテーションのみ取得
def get_user_to_system_chatdata():
    #読み込むjsonFileのリスト取得
    path_list = glob.glob('./json/*/*.json')

    #pairになっているchatデータを格納
    pair_chatdata = []

    #各pathに対してchatdataを取得
    for path in path_list:
        read_data = get_user_to_system_dialogue_from_oneJsonFile(filepath=path)
        for data in read_data:
            pair_chatdata.append(data)

    #chatデータが1次元配列になっているものを返す
    return pair_chatdata

#ユーザに対するシステムの発話のデータを保存
def save_dataset_user_to_system_chatdata(format):
    #ファイルが存在する場合は再作成を行うかどうかの確認を行う
    fileName = './outputData/pair_chatdata.'+format
    if os.path.isfile(fileName):
        print(fileName+"は存在しています．再作成しますか？再作成する場合はcを，それ以外はqを入力してください")
        if not "c" == input():
            return

    #データを取得
    pair_chatdata = get_user_to_system_chatdata()

    #csv形式で保存
    if format=='csv':
        with open(fileName,'w') as f:
            writer = csv.writer(f)
            writer.writerow(["user","system","annotation_O","annotation_T","annotation_X","annotation_G"])
            for chat in pair_chatdata:
                writer.writerow([chat["user"],
                                chat["system"],
                                chat["annotation"]["O"],
                                chat["annotation"]["T"],
                                chat["annotation"]["X"],
                                chat["annotation"]["G"]])

    #binaryfile形式で保存
    if format=='binaryfile':
        with open(fileName,'wb') as f:
            pickle.dump(pair_chatdata,f)


#ユーザに対するシステムの発話のデータを保存
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('保存形式(format)を指定してください')

    #outputDataフォルダがまだ存在していない場合はフォルダを作成
    if not os.path.isdir('./outputData'):
        os.mkdir('./outputData')

    #形式を指定して保存
    format = sys.argv[1]
    save_dataset_user_to_system_chatdata(format=format)
