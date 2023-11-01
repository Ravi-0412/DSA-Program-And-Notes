# time: O(n)= space
# Note: in same way you can form rectangle.

# Do on pen and paper to understand properly.

# Logic: for given point, find if there exist any diagonal.
# if diagonal exist then multiply with occurences of diagonal and points and add into the ans.

# Time: add: O(1)
# count: O(T), where T <= 5000 is total number of points after calling add.
# Space: O(T)

from collections import defaultdict
class DetectSquares:
    def __init__(self):
        self.ptsCount= Counter()  # store the no of occurence of each point
        # self.ptsCount = collection.defaultdict(int)  # will give error when any key won't present.
        
    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1  # list cant be the key so converting into tuple
        
    def count(self, point: List[int]) -> int:
        res= 0 
        px, py= point
        # find if there any diagonal exist for this point.
        # diagonal will be only present if abs(px -x)== abs(py -y) i.e horizontal and vertical length should be equal.
        for (x, y), cnt in self.ptsCount.items():
            if (abs(px -x)!= abs(py - y)) or px== x or py==y :  # 2nd case for +ve area. it can form square with its duplictes but area will be '0'.
                continue
            # now we have found the diagonal, now search if other two points exists.
            # if exists then add the count of those in the result(after multiplying).
            # coordinates of other two points will be (x, py) and (px, y),
            # if they will form square with the these two points(diagonal one) i.e (x, y) and (px, py)
            res+= cnt * self.ptsCount[(x, py)] * self.ptsCount[(px, y)]  # just like we can choose one element from given frequency.
        return res


# Differenec between 'Counter()' and 'defaultdict(int)'.
# Both Counter and defaultdict(int) can work fine here, but there are few differences between them:
# a) Counter supports most of the operations you can do on a multiset. 
# So, if you want to use those operation then go for Counter.

# b) Counter won't add new keys to the dict when you query for missing keys. 
# So, if your queries include keys that may not be present in the dict then better use Counter.

# Method 2:
# Given p1, try all points p2 (same x-axis) then compute the positions of 2 remain points p3, p4.

# To compute count(p1):
# We try all the points p2 which has the same x-axis with p1, it means p2.x = p1.x
# Since we have 2 points p1 and p2, we can form a square by computing the positions of 2 remain points p3, p4.
# Calculate sideLen = abs(p1.y - p2.y)
# Case 1: p3, p4 points are in the left side of line p1p2
# p3 = (p1.x - sideLen, p2.y)
# p4 = (p1.x - sideLen, p1.y)
# Case 2: p3, p4 points are in the right side of line p1p2
# p3 = (p1.x + sideLen, p2.y)
# p4 = (p1.x + sideLen, p1.y)


class DetectSquares:
    def __init__(self):
        self.xPoints = defaultdict(list)
        self.cnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xPoints[x].append(y)
        self.cnt[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ans = 0
        for y2 in self.xPoints[x1]:
            if y2 == y1: continue  # Skip empty square
            sideLen = abs(y2 - y1)

            # Case: p3, p4 points are in the left side
            x3, y3 = x1 - sideLen, y2
            x4, y4 = x1 - sideLen, y1
            ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]

            # Case 2: p3, p4 points are in the left side
            x3, y3 = x1 + sideLen, y2
            x4, y4 = x1 + sideLen, y1
            ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]
        return ans