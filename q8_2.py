__author__ = 'Vitaly'
import random
def create_dna(n, alphabet='acgt'):
    return ''.join([random.choice(alphabet) for i in range(n)])
dna = create_dna(1000000)
print(len(dna))
print(dna)
