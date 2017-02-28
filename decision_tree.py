# Thai Thien
# 1351040
import util
import numpy as np
from decision_node import DecisionNode
from CONST import *
import networkx as nx



class DecisionTree:
    def __init__(self, target_column):
        data = util.read_csv('data.csv')
        data = np.array(data)
        self.target_column = target_column
        self.data = data
        self.tree = None
        self.G = nx.Graph()

    def build_tree(self):
        choosed = [False] * len(self.data[0, :])
        choosed[0] = True
        choosed[self.target_column] = True
        order = util.get_attribute_order(self.data, self.target_column, choosed)
        choosed[order[0]] = True
        root = DecisionNode(self.data, order[0], self.target_column,'ROOT', choosed)
        self.tree = root
        return self.tree

    def draw_tree(self):
        self.tree.draw_graph(self.G)
        label_dict = self.tree.get_labels()
        return self.G

    def print_tree(self):
        self.tree.print_node(0)



