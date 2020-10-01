#Note that this is not an inplace algorithm and takes up O(N^2) space
def matrix_rotation_mine(mat):  # O(N^2) solution as we are going through all of the elements of square matrix
    mat2 = []
    for i in (range(len(mat))):
        li = []
        for j in reversed(range(len(mat))):
            li.append(mat[j][i])
        mat2.append(li)
    return mat2

def matrix_rotation_nick(mat):
    if len(mat)==0 or len(mat)!= len(mat[0]):
        return "Rotation not possible!"
    n = len(mat)
    for i in range(n):
        for j in range(i+1,n):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
    for i in range(n):
        for j in range(n//2):
            temp = mat[i][j]
            mat[i][j] = mat[i][n-1-j]
            mat[i][n-1-j] = temp


mat = [[1,2,3], [4,5,6], [7,8,9]]
matrix_rotation_nick(mat)
print(mat)
