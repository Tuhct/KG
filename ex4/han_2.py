from pyhanlp import HanLP

def extract_chinese_name(string: str) -> list:
    """使用HanLP人名识别"""
    if (string is None) or (string == ""):
        return []
    segment = HanLP.newSegment().enableNameRecognize(True)
    user_list = []
    for i in segment.seg(string):
        split_words = str(i).split('/')  # check //m
        word, tag = split_words[0], split_words[-1]
        if tag == 'nr':
            user_list.append(word)
    return user_list

txt = open("E:/KG/实验三数据集/红楼梦.txt","r",encoding="utf-8").read()
user_list=extract_chinese_name(txt)
a={}
for i in user_list:
    if user_list.count(i)>1:
        # 单个词语不计算在内
        a[i]=user_list.count(i)
        # 遍历所有词语，每出现一次其对应的值加 1

a1=sorted(a.items(),key=lambda x: x[1],reverse=True)
# 根据词语出现的次数进行从大到小排序
fi = open("D:/KG/renwu/han人物角色提取.txt","w",encoding="utf-8")
for i in range(len(a1)):
    fi.write(str(a1[i][0])+',')
    fi.write(str(a1[i][0])+'\n')
fi.close()


'''txt = open("E:/KG/实验三数据集/红楼梦.txt","r",encoding="utf-8").read()
user_list = extract_chinese_name(txt)
a=Counter(user_list)
#print(a)

if __name__ == '__main__':
    txt = open("E:/KG/实验三数据集/红楼梦.txt", "r", encoding="utf-8").read()
    user_list = extract_chinese_name(txt)
    #for word in user_list:
    #    if len(word.word) == 1:  # 单个词语不计算在内
    #        continue
    #    else:
    #        counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1

#        items = list(counts.items())
 #       items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序
  #      fi = open("D:/KG/renwu/han人物角色提取.txt", "w", encoding="utf-8")
   #     for i in range(len(items)):
    #        word, pos = items[i][0]
     #       count = items[i][1]
      #      a = word + "," + str(count)
       #     fi.write(a + "\n")

        #fi.close()'''
