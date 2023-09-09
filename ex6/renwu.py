import json
# 读取下载的json文件
f=open('E:/KG/neo4j-community-3.5.5/import/renwu.json', 'r', encoding='utf-8')
data = []
for line in f.readlines():
    dic=json.loads(line)
    data.append(dic)
#print(data)
# 输出符合html格式的输出，source: target: rela: type:
for item in data:
    print("{id:'",item['id'],"',name:'",item['properties']['name'],"'}",sep='')