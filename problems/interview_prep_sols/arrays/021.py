def setZeroes(mat):
    n = len(mat)
    m = len(mat[0])
    rows = [0]*n
    cols = [0]*m

    for i in range(n):
        for j in range(m):
            if(mat[i][j] == 0):
                rows[i] = 1
                cols[j] = 1
    for idx in range(len(rows)):
        if rows[idx]==1:
            for k in range(0,m):
                mat[idx][k] = 0
    for idx in range(len(cols)):
        if cols[idx]==1:
            for k in range(0,n):
                mat[k][idx] = 0