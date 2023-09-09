# -*- coding: utf-8 -*-
from snownlp import SnowNLP

txt = open("E:\KG\实验三数据集\红楼1.txt","r",encoding="utf-8").read()
s = SnowNLP(txt)
tags=[x for x in s.tags]
print(tags)
a=[]
for i in range(len(tags)):
    if tags[i][1]=='nr' and tags[i+1][1]=='nr':
        #print(tags[i])
        #print(tags[i+1])
        a.append(tags[i][0]+tags[i+1][0])
#print(a)

fi = open("D:/KG/renwu/snow人物角色提取.txt","w",encoding="utf-8")
for i in range(len(a)):
    '''    if tags[i][1]=='nr':'''
    fi.write(a[i]+'\n')

fi.close()
