import json
import jieba
import jieba.posseg as pseg
import string
import math
from tqdm import tqdm

datasetPath = "../dataset/example.json"
chineseDict = "../dict.txt.big"
outPath = "../preprocessingData/exampleEmbedding.json"

print("Setting Chinese dictionary...")

jieba.set_dictionary(chineseDict)

dataJsonList = []
questionVecs = []

print("Loading data...")

with open(datasetPath, 'r', encoding="utf-8") as dataset:
    jsonObj = dataset.read()
    parseJson = json.loads(jsonObj)
    for paragraphID in parseJson:
        questionVec = {}
        dataJsonList.append(parseJson[paragraphID])
        questionWordList = pseg.lcut(dataJsonList[-1]["content"])
        for word, attribute in questionWordList:
            questionVec[word] = questionVec.get(word, 0) + 1
        questionVecs.append(questionVec)

print("Cutting...")

questionWordDict = {}
for wordDict in tqdm(questionVecs):
    for word in wordDict:
        questionWordDict[word] = questionWordDict.get(word, 0) + 1

print("Counting...")

QuestionNum = len(questionVecs)
for vec in tqdm(questionVecs):
    for w in vec:
        vec[w] = vec[w] * math.log10((QuestionNum + 1) / questionWordDict[w])

print("Writting...")

with open(outPath, "w", encoding="utf-8") as outfile:
    for dictionary in tqdm(questionVecs):
        json.dump(dictionary, outfile, ensure_ascii = False)
        outfile.write('\n')

