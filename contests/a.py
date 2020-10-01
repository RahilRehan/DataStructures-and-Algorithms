t = int(input())
while t:
    a, b, r = list(map(int, input().split()))
    s = 0
    c = 0
    ans = 0
    while s < r or c < r:
        if s < r:
            s = s * a
            ans += 1
            continue
        if c < r:
            s = s-b
            c += 1
            ans += 1
    print(ans)
    t -= 1
