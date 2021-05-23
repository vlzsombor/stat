import csv
import numpy as np
import codecs



# csvReader = csv.reader(codecs.open('commaMerged2.csv', 'rU', 'utf-16'))


with open('mergedSorted.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = list(csv_reader)

arr = np.array(data)
print(arr[:,0])

subArr = arr[0:1000]
print(np.corrcoef(subArr[:,2:6].astype(np.int).mean(axis=1),subArr[:,6:10].astype(np.int).mean(axis=1)))