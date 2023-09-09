# coding:utf-8
from py2neo import Graph, Node, Relationship,NodeMatcher,Path,Subgraph
import pandas as pd
import csv
##连接neo4j数据库，输入地址、用户名、密码
graph=Graph("http://localhost:7474", auth=("neo4j", "123456"))

graph.delete_all()

with open('D:\KG\ex1.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader) # 导入csv文件

for i  in  range(1,len(data)):
    node = Node('person',name = data[i][0],stu_id = data[i][1])
    graph.create(node) # 创建人物节点，拥有 学号“stu_id” 和 姓名“name” 两个属性

f=0 # 用于获取关系条数,方便后面进行关系数据的存储
for i  in  range(1,len(data)):
    for j in data[i][2].split('，') :
        for k in range(i+1,len(data)) :
            if j in data[k][2].split('，') :
                #m=[data[i][0],data[k][0],j]
                f=f+1
                #print(m)
#print(f)
list_guanxi=[[0 for i in range(3)] for j in range(f)] # 创建空的二维数组，其正好可以包含全部的关系
#print(list_guanxi)

f=0 # 用于表示关系编号
for i  in  range(1,len(data)): # 第二次循环，将关系存入数组中，目前没有改进方法
    for j in data[i][2].split('，') :
        for k in range(i+1,len(data)) :
            if j in data[k][2].split('，') :
                m=[data[i][1],data[k][1],j]
                list_guanxi[f]=m
                #print(list_guanxi[f])
                f=f+1
#print(list_guanxi)


graph = Graph()
matcher = NodeMatcher(graph)
for i in range(0,len(list_guanxi)):
    #node=matcher.match('person').where(stu_id=list_guanxi[i][0]).first()
    #print(node)
    guanxi = 'guanxi' + str(i)
    guanxi = Relationship(matcher.match('person').where(stu_id=list_guanxi[i][0]).first(), list_guanxi[i][2], matcher.match('person').where(stu_id=list_guanxi[i][1]).first())
    # 通过 stu_id 匹配node节点，进行关系创建
    graph.create(guanxi)

'''for i  in  range(1,len(data)):
    for j in range(1, len(data)):
        if(data[i][0]!=data[j][0]) :
            tongxue='tongxue'+str(i)+str(j)
            tongxue = Relationship(matcher.match('person').where(name=data[i][0]).first(), '同学', matcher.match('person').where(name=data[j][0]).first())
            # 通过 name 匹配node节点，进行关系创建
            graph.create(tongxue)


  
graph = Graph()
matcher = NodeMatcher(graph)
guanxi = Relationship(matcher.match('person').where(stu_id='20011419').first(), 'guanxi', matcher.match('person').where(stu_id='20011448').first())
 
 #print(node)
graph = Graph()
matcher = NodeMatcher(graph)
node=matcher.match('person').where(name='朱明方').first()
print(node)

for i in range(0,len(list_guanxi)):
    guanxi='guanxi'+str(i)
    guanxi = Relationship(node_matcher.match("Person").where(name=list_guanxi[i][0]), list_guanxi[i][2],node_matcher.match("Person").where(name=list_guanxi[i][1]))

print(node)

  node_matcher = NodeMatcher(graph)
node = node_matcher.match("Person").where(age=20).first()

match (from:student{id:line.student_id}),(to:school {id:line.school_id})
merge (from)-[r:学校]->(to)#创建标签为学校的关系

a=[]
for i  in  range(1,len(data)):
    a=a+data[i][2].split('，')
a=set(a)


for i  in  range(1,len(data)):
    node = Node('person',name = data[i][0],id = data[i][1]) 
    graph.create(node)
    
for i  in  range(1,len(a)):
    relation = Node('xingqu',name = a[i])
    xingqu  = Relationship(node,a[i],relation)

#print(a)'''