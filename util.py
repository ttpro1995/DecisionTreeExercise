import numpy as np
import csv
import networkx as nx
import copy
from CONST import *
def entropy(true_instance, false_instance):
    p_true = float(true_instance)/ (true_instance+false_instance)
    p_false = float(false_instance)/(true_instance + false_instance)
    if (p_false == 0) or (p_true == 0):
        return 0
    e = -(p_true)*((np.log2(p_true))) \
    - (p_false)*((np.log2(p_false)))

    return (e)

def read_csv(file_name):
    with open('data.csv', 'r') as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        # next(reader, None)  # skip the headers
        data_read = [row for row in reader]

    return data_read



def hierarchy_pos(G, root = 'ROOT', width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5,
                  pos = None, parent = None):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node of current branch
       width: horizontal space allocated for this branch - avoids overlap with other branches
       vert_gap: gap between levels of hierarchy
       vert_loc: vertical location of root
       xcenter: horizontal location of root
       pos: a dict saying where all nodes go if they have been assigned
       parent: parent of this branch.'''
    if pos == None:
        pos = {root:(xcenter,vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    neighbors = G.neighbors(root)
    if parent != None:
        neighbors.remove(parent)
    if len(neighbors)!=0:
        dx = width/len(neighbors)
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos = hierarchy_pos(G,neighbor, width = dx, vert_gap = vert_gap,
                                vert_loc = vert_loc-vert_gap, xcenter=nextx, pos=pos,
                                parent = root)
    return pos

# changed by Van Duy Vinh----------------------------------
def get_attribute_order(data, target_column, choosed):
    # calculate information gain to choose the order
    aspect_gain_list = []
    idx = []
    for i in range(len(choosed)):
        if choosed[i] == False:
            idx.append(i)

    for i in idx:
        aspect_gain = calculate_information_gain(data, target_column, i)
        aspect_gain_list.append(aspect_gain)

    aspect_gain_sort = copy.deepcopy(aspect_gain_list)
    aspect_gain_sort.sort(reverse=True)
    order = []
    for gain in aspect_gain_sort:
        h = idx[aspect_gain_list.index(gain)]
        order.append(h)
    return order


def calculate_entropy(data, target_column, column_of_a = None):
    # calculate E(s)
    # s = day/outlook/temp/humidity/wind
    target_concept = data[:,target_column]
    if column_of_a == None:
        t = (target_concept == POSITIVE_TARGET).sum()
        f = len(target_concept) - t
        return entropy(t,f)

    data = data[:, column_of_a]

    v_list = np.unique(data)
    entropy_v_list = []
    for v in v_list:
        # v is value of a
        idx_v = np.where(data==v)
        idx_v = idx_v[0]
        t = 0
        for idx in idx_v:
            if (target_concept[idx] == POSITIVE_TARGET):
                t+=1
        f = len(idx_v) - t
        e = entropy(t,f)
        entropy_v_list.append(e)
    return v_list, entropy_v_list


def calculate_information_gain(data, target_column, column_of_a):
    data_a = data[:, column_of_a]
    es = calculate_entropy(data, target_column)
    v_list, entropy_v_list = calculate_entropy(data, target_column, column_of_a)
    sum_of_part2 = 0
    for idx, v in enumerate(v_list):
        sv = (data_a == v).sum()
        s = len(data_a)
        esv = entropy_v_list[idx]
        sum_of_part2+= (float(sv)/s)*esv
    gain = es - sum_of_part2
    return gain
# changed by Van Duy Vinh----------------------------------