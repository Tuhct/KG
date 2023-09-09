import snownlp
import time


txt = open("D:/KG/test_pku.txt", encoding='UTF-8').read()
result=open('D:/KG/fenci/snow_result.txt','w',encoding='UTF-8')

start = time.perf_counter()
words=snownlp.SnowNLP(txt).words
end = time.perf_counter()
print("运行耗时", end-start)

result.write(' '.join(words))
result.close()