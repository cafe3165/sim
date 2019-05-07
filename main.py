import Similar as s
import rwfile as rwf
import datetime
nowTime1=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
print(nowTime1)
sentencelist = rwf.readfile()
print(sentencelist)
print(len(sentencelist))

dname = "50d.txt"

# sentence1 = "turn off the light in sitting room"
# v1 = s.calculate(dname, sentence1)
# sentence2 = "monitor the temperature of sitting room"
# v2 = s.calculate(dname, sentence2)
# #
# # print(v1)
# # print(v2)
# print(s.cos_sim(v1, v2))

sen2vec=[]
for sentence in sentencelist:
    v=s.calculate(dname,sentence)
    sen2vec.append(v)
rwf.writefile(sen2vec)
nowTime2=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
print(nowTime2)