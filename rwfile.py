import numpy as np


def readfile():
    pathname1 = "D:/idea_workspace/littletest/vbd.txt"
    pathname2 = "D:/idea_workspace/littletest/vbc.txt"
    file1 = open(pathname1, 'r', encoding='utf-8')
    file2 = open(pathname2, 'r', encoding='utf-8')
    sentencelist1 = []
    sentencelist2 = []
    for line in file1.readlines():
        curLine = line.strip()
        sentencelist1.append(curLine)
    for line in file2.readlines():
        curLine = line.strip()
        sentencelist2.append(curLine)

    sentencelist = sentencelist1 + sentencelist2
    return sentencelist


def readfile2(pathname):
    sentencelist = []
    file = open(pathname, 'r', encoding='utf-8')
    for line in file.readlines():
        curLine = line.strip()
        sentencelist.append(curLine)
    return sentencelist


def writefile(sen2vec):
    file = open(r'newsen2vec.txt', 'w')
    # print(sen2vec.tolist())
    # print(type(sen2vec))
    # print(type(sen2vec[0]))

    ff = []
    # print(len(sen2vec))
    for i in sen2vec:
        # print(len(i))

        f = i.tolist()
        temp = []
        for j in f:
            temp.append(round(j, 5))

        ff.append(temp)
        # ff.append(round(f,5))

    # print(ff)
    for k in ff:
        print(k)
        file.write(str(k).replace('[', '').replace(']', '').replace(',', '') + "\n")
    file.close()

def writefile2(noList):
    file = open(r'result7.txt', 'w')
    file2 = open(r'sim7.txt', 'w')
    print(noList)
    for i in noList:
        file.write(str(list(i.keys())).replace('[', '').replace(']', '').replace(',', '') + "\n")
        file2.write(str(list(i.values())).replace('[', '').replace(']', '').replace(',', '') + "\n")
