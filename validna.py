__author__ = 'Vitaly'
dna = 'atgccaaj'
def valid_dna(dna):
    for c in dna:
        if not c in 'acgtACGT':
            print(c)
            return 'False'
    print(c)
    return 'True'

print(valid_dna(dna))