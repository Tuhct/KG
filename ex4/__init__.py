#需要导入Counter方法
from collections import Counter
txt = open("D:/KG/renwu/thu人物角色提取2.txt", "r", encoding="utf-8").read()
t=txt.split(',')
c={}
for i in t:
	#List.count(i)统计列表元素对应的个数
	if t.count(i) > 1:
	    c[i] = t.count(i)
c=sorted(c.items(),key=lambda  x:x[1],reverse=True)
print(c)
fi = open("D:/KG/renwu/thu人物角色提取.txt","w",encoding="utf-8")
for i in range(len(c)):
    fi.write(str(c[i][0])+',')
    fi.write(str(c[i][1])+'\n')
fi.close()


