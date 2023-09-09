import thulac

thu1 = thulac.thulac(filt=True)   #过滤没有意义的词，词语与词性之间的分隔符设置为’,’
txt = open("E:\KG\实验三数据集\红楼梦.txt","r",encoding="utf-8").read()
text = thu1.cut(txt, text=True)  #进行分词
text=text.split(' ')
#print(text)
a=[]
for i in range(len(text)):
    if text[i]:
            b=text[i].split('_')
    #print(b)
            a.append(b)
fi = open("D:/KG/renwu/thu人物角色提取2.txt", "w", encoding="utf-8")
#print(a)
for i in range(len(a)):
    if a[i][1]=='np':
        #print(a[i][0])
        fi.write(str(a[i][0]) + ',')

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





