from CONST import *
import numpy as np
import copy
import util

class DecisionNode:

    def __init__(self, data, cur_attribute, target_column, name, choosed, parent = None):
        self.name = name
        self.pos = 0
        self.neg = 0
        self.data = data
        self.target_column = target_column
        self.target_concept = data[:,target_column]
        # changed by Van Duy Vinh----------------------------------
        self.choosed = choosed
        # changed by Van Duy Vinh----------------------------------
        self.cur_attribute = cur_attribute
        self.children = []
        self.parent = parent
        self.calculate_pos_neg()
        self.create_children()
        self.label = self.name


    def draw_graph(self, G):
        G.add_node(self.name)
        G.node[self.name]['pos'] = self.pos
        G.node[self.name]['neg'] = self.neg
        if (self.parent!= None):
            G.add_edge(self.parent.name, self.name)
        for child in self.children:
            child.draw_graph(G)

    def get_labels(self):
        label_dict = {}
        label_dict[self.name] = self.label
        for child in self.children:
            label_dict.update({child.name:child.label})
        return label_dict



    def calculate_pos_neg(self):
        pos = (self.target_concept == POSITIVE_TARGET).sum()
        neg = len(self.target_concept) - pos
        self.pos = pos
        self.neg = neg

    def print_node(self, indent):
        indent_string = ' '
        for i in range(0, indent):
            indent_string+= ' '
        string_print = indent_string+ str(self.label)+' +'+str(self.pos)+' -'+str(self.neg)
        print (string_print)
        for child in self.children:
            child.print_node(indent+3)

    def parent_info(self):
        if (self.parent==None):
            return "NONE"
        else:
            p = self.parent
            return p.label+' +'+str(p.pos)+' -'+str(p.neg)

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
            # changed by Van Duy Vinh----------------------------------
            v_order = util.get_attribute_order(child_data, self.target_column, self.choosed)
            choosed = copy.deepcopy(self.choosed)
            choosed[v_order[0]] = True
            child = DecisionNode(child_data, v_order[0], self.target_column, v, choosed, self)
            # changed by Van Duy Vinh----------------------------------
            self.children.append(child)

