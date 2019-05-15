import numpy as np


def readfile():
    pathname1 = "E:/ideaworkspace/littletest/vbd3.txt"
    pathname2 = "E:/ideaworkspace/littletest/vbc3.txt"
    pathname3 = "E:/ideaworkspace/littletest/ta2.txt"
    file1 = open(pathname1, 'r', encoding='utf-8')
    file2 = open(pathname2, 'r', encoding='utf-8')
    file3 = open(pathname3, 'r', encoding='utf-8')
    sentencelist1 = []
    sentencelist2 = []
    sentencelist3 = []

    for line in file1.readlines():
        curLine = line.strip()
        sentencelist1.append(curLine)
    for line in file2.readlines():
        curLine = line.strip()
        sentencelist2.append(curLine)
    for line in file3.readlines():
        curLine = line.strip()
        sentencelist3.append(curLine)

    sentencelist = sentencelist1 + sentencelist2+sentencelist3
    # print(sentencelist)
    return sentencelist


def readfile2(pathname):
    sentencelist = []
    file = open(pathname, 'r', encoding='utf-8')
    for line in file.readlines():
        curLine = line.strip()
        sentencelist.append(curLine)
    return sentencelist


def writefile(sen2vec):
    file = open(r'sen2vec15.txt', 'w')
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
    file = open(r'result15.txt', 'w')
    file2 = open(r'sim15.txt', 'w')
    print(noList)
    for i in noList:
        file.write(str(list(i.keys())).replace('[', '').replace(']', '').replace(',', '') + "\n")
        file2.write(str(list(i.values())).replace('[', '').replace(']', '').replace(',', '') + "\n")
