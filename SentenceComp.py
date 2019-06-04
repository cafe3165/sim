import rwfile
import st
import datetime

sentenceList =[]
pathname1="command4.txt"
pathname2="sen2vec15.txt"

nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
print(nowTime)
sentenceList=rwfile.readfile2(pathname1)
orderList=[]
mapList=[]
print(sentenceList)
for i in sentenceList:
    L = st.returnSimilarSentence(i, pathname2,-5)
    print(list(L.keys()))
    orderList.append(list(L.keys()))
    mapList.append(L)

print(orderList)
rwfile.writefile2(mapList)
#
nowTime2=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
print(nowTime2)