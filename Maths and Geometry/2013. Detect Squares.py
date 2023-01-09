# time: O(n)= space
# Note: in same way you can form rectangle.
from collections import defaultdict
class DetectSquares:
    def __init__(self):
        self.ptsCount= defaultdict(int)  # store the no of occurence of each point
        self.points= []   #  store the points. storing separately with 'count' as hashmap will remove the duplicates
        
    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)]+= 1  # list cant be the key so converting into tuple
        self.points.append(point)
        
    def count(self, point: List[int]) -> int:
        res= 0
        px, py= point
        # find if there any diagonal exist for this point.
        # diagonal will be only present if abs(px -x)== abs(py -y)
        for x, y in self.points:
            if (abs(px -x)!= abs(py - y)) or px== x or py==y :  # 2nd case for +ve area. it can form square with its duplictes but area will be '0'.
                continue
            # now we have found the diagonal, now search if other two points exists.
            # if exists then add the count of those in the result(after multiplying).
            # coordinates of other two points will be (x, py) and (px, y),
            # if they will form square with the these two points(diagonal one) i.e (x, y) and (px, py)
            res+= self.ptsCount[(x, py)] * self.ptsCount[(px, y)]  
        return res
