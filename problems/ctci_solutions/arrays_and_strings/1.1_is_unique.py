#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def is_unique_1(st):  # O(N) time and O(N) space complexity, Hashing
    s = set()
    for ele in st:
        if ele in s:
            return False
        s.add(ele)
    return True

def is_unique_2(st):  # O(N) time and O(1) space complexity, Bit, XOR
    if(len(st) > 128): return True   # Assuming, ASCII
    charset = [False for _ in range(128)]
    for ele in st:
        if(charset[ord(ele)]):
            return False
        charset[ord(ele)] = True
    return True


# Other Solutions
# Pythonic one liner - return False if (len(st)>len(set(st))) else True

#Compare each and every element - O(N^2)

#Sort and compare neighbouring elements - O(NlogN)




print(is_unique_1("rahil"))  #True
print(is_unique_1("rahilrehan"))  #False

print(is_unique_2("rahil"))  #True
print(is_unique_2("rahilrehan"))  #False


