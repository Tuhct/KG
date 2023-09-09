from py2neo import Node, Graph, Relationship
from ltp_data import ltp_data


class DataToNeo4j(object):
    """将excel中数据存入neo4j"""

    def __init__(self):
        """建立连接"""
        link = Graph("localhost", username="root", password="123456")
        self.graph = link
        # self.graph = NodeMatcher(link)
        self.graph.delete_all()


    def create_node(self, name_node, type_node):
        """建立节点"""
        nodes = []
        for name_sentence, type_sentence in zip(name_node, type_node):
            nodes_sentence = []
            for name_word, type_word in zip(name_sentence, type_sentence):
                # 创建节点
                node = Node(type_word, name = name_word)
                self.graph.create(node)
                # 保存下来
                nodes_sentence.append(node)
            nodes.append(nodes_sentence)

        print('节点建立成功')
        return nodes


    def create_relation(self, rel):
        """建立联系"""
        for sentence in rel:
            for word in sentence:
                try:
                    # 关系要转化成字符串格式
                    r = Relationship(word[0], str(word[2]), word[1])
                    self.graph.create(r)
                except AttributeError as e:
                    print(e)

        print('关系建立成功')


def node_extraction(seg, pos):
    """从语义依存图中提取出节点的名字和节点类型"""
    for i in range(len(seg)):
        seg[i] = [str(i) for i in seg[i]]
        pos[i] = [str(i) for i in pos[i]]

    return seg, pos


def relation_extraction(ds,nodes):
    pass
    """
    提取出节点间的关系，将节点与关于整合成三元组，并存放在列表中。
    （node1,node2,relation)
    """
    rel = []
    for ds_sentence, nodes_sentence in zip(ds, nodes):
        rel_sentence = []
        for ds_word, nodes_word in zip(ds_sentence, nodes_sentence):
            # 根据索引提取出节点和关系
            index1 = int(ds_word[0]) - 1
            index2 = int(ds_word[1]) - 1
            node1 = nodes_sentence[index1]
            node2 = nodes_sentence[index2]
            relation = ds_word[2]

            # 将节点和关系添加到3元组中
            rel_word = []
            rel_word.append(node1)
            rel_word.append(node2)
            rel_word.append(relation)

            # 将3元组整合到句子中
            rel_sentence.append(rel_word)

            # 将单句整合到列表中
        rel.append(rel_sentence)

    return rel


if __name__ == '__main__':
    ds, pos, seg = ltp_data()
    create_data = DataToNeo4j()

    # 建立节点
    node_name, node_type = node_extraction(seg, pos)
    nodes = create_data.create_node(node_name, node_type)
    print("第一句话的节点：\n{k}".format(k = nodes[0]))

    # 建立联系
    rel = relation_extraction(ds, nodes)
    create_data.create_relation(rel)
    print("第一句话的关系：\n{k}".format(k = rel[0]))
