from gensim.models import word2vec

sentences = word2vec.LineSentence('D:/KG/fenci/jie红楼_result.txt')
model = word2vec.Word2Vec(sentences)
model.save("test_1.model")
model.wv.save_word2vec_format('test_1.model.txt', binary=False)
print('Nearest 宝玉: ', model.wv.most_similar('宝玉'))
