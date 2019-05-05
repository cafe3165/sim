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
sentence ="enhance the temperature of sitting room"
pathname="sen2vec3.txt"
L=st.returnSimilarSentence(sentence,pathname)
print(list(L.keys()))
print(L.values())