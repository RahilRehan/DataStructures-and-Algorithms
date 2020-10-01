

def string_compression(st):  # CTCI solution, O(N) time and O(N) output space
    cnt = 0
    out = ""
    for i in range(len(st)):
        cnt+=1
        if(i+1 >= len(st) or st[i] != st[i+1]):
            out+=(st[i]+str(cnt))
            cnt = 0
    return out if len(out)<len(st) else st

def string_compression_pythonic(st):
    compressed = []
    cnt = 0
    for i in range(len(st)):
        if i!=0 and st[i]!=st[i-1]:
            compressed.append(st[i-1]+str(cnt))
            cnt=0
        cnt+=1
    compressed.append(st[-1]+str(cnt))
    return min(st, ''.join(compressed), key=len)

def string_compression_mine(st):  # This is my solution to the problem, O(N) time space for output string
    if len(st) <= 1: return st
    idx = 1
    out = ""
    cnt = 1
    while(idx < len(st)):
        if st[idx] == st[idx-1]:
            cnt+=1
            idx+=1
        else:
            if cnt > 1:
                out+=(st[idx-1]+str(cnt))
            else:
                out+=(st[idx-1])
            cnt = 1
            idx+=1

    if cnt > 1:
        out+=(st[idx-1]+str(cnt))
    else:
        out+=(st[idx-1])
    return out


#Note that and assume we are using a string builder rather than normal string. A normal string time complexity is about O(N) for appending, and total it would take O(N^2)
# whereas a string builder time complexity is just O(1) for append and total time complexity would be just O(N)


print(string_compression("abcdef"))
print(string_compression_pythonic("aabcccccaaa"))
