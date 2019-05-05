import rwfile
import st

sentenceList =[]
pathname1="command.txt"
pathname2="sen2vec3.txt"


sentenceList=rwfile.readfile2(pathname1)
orderList=[]
print(sentenceList)
for i in sentenceList:
    L = st.returnSimilarSentence(i, pathname2)
    print(list(L.keys()))
    orderList.append(list(L.keys()))

print(orderList)
rwfile.writefile2(orderList)
#
