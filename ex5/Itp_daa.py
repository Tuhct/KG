from ltp import LTP

def ltp_data():
    """将句子处理成语义依存图"""

    ltp = LTP()
    # 分句
    txt = open("E:\KG\实验三数据集\红楼梦.txt", encoding='UTF-8')
    lines = txt.readlines()
    for line in lines:
        line = line.strip("\n")
        line = line.split(" ")
        line = [float(x) for x in line]
    sents = ltp.sent_split(line)
    # 分词
    seg, hidden = ltp.seg(sents)
    # 词性标注
    pos = ltp.pos(hidden)
    # 词性标注
    ner = ltp.ner(hidden)
    # 语义角色标注
    srl = ltp.srl(hidden)
    # 依存句法分析
    dep = ltp.dep(hidden)
    # 语义依存分析（图）
    sdp = ltp.sdp(hidden, mode='graph')

    return dep, pos, seg


if __name__ == '__main__':
    ds, pos, seg = ltp_data()
    print("语义依存关系：{k}".format(k = ds))
    print("标签：{k}".format(k = pos))
    print("分句：{k}".format(k = seg))
