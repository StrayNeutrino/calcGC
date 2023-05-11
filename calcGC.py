# -*- coding: utf-8 -*-
"""
Programming Project: GC Analysis of FASTA files
by Christina Burris


This is a simple script to calculate GC percentage from a fasta file. I 
used three fasta files for testing: the complete genome of Carsonella 
ruddii (sample.fna), chromosome 1 of Arabidopsis thaliana, and chromosome 1 
of Helianthus annuus. It currently only works on files containing one 
record. 
  
"""
# Load the Biopython module Bio.SeqIO into the namespace.
# Bio.SeqIO allows sequences to be read and written as SeqRecord objects.
# A SeqRecord object is a Seq (sequence) object with ID, name, etc...

from Bio import SeqIO

# Change the file name to read a different file. File should be in
# current directory. Sample.fna (Carsonella ruddii) is included with script 
# because it is the smallest.
# NOTE: Carsonella ruddii has an extremely low GC content. This is not 
# an error.

record = SeqIO.read("sample.fna", "fasta")

# GC% = # of G + # of C / Total # of nucleotide bases

percent = ((100 * (float(record.seq.count("G")) + float(record.seq.count("C")))) / len(record))

#Round to desired degree of precision.

print (round(percent),"%")