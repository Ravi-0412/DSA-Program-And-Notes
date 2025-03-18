# Method 1:
"""
No need to check all 8 directions, we need to check only 4 directions from each cell if value = 1.
4 directions: upper- left diagonal, up, upper- right diagonal, right OR other four directions.
"""

def countConnections(matrix):
    m = len(matrix)
    n = len(matrix[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                # check upper- left diagonal
                if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1] == 1:
                    count += 1
                # check up
                if i - 1 >= 0 and matrix[i - 1][j] == 1:
                    count += 1
                # check upper- right diagonal
                if i - 1 >= 0 and j + 1 < n and matrix[i - 1][j + 1] == 1:
                    count += 1
                # check right
                if j + 1 < n and matrix[i][j + 1] == 1:
                    count += 1
    return count

# Method 2: 
"""
If you want to check all 8 diretions then you need to mark current call value = 0 to avoid duplication.
i) iterate over m * n matrix
ii) if matrix element == 1 check in all eight directions, count if adjacent is 1
iii) once done with this element set it as 0 so that no other element can count this again
"""

def count_connections(matrix):
    m, n = len(matrix), len(matrix[0])
    count = 0
    dirs = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] == 1:
                        count += 1
            matrix[i][j] = 0   # marking 
    return count

