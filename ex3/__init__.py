import re

def to_region(segmentation: str) -> list:
    region = []
    start = 0
    for word in re.split(' ',segmentation):
        end = start + len(word)
        region.append((start, end))
        start = end
        #print(word)
        #print((start,end))
    return region


def prf(gold: str, pred: str):
    """
     计算P、R、F1
     :param gold: 标准答案文件
     :param pred: 分词结果文件
     :return: (P, R, F1)
    """
    A_size, B_size, A_cap_B_size = 0, 0, 0
    A, B = to_region(gold), to_region(pred)

    #print(set(A)^set(B))
    A_size += len(A)
    B_size += len(B)
    A_cap_B_size += len(set(A)&set(B))

    p, r = A_cap_B_size / B_size * 100, A_cap_B_size / A_size * 100
    return p, r, 2 * p * r / (p + r)


if __name__ == '__main__':
    gold = open("D:/KG/pku.txt", encoding='UTF-8').read()
    result = open('D:/KG/fenci/pyn_result.txt',  encoding='UTF-8').read()
    gold = re.sub(r'[\W]', ' ', gold)
    pred = re.sub(r'[\W]', ' ', result)
    #print(pred)
    #print(len(gold))
    print("Precision:%.2f Recall:%.2f F1:%.2f " % prf(gold, pred))