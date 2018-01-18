__author__ = 'Vitaly'
dna = "GATGATTTTTTTTA"


def reverse_string(seq):
    return seq[::-1]


print(reverse_string(dna))


def complement(dna):
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N':'N', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a', 'n': 'n'}
    letters = list(dna)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)
print(complement(dna))