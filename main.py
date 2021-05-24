import csv
import numpy as np
import matplotlib.pyplot as plt


featureNumber = 0

# csvReader = csv.reader(codecs.open('commaMerged2.csv', 'rU', 'utf-16'))

with open('mergedSorted.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = list(csv_reader)

arr = np.array(data)

if(featureNumber == 0):
    featureNumber = len(arr)

subArr = arr[0:featureNumber]
A1 = subArr[:,2:6].astype(np.int).mean(axis=1)
A2 = subArr[:,6:10].astype(np.int).mean(axis=1)

# print(np.corrcoef(A1,A2))


A = subArr[:,2:10].astype(np.float).mean(axis=1)
B = subArr[:,10].astype(np.float)

# print(np.corrcoef(A,B))

# print(np.std(A,axis=0))


r1 = np.mean(A)
print("\nMean: ", r1)
  
r2 = np.std(A2)
print("\nstd: ", r2)
  
r3 = np.var(A)
print("\nvariance: ", r3)


# x = np.linspace(0, 1, featureNumber)

# plt.plot(x, A, label='linear')  # Plot some data on the (implicit) axes.
# plt.plot(x, B, label='quadratic')  # etc.

# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
# plt.show()