#O(N*M) time and O(N*M) space
# def zero_matrix(mat):
#     n = len(mat)
#     m = len(mat[0])
#     zero_indices = []
#     for i in range(n):
#         for j in range(m):
#             if(mat[i][j]==0):
#                 zero_indices.append([i,j])
#     for ele in zero_indices:
#         set_zeroes(ele[0], ele[1])

# def set_zeroes(i, j):
#     n = len(mat)
#     m = len(mat[0])
#     for k in range(0, n):
#         mat[i][k] = 0
#     for l in range(0,m):
#         mat[l][j] = 0


# #O(N*M) time and O(M+N) space, best approach
def zero_matrix(mat):
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

# #O(N*M) time and O(1) space, long approach
# def zero_matrix(mat):
#     n = len(mat)
#     m = len(mat[0])
#     rowhasZero = False
#     colhasZero = False

#     #check if first row has zero
#     for i in range(m):
#         if mat[0][i]==0:
#             rowhasZero = True
#             break
#     #check if first col has zero
#     for i in range(n):
#         if mat[i][0]==0:
#             colhasZero = True
#             break

#     #check for rest of the matrix
#     for i in range(1,n):
#         for j in range(1,m):
#             if mat[i][j] == 0:
#                 mat[0][j] = 0
#                 mat[i][0] = 0

#     #nullify matrix based on stored 0 indices in first row and col
#     for idx in range(n):
#         if mat[idx][0] == 0:
#             for i in range(m):
#                 mat[idx][i] = 0
#     for idx in range(m):
#         if mat[0][idx] == 0:
#             for i in range(n):
#                 mat[i][idx] = 0

#     #set first row and cols zero to all corresponding
#     if rowhasZero:
#         for i in range(m):
#             mat[0][i] = 0
#     if colhasZero:
#         for i in range(n):
#             mat[i][0] = 0






mat = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

mata = [
    [1,0,1],
    [0,0,0],
    [1,0,1]
]


zero_matrix(mat)

print(mat)
print(mat==mata)
