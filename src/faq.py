import json
import jieba
import jieba.posseg as pseg
import string

dataset = "../dataset/output.json"
chineseDict = "../dict.txt.big"

jieba.set_dictionary(chineseDict)

dataJsonList = []
questionVecs = []

with open(dataset, 'r', encoding="utf-8") as data:
    jsonObj = data.readline()
    while jsonObj:
        questionVec = {}
        dict = json.loads(jsonObj)
        dataJsonList.append(dict)
        questionWordList = pseg.lcut(dataJsonList[-1]["q:"])
        for word, attribute in questionWordList:
            questionVec[word] = questionVec.get(word, 1)
        questionVecs.append(questionVec)
        questionVecs.clear()
        jsonObj = data.readline()

