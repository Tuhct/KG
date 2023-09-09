'''import re
s= open("D:/KG/pku.txt", encoding='UTF-8').read()
a = re.sub(r'[\W]', ' ', s)
print(a)
'''
import re

def to_region(segmentation: str) -> list:
    region = []
    start = 0
    for word in re.split(' ', segmentation):
        end = start + len(word)
        region.append((start, end))
        start = end
        print(word)
        print((start, end))
    return region


f = open('D:/KG/fenci/a.txt',  encoding='UTF-8').read()
b = open('D:/KG/fenci/b.txt',  'w',encoding='UTF-8')
for i in f:
    i=i.replace('\n','')
    b.write(i)
b.close()
c = open('D:/KG/fenci/b.txt',  encoding='UTF-8').read()

print(c)

to_region(c)
