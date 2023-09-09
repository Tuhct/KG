import jiagu
import time


txt = open("D:/KG/test_pku.txt", encoding='UTF-8').read()
result=open('D:/KG/fenci/jiagu_result.txt','w',encoding='UTF-8')

jiagu.init()
start = time.perf_counter()
words=jiagu.seg(txt)
end = time.perf_counter()
print("运行耗时", end-start)

result.write(' '.join(words))
result.close()