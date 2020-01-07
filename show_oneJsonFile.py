#! python coding:utf-8

import sys
import json

#Jsonファイル1つに入っている対話データを表示する関数
def show_oneJsonFile(filepass):
	#jsonファイル読み込み
	f=open(filepass, "r")
	json_data = json.load(f)

	#対話タグ
	print ("dialogue-id : " + json_data["dialogue-id"])
	print ("speaker-id : " + json_data["speaker-id"])
	print ("group-id : " + json_data["group-id"])

	#対話データとアノテーションのカウント結果を表示
	for turn in json_data["turns"]:
		s = turn["speaker"] + ":" + turn["utterance"]

		count_all = len(turn["annotations"])
		count_O = 0
		count_T = 0
		count_X = 0
		sentense_True = 0

		#各被験者のアンケートの読み込み
		for annotate in turn["annotations"]:
			#対話破綻かどうか
			if annotate["breakdown"] == 'O':
				count_O += 1
			elif annotate["breakdown"] == 'T':
				count_T += 1
			else:
				count_X += 1
			#非文かどうか
			if annotate["ungrammatical-sentence"] == 'O':
				sentense_True += 1

		#話者と発話内容を表示
		print (s)
		#アノテーションカウント結果表示(O,T,X,ungrammatical-sentence の順で割合で表示)
		if turn["annotations"]:
			a = str(count_O / count_all) + ',' + str(count_T / count_all) + ',' + str(count_X / count_all) + ',' + str(sentense_True / count_all)
			print('annotation:'+a)




if __name__ == '__main__':
	argvs = sys.argv
	argc = len(argvs)

	if argc < 2:
		print ("usage:python argvs[0] filename")
	else:
		show_oneJsonFile(filepass=argvs[1])
