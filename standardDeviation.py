import math
import csv
from re import X
with open('data.csv', newline = '') as f:
    r = csv.reader(f)
    fileData = list(r)
print(fileData)
data = fileData[0]
print(data)
def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total = total + int(i)
    mean = total / n
    return mean
dataList = []
for num in data:
    a = int(num) - mean(data)
    a = a ** 2
    dataList.append(a)
sum = 0
for i in dataList:
    sum = sum + i
result = sum / len(data) - 1
standardDeviation = math.sqrt(result)
print(standardDeviation)