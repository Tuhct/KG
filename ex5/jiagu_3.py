import jiagu

# 吻别是由张学友演唱的一首歌曲。
# 《盗墓笔记》是2014年欢瑞世纪影视传媒股份有限公司出品的一部网络季播剧，改编自南派三叔所著的同名小说，由郑保瑞和罗永昌联合导演，李易峰、杨洋、唐嫣、刘天佐、张智尧、魏巍等主演。

text = open("E:\KG\实验三数据集\红楼1.txt","r",encoding="utf-8").read()
knowledge = jiagu.knowledge(text)
print(knowledge)

