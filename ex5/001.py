import jieba
import gensim
from gensim.models import word2vec
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
lines=open("E:\KG\实验三数据集\红楼梦.txt",encoding = 'utf-8')
#加载停用词 一定要加.strip() 这个地方改了好久 一直停用词去不掉，输出后才发现带着\n
stop_word=[]
with open('D:/KG/renwu/hit_stopwords.txt', 'r',encoding = 'utf-8') as f:
     for line in f.readlines():  # 按行读文件
        stop_word.append(line.strip())

jieba.load_userdict("D:/KG/renwu/红楼人物角色.txt")
#将分词结果存储到list内
l_=[]
for line in lines:
    #print(line)
    l=jieba.cut(line.replace("/n","").replace("/r","").replace("\u3000","").replace("”","").replace("“",""))
    for i in l:
        if i not in stop_word:
            l_.append(i)
#word2vec需要词以及空格隔开的形式～
s=''
for i in l_:
    s+=(" "+i)
#保存下来
fh = open('001.txt', 'w+', encoding='utf-8')
fh.write(s)
fh.close()
sentences=LineSentence('001.txt')
model=Word2Vec(sentences)

#看两个实体之间的相似度
name1="宝玉"
name2="黛玉"
try:
    sim1 = model.similarity(name1, name2)
    print('{0} 和 {1} 的相似度为：{2}\n'.format(name1,name2,sim1))
except:
    print('{0} 或 {1} 可能不存在～：\n'.format(name1,name2))

#看某实体最相似的n个实体
name='晴雯'
n = 8
try:
    for key in model.wv.similar_by_word(name):
        if len(key[0]) == 3:
            n -= 1
            print(key[0], key[1])
            if n == 0:
                break
except:
    print(u'没有在文章中找到 {0} ：\n'.format(name))

#看某实体的相似列表
name='贾母'
try:

    sim3 = model.wv.most_similar(name, topn=20)
    print(u'和 {0} 与相关的词有：\n'.format(name))
    for key in sim3:
        print(key[0], key[1])
except:
    print(u'没有在文章中找到 {0} ：\n'.format(name))
#保存模型
save_path="红楼人物关系.model"
model.save(save_path)
#加载模型
model2 = word2vec.Word2Vec.load(save_path)
#加载模型后的测试
name="刘姥姥"
sim3 = model2.wv.most_similar(name, topn=20)
print(u'和 {0} 与相关的词有：\n'.format(name))
for key in sim3:
    print(key[0], key[1])