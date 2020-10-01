# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def check_perm_1(st1, st2):  #O(NlogN) time and space depending on the sorting algorithm used.
    if(len(st1)!=len(st2)): return False
    return sorted(st1)==sorted(st2)

from collections import Counter

def check_perm_2(st1, st2): #Considering ASCII, 128 bit counter space used. Hence O(1) time complexity.
    if(len(st1)!=len(st2)): return False
    counter = Counter(st1)
    for ele in st2:
        if counter[ele]==0: return False
        counter[ele] -= 1
    return True

print(check_perm_1('3563476', '7334566')) #True
print(check_perm_1('abcd', 'd2cba')) #False

print(check_perm_2('3563476', '7334566')) #True
print(check_perm_2('abcd', 'd2cba')) #False
