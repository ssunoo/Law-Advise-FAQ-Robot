import json
import jieba
import jieba.posseg as pseg

chineseDict = "../dict.txt.big"
dataset = "../dataset/output.json"
preprocessingData = "../preprocessingData/questionsData.json"

jieba.set_dictionary(chineseDict)

questionsList = []
with open(dataset, 'r', encoding="utf-8") as data:
    jsonObj = data.readline()
    while jsonObj:
        dict = json.loads(jsonObj)
        questionsList.append(dict)
        jsonObj = data.readline()

questionsVec = []
with open(preprocessingData, 'r', encoding="utf-8") as data:
    jsonObj = data.readline()
    while jsonObj:
        vec = json.loads(jsonObj)
        questionsVec.append(vec)
        jsonObj = data.readline()

query = input("Enter your question: ")
queryWordList = pseg.lcut(query)
queryVec = {}
for word, attribute in queryWordList:
    queryVec[word] = queryVec.get(word, 0) + 1
disQuery = 0
for w in queryVec.values():
    disQuery += w**2
disQuery = disQuery**(0.5)

similarQuestionDict = {}

for ids, question in enumerate(questionsVec):
    product = 0
    for word in queryVec:
        product += queryVec[word] * question.get(word, 0)
    
    disQuestion = 0
    for w in question.values():
        disQuestion += w**2
    disQuestion = disQuestion**(0.5)

    similarQuestionDict[ids] = product / (disQuery * disQuestion)

sortSimilarQuestionDict = sorted(similarQuestionDict.items(), key=lambda x: x[1], reverse=True)
print(questionsList[sortSimilarQuestionDict[0][0]]["a:"])








