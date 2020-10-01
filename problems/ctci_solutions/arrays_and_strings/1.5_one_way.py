# One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def one_way(s1, s2):
    if(len(s1) == len(s2)):  #only one replacement can take place now
        return one_replacement(s1, s2)
    elif(len(s1)+1 == len(s2)):
        return one_edit(s1, s2)  #check for insertion or removal , pass smaller string as first argument
    elif(len(s1)-1 == len(s2)):
        return one_edit(s2, s1)

def one_replacement(s1, s2):
    found_difference = False
    for idx in range(len(s1)):
        if s1[idx]!=s2[idx]:
            if found_difference:
                return False
            found_difference = True
    return True

def one_edit(s1, s2):
    idx1, idx2 = 0,0
    while(idx1<len(s1) and idx2<len(s2)):
        if(s1[idx1] != s2[idx2]):
            if(idx1 != idx2):
                return False
            idx2+=1
        else:
            idx1+=1
            idx2+=1
    return True



print(one_way("pale","ple"))
print(one_way("pales","pale"))
print(one_way("pale","bale"))
print(one_way("pale","bake"))


