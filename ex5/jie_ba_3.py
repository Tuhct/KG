import jieba
import jieba.posseg as psg

txt = open("E:/KG/实验三数据集/红楼梦.txt","r",encoding="utf-8").read()
words= psg.cut(txt) # 使用精确模式对文本进行分词
counts={} #通过键值对的形式存储词语及其出现的次数

for word in words:
    if len(word.word) == 1: # 单个词语不计算在内
        continue
    else:
        if word.flag =="nr":# 仅统计词性为nr的词语
            counts[word] = counts.get(word,0) + 1# 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())
items.sort(key=lambda x: x[1],reverse=True) # 根据词语出现的次数进行从大到小排序
fi = open("D:/KG/renwu/红楼人物角色.txt","w",encoding="utf-8")
for i in range(len(items)):
    word,pos = items[i][0]
    a = word
    fi.write(a +"\n")

fi.close()