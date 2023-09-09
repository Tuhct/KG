import jiagu

'''txt = open("E:\KG\实验三数据集\红楼1.txt","r",encoding="utf-8").read()
s = jiagu.seg(txt)

print(s)
'''
import jiagu

#jiagu.init() # 可手动初始化，也可以动态初始化

text = open("E:\KG\实验三数据集\红楼1.txt","r",encoding="utf-8").read()

words = jiagu.seg(text) # 分词
#print(words)
pos=jiagu.pos(words)
#print(pos)
a=[]
for i in range(len(words)):
    a.append((words[i],pos[i]))
print(a)
