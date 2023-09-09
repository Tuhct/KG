import glob
from itertools import islice
inputfile_dir = ''
outputfile = 'E:/KG/neo4j-community-3.5.5/import/datas/tp/entity.csv'

path =r'E:/KG/neo4j-community-3.5.5/import/datas/tp/entity'# use your path
csv_list = glob.glob(path+'/*.csv')
print(u'共发现%s个CSV文件'%len(csv_list))
print(u'正在处理............')
for i in csv_list: #循环读取同文件夹下的csv文件
    fr = open(i,'rb').read()
    with open(outputfile,'ab') as f: #将结果保存为rel.csv
         f.write(fr)
print(u'合并完毕！')



