import csv
import numpy as np
import matplotlib.pyplot as plt


featureNumber = 66.000

# csvReader = csv.reader(codecs.open('commaMerged2.csv', 'rU', 'utf-16'))

with open('mergedSorted.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = list(csv_reader)

arr = np.array(data)

if(featureNumber == 0):
    featureNumber = len(arr)

subArr = arr[0:featureNumber]
ax1 = subArr[:,2:6].astype(np.int).mean(axis=1)
ax2 = subArr[:,6:10].astype(np.int).mean(axis=1)

print(np.corrcoef(ax1,ax2))





x = np.linspace(0, 1, featureNumber)

plt.plot(x, ax1, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, ax2, label='quadratic')  # etc.

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()