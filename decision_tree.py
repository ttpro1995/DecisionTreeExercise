import util
import numpy as np
import copy

DAY = 0
OUTLOOK = 1
TEMP = 2
HUMIDITY = 3
WIND = 4
TENNIS = 5
POSITIVE_TARGET = 'YES'



class DecisionTree:
    def __init__(self, target_column):
        data = util.read_csv('data.csv')
        data = np.array(data)
        self.target_column = target_column
        self.data = data

    def get_attribute_order(self):
        # calculate information gain to choose the order
        aspect_gain_list = []
        for i in range(1, self.target_column):
            aspect_gain = self.calculate_information_gain(i)
            aspect_gain_list.append(aspect_gain)
        aspect_gain_sort = copy.deepcopy(aspect_gain_list)
        aspect_gain_sort.sort()
        order = []
        for gain in aspect_gain_sort:
            idx = aspect_gain_list.index(gain)
            order.append(idx)
        return order


    def calculate_entropy(self, column_of_a = None):
        # calculate E(s)
        # s = day/outlook/temp/humidity/wind
        target_concept = self.data[:,self.target_column]
        if column_of_a == None:
            t = (target_concept == POSITIVE_TARGET).sum()
            f = len(target_concept) - t
            return util.entropy(t,f)

        data = self.data[:, column_of_a]

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
            e = util.entropy(t,f)
            entropy_v_list.append(e)
        return v_list, entropy_v_list


    def calculate_information_gain(self, column_of_a):
        data = self.data[:, column_of_a]
        es = self.calculate_entropy()
        v_list, entropy_v_list = self.calculate_entropy(column_of_a)
        sum_of_part2 = 0
        for idx, v in enumerate(v_list):
            sv = (data == v).sum()
            s = len(data)
            esv = entropy_v_list[idx]
            sum_of_part2+= (float(sv)/s)*esv
        gain = es - sum_of_part2
        return gain


