def gameOfLife(board):
    directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    m, n = len(board), len(board[0])
    
    for row in range(m):
        for col in range(n):
            lives = 0
            for nei in directions:
                nexti, nextj = row + nei[0], col + nei[1]
                if nexti < m and nexti >= 0 and nextj < n and nextj >= 0:
                    if board[nexti][nextj]==1 or board[nexti][nextj]==-1:
                        lives += 1
            if (board[row][col] == 1 and lives<2) or (board[row][col] == 1 and lives > 3):
                board[row][col] = -1

            if board[row][col] == 0 and lives == 3:
                board[row][col] = 2
    
    for row in range(m):
        for col in range(n):
            if board[row][col] > 0:
                board[row][col] = 1
            else:
                board[row][col] = 0 