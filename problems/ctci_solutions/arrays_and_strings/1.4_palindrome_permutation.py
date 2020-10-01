#Given a string, determine if a permutation of the string could form a palindrome.

# Example 1:

# Input: "code"
# Output: false
# Example 2:

# Input: "aab"
# Output: true
# Example 3:

# Input: "carerac"
# Output: true

from collections import Counter
def pal_per(st):
    cnt = Counter(st)
    even_count = 0
    odd_count = 0
    ones = 0
    for key in cnt:
        if cnt[key]==1:
            if(len(st)%2==0): return False
        if cnt[key]%2==1:
            if(len(st)%2==0): return False
    return True


def nick_whites_way(st):
    char_set = [0]*128
    for ele in st:
        char_set[ord(ele)-ord('a')]+=1
    counts = 0
    for ele in char_set:
        counts += ele%2
    return counts <=1

print(pal_per("never odd or even"))
print(nick_whites_way("never odd or even"))
