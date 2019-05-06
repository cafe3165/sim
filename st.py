import Similar
import rwfile

def returnSimilarSentence(sentence,filepath):
    vecs = []
    file = open(filepath, 'r', encoding='utf-8')

    for line in file.readlines():
        curLine = line.strip().split(" ")
        vecs.append(curLine[:])
    v1 = Similar.calculate("50d.txt", sentence).tolist()

    result = []
    for i in vecs:
        c = list(map(float, i))
        result.append(Similar.cos_sim(v1, c))
    sentenDict = {}
    for i in range(len(result)):
        sentenDict[i + 1] = result[i]

    sentenSortedSet = sorted(list(set(sentenDict.values())))

    sentenceList = rwfile.readfile()
    returnDict={}
    for i in sentenSortedSet[-3:]:
        for j in range(len(sentenDict)):
            if i == sentenDict[j + 1]:
                print(sentenceList[j + 1], round(i, 4))

                returnDict[j+1]=i
                break
    return returnDict