#! python coding:utf-8

import sys
import json

#Jsonファイル1つに入っている対話データを表示する関数
def get_from_oneJsonFile(filepath):
	#jsonファイル読み込み
	f = open(filepath, "r")
	json_data = json.load(f)

	#対話タグ
	"""
	print ("dialogue-id : " + json_data["dialogue-id"])
	print ("speaker-id : " + json_data["speaker-id"])
	print ("group-id : " + json_data["group-id"])
	"""

	#JsonFile内の対話ログを組みにして返す
	getDialogue = []
	userUtterance = ""
	systemUtterance = ""


	#対話データとアノテーションのカウント結果を表示
	for turn in json_data["turns"]:
		s = turn["speaker"] + ":" + turn["utterance"]

		#ユーザ発話のturn
		if turn["speaker"] == 'U':
			userUtterance = turn["utterance"]
			#システム発話のturnに移動
			continue

		#システム発話のturn
		systemUtterance = turn["utterance"]

		#アノテーションパラメータ初期設定
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

		#アノテーションカウント結果表示(O,T,X,ungrammatical-sentence の順で割合で表示)
		"""
		if turn["annotations"]:
			a = str(count_O / count_all) + ',' + str(count_T / count_all) + ',' + str(count_X / count_all) + ',' + str(sentense_True / count_all)
			print('annotation:'+a)
		"""
		rate_O = count_O / count_all
		rate_T = count_T / count_all
		rate_X = count_X / count_all
		rate_G = sentense_True / count_all

		#ユーザ発話，システム発話，アノテーションを辞書型として整形
		dialogue = {"user"        : userUtterance,
					"system"      : systemUtterance,
					"annotation"  :{"O":rate_O,
									"T":rate_T,
									"X":rate_X,
									"G":rate_G}}
		#1データ分を追加
		#if dialogue['user']!="":	もし最初のシステムの発話がいらない場合はこのif文を付ける
		getDialogue.append(dialogue)

	return getDialogue
