#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

data = []
for line in fileinput.input():
	if line[0] == '#': continue		 	
	data.append(float(line))
	
data.sort()
count = len(data)
min = data[0]
max = data[-1]

sum = 0
for i in data:
	sum += i
	mean = sum / count

d = 0	
for j in data:
	d += (j - mean) ** 2
	std_dev = sqrt(d / count)
	
middle = ((count + 1) / 2) - 1
if middle == int(middle): 		# ?
	median = data[int(middle)]
else: 
	mid1 = int(middle - 0.5)
	mid2 = int(middle + 0.5)
	median = (data[mid1] + data[mid2]) / 2		


# output
print(f'Count: {count}')
print(f'Minimum: {min}')
print(f'Maximum: {max}')
print(f'Mean: {mean}')
print(f'Std. dev: {std_dev:.3f}')
print(f'Median: {median}')

"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
