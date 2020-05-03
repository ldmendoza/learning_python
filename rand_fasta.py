#!/usr/bin/env python3

import gzip
import sys
import math
import random

# Write a program that creates random fasta files
# Create a function that makes random DNA sequences
# Parameters include length and frequencies for A, C, G, T
# Command line: python3 rand_fasta.py <count> <min> <max> <a> <c> <g> <t>

def rand_dna(lenseq, a, c, g, t):
	seq = []
	for i in range(lenseq):
		r = random.random()
		if	 r < a: 	seq.append('A')
		elif r < a+c:	seq.append('C')
		elif r < a+c+g: seq.append('G')
		else:			seq.append('T')
	return(''.join(seq))

assert(len(sys.argv) == 8)
count = int(sys.argv[1])	# number of seqs generated
min   = int(sys.argv[2])	# min length of each seq
max   = int(sys.argv[3])	# max length of each seq
a	  = float(sys.argv[4])	# freq of nucleotides
c	  = float(sys.argv[5])
g	  = float(sys.argv[6])
t	  = float(sys.argv[7])

assert(count > 0)
assert(min > 0)
assert(max >= max)
assert(a >= 0 and a <= 1)
assert(c >= 0 and c <= 1)
assert(g >= 0 and g <= 1)
assert(t >= 0 and t <= 1)

sum = a + c + g + t
assert(math.isclose(sum, 1))

for i in range(count):
	x = random.randint(min, max)
	dna = rand_dna(x, a, c, g, t)
	print('>seq-%d' % (i))
	print(dna)
	
"""
python3 rand_fasta.py 3 10 20 0.1 0.2 0.3 0.4
>seq-0
TCGTTTTGATTACGG
>seq-1
CGGCTGTTCCGTAATGC
>seq-2
TTTCGTGTACTTTCTAGTGA
"""
