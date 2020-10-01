# Check if the given two strings are rotation of each other, given a function isSubstring, you can make only one call to it.

# Logic -> consider two parts of string s1. s1= xy and s2 is yx.
# Then it is sure that s2 i.e yx is definetly part of s1s1 xyxy

def check_rotation(s1, s2):  #Time complexity, O(N) i.e (A+B). Depends on how isSubstring is implemented.
    if(len(s1)==len(s2) and len(s1)>0):
        s1s1 = s1+s1
        return isSubstring(s1s1, s2)
    return False

def isSubstring(s1, s2):
    if s2 in s1:
        return True
    return False

print(check_rotation("waterbottle", "erbottlewat"))
