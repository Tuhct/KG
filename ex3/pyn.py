import pynlpir
import time

pynlpir.open()
txt = open("E:\KG\实验三数据集\红楼梦.txt", encoding='UTF-8').read()
result=open('D:/KG/fenci/pyn红楼_result.txt','w',encoding='UTF-8')

start = time.perf_counter()
words=pynlpir.segment(txt,pos_tagging=False)
end = time.perf_counter()
print("运行耗时", end-start)
pynlpir.close()

result.write(' '.join(words))
result.close()