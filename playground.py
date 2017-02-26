import csv


# -*- coding: utf-8 -*-
import csv


# Read CSV file
with open('data.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]

print ('breakpoint')