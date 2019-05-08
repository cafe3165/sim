import numpy as np
import rwfile
import st

# x = np.zeros(5)
# print(x)
# y = np.zeros((50,), dtype=np.float)
# print(y)
#
#
# def calculateVec(sentence):
#     s = sentence.split(" ")
#     print(s)
#
#
# calculateVec("turn on the light")
#
# list = [1, 2, 3, 4, 5, 6, 7, 8]
#
# print(list[-10:])
#
# sl = rwfile.readfile()
# sd={}
# nl=[]
# for i in range(len(sl)):
#     nl.append(i+1)
#     sd[i+1]=sl[i]
# print(sd)
#
# print(sorted())


# print(sl)
# sentence ="enhance the temperature of sitting room"
# pathname="sen2vec3.txt"
# L=st.returnSimilarSentence(sentence,pathname)
# print(list(L.keys()))
# print(L.values())

sl = rwfile.readfile()
print(sl)

filer = open('result6.txt', 'r', encoding='utf-8')
# file2=open('command4.txt', 'r', encoding='utf-8')
cl = rwfile.readfile2('command4.txt')
print(cl)
l1 = []
l2 = []
for line in filer.readlines():
    curLine = line.strip().split(" ")
    l2.append(list(map(int, curLine)))
    # print(list(map(int,curLine)))
print(l2)
index = 0
filetest = open(r'com33.txt', 'w')
filetest2 = open(r'sim6.txt', 'r')

ll = []
for line in filetest2.readlines():
    curLine = line.strip().split(" ")
    ll.append(list(map(float, curLine)))

print(ll)
llindex=0
print(len(ll))
for i in l2:
    # print(cl[index])
    filetest.write(cl[index])
    filetest.write('\n')
    # print(ll[llindex])
    li=0
    for j in i:
        print(sl[j],ll[llindex][li])
        filetest.write(sl[j])
        filetest.write(' ')
        filetest.write(str(ll[llindex][li]))
        filetest.write('\n')
        li+=1
    llindex+=1
    print('\n')
    filetest.write('\n')
    index+=1
#
