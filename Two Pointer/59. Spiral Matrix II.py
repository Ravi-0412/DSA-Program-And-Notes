# Logic: 
"""
Same as : "54. Spiral Matrix"
Just keep on adding element at the cell we are visiting.
Take a counter 'cnt' that will tell what value we have to add that cell and 
for exit condition.

"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:   # without this it will give TLE because count will never increment.
            return [[1]]
        res = [[0 for j in range(n)] for i in range(n)]
        row, col= n, n
        up= 0                  # rowBegin
        down= row -1    # rowEnd
        left= 0                # colBegin
        right= col  -1  # colEnd
        cnt = 1
        while cnt <= row * col:
            # Traverse right, proper row should be fixed
            for c in range(left, right +1):
                if len(res) >= row * col:
                    break
                res[up][c] = cnt
                cnt += 1
            # Traverse down, proper col should be fixed
            for r in range(up +1, down +1):
                if len(res) >= row * col:
                    break
                res[r][right] = cnt 
                cnt += 1
            # Traverse left, proper row should be fixed
            for c in range(right-1, left-1, -1):
                if len(res) >= row * col:
                    break
                res[down][c] = cnt 
                cnt += 1
            # Traverse up, proper col should be fixed
            for r in range(down-1, up, -1):
                if len(res) >= row * col:
                    break
                res[r][left] = cnt 
                cnt += 1
            up, down, left, right= up + 1, down -1, left + 1, right -1
        return res

# concise way
# logic : 
"""
Why 'dx, dy = -dy, dx'?
Initial slope m1 is dy/dx
after a 90 deg rotation the slope becomes m2
since the angle between the lines is 90 degree
m1 * m2 = -1
m2 = -1/m1 = -dx/dy
"""
# Time: O(n^2)

class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 1, 0
        for i in range(n * n):
            matrix[y][x] = i + 1    # Initailly going right keeping 'y' same 
            # if index goes out of bound or it visites the already modified cell
            # change the direction by 90 degree
            if (x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n or matrix[y + dy][x + dx] != 0):
                dx, dy = -dy, dx
            x, y = x + dx, y + dy
        return matrix
