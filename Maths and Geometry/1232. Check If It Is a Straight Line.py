# method 1: slope of all pair should be equal.
# time= O(n)

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope= None
        if coordinates[1][0] - coordinates[0][0]== 0:
            slope= float('inf')
        else:
            slope= (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        pre_x, pre_y= coordinates[1][0] , coordinates[1][1]
        for i in range(2, len(coordinates)):
            slope1= None
            if coordinates[i][0] - pre_x == 0:
                slope1= float('inf')
            else:
                slope1= (coordinates[i][1] - pre_y) / (coordinates[i][0] - pre_x)  # no need to take 'abs'.
            # checking if slope is equal or not.
            if slope != slope1:
                return False
            pre_x, pre_y= coordinates[i][0] , coordinates[i][1]
        return True


# method 2: just same logic as above
# But doing other way to avoid handling the 'infinity case' i.e when x2- x1= 0

# logic: All points should be collinear.
# just applying the logic of "checking three points are collinear".
# Three points are: first one(A), 2nd one(B) and current point(C).

# Three points 'A', 'B', 'C' are said to be collinear if slope of AB = BC
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0= coordinates[0]   # 'A'
        x1, y1= coordinates[1]   # 'B'
        for x, y in coordinates:
            if (y1 - y0) * (x - x1) != (y - y1) * (x1 - x0): # Just equating slope of AB = BC
                return False
        return True