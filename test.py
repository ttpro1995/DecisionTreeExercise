import util
from decision_tree import DecisionTree

data = util.read_csv('data.csv')
def test_calculate_entropy():
    tree = DecisionTree(5)
    a, b = tree.calculate_entropy(1)
    c, d = tree.calculate_entropy(2)
    print (a,b)
    print (c,d)
    print (tree.calculate_entropy())

test_calculate_entropy()