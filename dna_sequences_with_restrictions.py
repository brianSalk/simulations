# A DNA sequence consists of some combination of zero or more of each A,T,C, and G.
# each A,T,C, or G represents a nucleotide
# Given that we know the following about a newly discovered species:
# -- there cannot be more than five adjacent A's in a single gene
# -- there must be at least one G
# -- there must be at least two T's
# how many genes of length 7 nucleotides can there be in this species?
import random
from statistics import mean
from itertools import combinations_with_replacement, permutations

def has_sublist(sublist, ls):
    """ starting at each index in ls, check if sublist exists """
    for i in range(len(ls)):
        if ls[i:-1] == sublist:
            return True
    return False

if __name__ == "__main__":
    ans = set()
    for comb in combinations_with_replacement(('A','T','C','G'), 7):
        for perm in permutations(comb):
            if ('G' in perm and perm.count('T') > 1) and not has_sublist(('A','A','A','A','A'), perm):
                ans.add(perm)
    print(len(ans))