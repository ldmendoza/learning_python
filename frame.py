#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

for p in range(0, len(dna), 3):
	for f in range(0, 3):
		print(p+f, f, dna[p+f])	
print('-')

for i in range(len(dna)):
	print(i, i%3, dna[i])

"""
for c in dna:
	for j in range(3):
		print(j, c)
print('--')


i = 0
for f in range(3):
	print(i, f, dna[i])
	i += 1
print('---')


# from practice in class
for i in range(len(aa)):
	for j in range(i + 1, len(aa)):
		print(i, j, aa[i], aa[j])





0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
