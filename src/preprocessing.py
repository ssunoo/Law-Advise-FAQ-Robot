import json
import jieba
import jieba.posseg as pseg
import string
import math

dataset = "../dataset/output.json"
chineseDict = "../dict.txt.big"
out = "../preprocessingData/questionsData.json"

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
            questionVec[word] = questionVec.get(word, 0) + 1
        questionVecs.append(questionVec)
        jsonObj = data.readline()

questionWordDict = {}
for wordDict in questionVecs:
    for word in wordDict:
        questionWordDict[word] = questionWordDict.get(word, 0) + 1

QuestionNum = len(questionVecs)
for vec in questionVecs:
    for w in vec:
        vec[w] = vec[w] * math.log10((QuestionNum + 1) / questionWordDict[w])

with open(out, "w", encoding="utf-8") as outfile:
    for dictionary in questionVecs:
        json.dump(dictionary, outfile, ensure_ascii = False)
        outfile.write('\n')

