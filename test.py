#!/usr/bin/python3
import numpy as np

# print("Hello, World!")
data = []
for line in open("words.txt","r"): #设置文件对象并读取每一行文件
    data.append(line.strip('\n').split(','))               #将每一行文件加入到list中
print(data[0])
# list1=[]
# with open('words.txt', 'r') as f1:
#     list1 = f1.readlines()
# for i in range(0, len(list1)):
#     list1[i] = list1[i].rstrip('\n')
# list11=[]
# print(list1)
#
# for i in list1:
#     list11.append(i.strip(' ').split(','))
# print(list11)
# list12=[]
#
# for i in list11:
#     print(i)




# data2=[]
# data2= np.loadtxt("words.txt")   #将文件中数据加载到data数组里
# print(data2)
with open("words.txt","r") as file:
    result=[]
    for line in file.readlines():
        result.append(list(map(str,line.strip().split(','))))
    print(result[0][0])


