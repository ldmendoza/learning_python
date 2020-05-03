#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = - sum(pi * log2(pi))
# Use fileinput to get the data from nucleotides.txt
# Make sure that the values are probabilities
# Make sure that the distribution sums to 1
# Report with 3 decimal figures

import fileinput
import math

p = []
sum = 0
for line in fileinput.input():
	if line[0] == '#': continue
	cols = line.split()
	v = float(cols[1])
	assert(v >= 0 and v <= 1)
	sum += v
	p.append(v)
assert(math.isclose(sum, 1))

h = 0
for i in range(len(p)):
	h -= p[i] * math.log2(p[i])
print(f'{h:.3f}')

"""
python3 entropy.py nucleotides.txt
1.846
"""
