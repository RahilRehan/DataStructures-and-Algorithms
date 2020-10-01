# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string

def urlify(st, length): #O(N) time and as string is immutable in python, we can consider extra space(list passing) is used by input itself.
    big_len = len(st)
    for i in reversed(range(length)):
        if st[i]==" ":
            st[big_len-3:big_len] = '%20'
            big_len-=3
        else:
            st[big_len-1] = st[i]
            big_len-=1
    return st

print("".join(urlify(list('Mr John Smith    '), 13)))
print("".join(urlify(list('much ado about nothing      '), 22)))
