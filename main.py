import Similar as s
import rwfile as rwf
sentencelist=rwf.readfile()
print(sentencelist)
print(len(sentencelist))

# sentence1="turn on the light"
dname="100d.txt"
# v1=s.calculate(dname,sentence1)
# sentence2 = "shut the light down"
# v2=s.calculate(dname,sentence2)
# print(s.cos_sim(v1,v2))
sen2vec=[]
for sentence in sentencelist:
    v=s.calculate(dname,sentence)
    sen2vec.append(v)
rwf.writefile(sen2vec)


