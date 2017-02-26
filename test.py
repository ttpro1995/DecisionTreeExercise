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

def test_gain():
    tree = DecisionTree(5)
    g_wind = tree.calculate_information_gain(4)
    print (g_wind)

def test_order():
    tree = DecisionTree(5)
    order = tree.get_attribute_order()
    print (order)

test_calculate_entropy()
test_gain()
test_order()