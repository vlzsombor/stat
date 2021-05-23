import csv
import codecs
import numpy as np


with open('gyorsabb2299.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    data = list(csv_reader)




arr = np.array(data,dtype=np.str)

print(arr[:,2:6].astype(np.int).mean(axis=1))
print(arr[:,6:10].astype(np.int).mean(axis=1))

print(np.corrcoef(arr[:,2:6].astype(np.int).mean(axis=1),arr[:,6:10].astype(np.int).mean(axis=1)))