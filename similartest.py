import Similar
# sentence1="raise the temperature of sitting room"
sentence1="enhance the temperature of sitting room"


file=open(r"sen2vec.txt",'r',encoding='utf-8')
vecs=[]
for line in file.readlines():
    curLine = line.strip().split(" ")
    vecs.append(curLine[:])
v1= Similar.calculate("100d.txt",sentence1).tolist()
# print(v1)
result=[]
for i in vecs:
    c=list(map(float,i))
    result.append(Similar.cos_sim(v1,c))

print(result)
max=result[0]
count=0

for i in result:
    count=count+1
    if i>max:
        max=i
        f=count
    else:
        continue
print(f)
    # print(c)
    # print(curLine)





