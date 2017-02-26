import numpy as np
import csv

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
