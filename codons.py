#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for nt in range(0, len(dna), 3):
	codon = dna[nt:nt+3]
	print(codon)

"""
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
