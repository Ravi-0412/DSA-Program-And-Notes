# just same logic as :" 462. Minimum Moves to Equal Array Elements II".

# Point should be median point of all 'x' and all 'y' coordinates where house is present respectively.

def findBestMeetingPoint(mat):
    n, m= len(mat), len(mat[0])
    # first store all 'x' and 'y' coordinates where house is present in separate arrays.
    x, y = [], []
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                x.append(i)
                y.append(j)
    # Get the median of 'x' and 'y' coordiantes.
    # sort both x and y coordinates of all houses
    x.sort()
    y.sort()
    lx, ly= len(x), len(y)
    median_x= x[lx//2] if lx % 2 else (x[lx//2] + x[lx//2 -1]) //2
    median_y= y[ly//2] if ly % 2 else (y[ly//2] + y[ly//2 -1]) //2
    median = (median_x, median_y)   # our meeting point
    # Now calculate the cost of all houses from median point
    cost = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                cost += abs(median_x - i) + abs(median_y - j)
    return cost