import Similar
import rwfile

def returnSimilarSentence(sentence,filepath,rank):
    vecs = []
    file = open(filepath, 'r', encoding='utf-8')

    for line in file.readlines():
        curLine = line.strip().split(" ")
        vecs.append(curLine[:])
    v1 = Similar.calculate("50d.txt", sentence).tolist()
    # print(v1)
    result = []
    for i in vecs:
        c = list(map(float, i))
        result.append(Similar.cos_sim(v1, c))
    sentenDict = {}
    # ii=0
    # for i in result:
    #     print(i,ii)
        # ii+=1
    for i in range(len(result)):
        sentenDict[i] = result[i]
        # print(sentenDict[i])

    sentenSortedSet = sorted(list(set(sentenDict.values())))

    sentenceList = rwfile.readfile()
    returnDict={}
    # print(sentenSortedSet)
    # print(sentenSortedSet[-3:])
    for i in sentenSortedSet[rank:]:
        for j in range(len(sentenDict)):
            if i == sentenDict[j]:
                print(sentenceList[j], round(i, 4),j)
                returnDict[j]=i
                break
    return returnDict