#!/usr/bin/env python3

import argparse
import biotools
import re
import math

# Develop a program that finds likely cases of horizontal gene transfer. 
	# Genes transferred from a diff genome may have very diff codon usage bias.
	# Program reads FASTA files of coding sequences
	# Compare codon usage by Kullback-Leibler distance
	# There should be a command line option for pseudocounts
	# Reports all genes and their distance (for sorting and filtering later)

# comparing two dictionaries to each other 

parser = argparse.ArgumentParser(
	description='Horiztonal gene transfer detector.')
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='FASTA file')
parser.add_argument('--pseudo', required=False, type=float, default=1.0,
	metavar='<float>', help='pseudocount [%(default)f]')
arg = parser.parse_args()


def kld(p, q):
	d = 0
	for i in p:
		d += p[i] * math.log2(p[i]/q[i])
	return d

# step 1: make a global table
counts = {}
freq = {}
total = 0
for name, seq in biotools.read_fasta(arg.file):
	for i in range(0, len(seq) - 2, 3):
		codon = seq[i:i+3]
		if codon in counts: counts[codon] += 1
		else:               counts[codon]  = 1
	total += len(seq)/3

for codon in counts:
	freq[codon] = counts[codon]/total

# step 2: compare indiv tables to global table
for name, seq in biotools.read_fasta(arg.file):
	g_counts = {}
	g_total = 0
	for codon in freq:
		g_counts[codon] = arg.pseudo
		g_total += arg.pseudo
	g_freq = {}
	g_total += len(seq)/3
	for i in range(0, len(seq) - 2, 3):
		codon = seq[i:i+3]
		g_counts[codon] += 1
	for codon in g_counts:
		g_freq[codon] = g_counts[codon]/g_total
	# get locus name and kld
	match = re.search('locus_tag=(\w+)', name)
	locus = match[1]
	print(locus, kld(freq, g_freq))