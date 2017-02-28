# Thai Thien
# 1351040
# with some contribution from Van Duy Vinh

import util
from decision_tree import DecisionTree

data = util.read_csv('data.csv')


if __name__ == "__main__":
    tree = DecisionTree(5)
    root = tree.build_tree()
    tree.print_tree()
