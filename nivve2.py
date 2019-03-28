import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('/home/al204/Documents/nivve1.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x,y, marker='o')

plt.title('Data from the CSV File: children and chocolate')

plt.xlabel('children')
plt.ylabel('chocolate')

plt.show()

