import pyhanlp
import time

txt = open("D:/KG/test_pku.txt", encoding='UTF-8').read()
result=open('D:/KG/fenci/han_result.txt','w',encoding='UTF-8')
words=[]

start = time.perf_counter()
for term in pyhanlp.HanLP.segment(txt):
    words.append(term.word)


end = time.perf_counter()
print("运行耗时", end-start)

result.write(' '.join(words))
result.close()