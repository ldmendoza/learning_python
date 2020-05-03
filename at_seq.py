#!/usr/bin/env python3

import random
#random.seed(1)  comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

seq = ''
length = 30
at_frac = 0.6
at_count = 0

for nt in range(length):
	r = random.random()
	if r < at_frac:
		at_count += 1
		r = random.random()
		if r < 0.5: seq += 'A'
		else:		seq += 'T'
	else:
		r = random.random()
		if r < 0.5: seq += 'C'
		else:		seq += 'G'
		
print(length, at_count/length, seq)

"""
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
