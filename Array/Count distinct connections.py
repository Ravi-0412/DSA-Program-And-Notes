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
