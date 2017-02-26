from CONST import *
import numpy as np

class DecisionNode:
    def __init__(self, data, order, cur_attribute, target_column):
        self.pos = 0
        self.neg = 0
        self.data = data
        self.target_column = target_column
        self.target_concept = data[:,target_column]
        self.order = order
        self.cur_attribute = cur_attribute
        self.children = []
        self.calculate_pos_neg()
        self.create_children()

    def calculate_pos_neg(self):
        pos = (self.target_concept == POSITIVE_TARGET).sum()
        neg = len(self.target_concept) - pos
        self.pos = pos
        self.neg = neg

    def create_children(self):
        if (self.pos == 0) or (self.neg == 0):
            return
        if self.cur_attribute == self.target_column:
            return
        data_column = self.data[:,self.cur_attribute]
        v_list = np.unique(data_column)
        for v in v_list:
            filter = np.asarray([v])
            child_data = self.data[np.in1d(self.data[:, self.cur_attribute], filter)]
            child = DecisionNode(child_data, self.order, self.cur_attribute+1, self.target_column)
            self.children.append(child)
