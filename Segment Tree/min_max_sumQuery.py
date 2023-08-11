# Note vvi: You can't use 'Fenwick Tree' (Binary Indexed Tree) for finding 'min/max' in a given range.
# Reason: 
# it relies on the fact that the acummulative frequency from a to b is 'f(b)- f(a-1)', and that property is not valid for the min/max functions
# i.e it stores value in range . if BIT[i] stores values in some range say (a, b) then, it will equal to 'f(b)- f(a-1)'.

# Note: tree will get formed correctly only but you will not get desired result in a range for 'min/max'.

# Use fenwick tree in operations other than 'min/max'.

# My mistake:
class segmentTree:
    
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.BITMin = [float('inf')] *(self.n + 1)
        # BITMin[i] will store minimum value for a range
        self.BITMax = [float('-inf')] *(self.n + 1)
        # BITMax[i] will store maximum value for a range
        self.BITSum = [0] *(self.n + 1)    # BITSum[i] will store sum for a range
        
        # create BIT for min/max and sum
        for i in range(self.n):
            self.createBITMinMax(i, nums[i])  # for min/max
            self.createBITSum(i, nums[i])     # for sum
    
    def createBITMinMax(self, i, val):
        i += 1   # because BIT is following 1 based indexing not '0' based.
        while i <= self.n:
            self.BITMin[i] = min(self.BITMin[i], val)
            self.BITMax[i] = max(self.BITMax[i], val)
            i += (i & -i)    # next index where we need to update
    
    def createBITSum(self, i, val):
        i += 1   # because BIT is following 1 based indexing not '0' based.
        while i <= self.n:
            self.BITSum[i] += val
            i += (i & -i)    # next index where we need to update
    
    def update(self, i, val):
        diff = val - self.nums[index]
        self.nums[i] = val
        
        # We have to update min, nax & sum
        # 1) updating min/max
        # Here we will check with new valuw
        self.createBITMinMax(i, val)
        
        # 1) updating sum
        # Here we will update with 'diff'
        self.createBITSum(i, diff)

    def getMin(self, i):
        ans = float('inf')
        i += 1
        while i > 0:   # going bottom up so index value will decrease
            ans=  min(ans, self.BITMin[i])
            parent = i - (i & -i)
            i = parent
        return ans
        
    def getMax(self, i):
        ans = float('-inf')
        i += 1
        while i > 0:   # going bottom up so index value will decrease
            ans=  max(ans, self.BITMax[i])
            parent = i - (i & -i)
            i = parent
        return ans
    
    def getSum(self, i):
        sum = 0
        i += 1
        while i > 0:   # going bottom up so index value will decrease
            sum += self.BITSum[i]
            parent = i - (i & -i)
            i = parent
        return sum
    
    def getRangeSum(self, i, j):
        return self.getSum(j) - self.getSum(i - 1)
    
    def getRangeMin(self, i, j):
        return min(self.getMin(j) , self.getMin(i -1))
    
    def getRangeMax(self, i, j):
        return max(self.getMax(j) , self.getMax(i -1))

nums = [12, 0, 1, 3, 5, 7, 9, 11]
s = segmentTree(nums)
i, j = 2, 5
print(s.BITMin, s.BITMax, s.BITSum)
print("sum between range {} and {} is: ".format(i, j), s.getRangeSum(i, j))
print("MinEle between range {} and {} is: ".format(i, j), s.getRangeMin(i, j))
print("MaxEle between range {} and {} is: ".format(i, j), s.getRangeMax(i, j))


# Correct code to get min/max/sum in a given range Using 'segment Tree'.
# Use this template in case of min/max/sum

# Just similar logic to "307.Range Sum Query"

class Node:
    def __init__(self, startInterval, endInterval):
        self.total = 0    # RangeSum of given interval
        self.start = startInterval    # start interval of that node
        self.end = endInterval        # end interval of that node
        self.MinVal = float
        self.MaxVal = float('-inf')
        self.left = None
        self.right = None

class SegmentTree:

    def __init__(self, nums):          
        self.nums = nums
        n= len(nums)
        self.root = self.createSegmentTree(nums, 0, n -1)
    
    def createSegmentTree(self, nums , l, r):
        if l == r:
            node = Node(l, r)
            node.total = nums[l]
            node.MinVal = nums[l]
            node.MaxVal = nums[l]
            return node

        node = Node(l, r)   # RangeSum for now will be '0', will assign later.

        mid = (l + r)//2
        node.left = self.createSegmentTree(nums , l, mid)
        node.right = self.createSegmentTree(nums , mid + 1, r)

        node.total = node.left.total + node.right.total
        node.MinVal= min(node.left.MinVal , node.right.MinVal)
        node.MaxVal= max(node.left.MaxVal , node.right.MaxVal)
        return node

    def update(self, index: int, val: int) -> None:
        
        def updateSum(node, index , val):
            # if index doesn't lie then return default value
            if index < node.start or index > node.end:
                return node.total
            # if index lie
            if index >= node.start and index <= node.end:
                if node.start == index and node.end == index:
                    node.total = val
                    return val   # start returning value to update value of parent directly
                
                node.total = updateValue(node.left, index , val) + updateValue(node.right, index , val)
                return node.total
        
        def updateMin(node, index , val):
            if index < node.start or index > node.end:
                return float('inf')   # return very big value to nullify it's impact

            if index >= node.start and index <= node.end:
                if node.start == index and node.end == index:
                    node.MinVal = val
                    return val   # returning value to update value of parent directly
                
                node.MinVal = min(updateValue(node.left, index , val) , updateValue(node.right, index , val))
                return node.MinVal
        
        def updateMax(node, index , val):
            if index < node.start or index > node.end:
                return float('-inf')   # return very big value to nullify it's impact

            if index >= node.start and index <= node.end:
                if node.start == index and node.end == index:
                    node.MinVal = val
                    return val   # returning value to update value of parent directly
                
                node.MinVal = max(updateValue(node.left, index , val) , updateValue(node.right, index , val))
                return node.MaxVal
        
        self.nums[index] = val
        # We will have to update all three
        updateSum(self.root, index , val)
        updateMin(self.root, index , val)
        updateMax(self.root, index , val)


    def getRangeSum(self, left: int, right: int) -> int:

        def RangeSum(node, l, r):
            # if interval lie fully in cur node then simply return node value
            if node.start >= l and node.end <= r :
                return node.total
            # If interval is outside for cur node then return default value
            if node.start > r or node.end < l:
                return 0

            return RangeSum(node.left , l, r) + RangeSum(node.right , l, r)

        return RangeSum(self.root, left, right)
        
    def getRangeMin(self, left: int, right: int) -> int:

        def RangeMin(node, l, r):
            if node.start >= l and node.end <= r :
                return node.MinVal
            if node.start > r or node.end < l:
                return float('inf')

            return min(RangeMin(node.left , l, r) , RangeMin(node.right , l, r))

        return RangeMin(self.root, left, right)
    
    def getRangeMax(self, left: int, right: int) -> int:

        def RangeMax(node, l, r):
            if node.start >= l and node.end <= r :
                return node.MaxVal
            if node.start > r or node.end < l:
                return float('-inf')

            return max(RangeMax(node.left , l, r) , RangeMax(node.right , l, r))

        return RangeMax(self.root, left, right)
        
nums = [12, 0, 1, 3, 5, 7, 9, 11]
s = SegmentTree(nums)
i, j = 3,6
print("sum between range {} and {} is: ".format(i, j), s.getRangeSum(i, j))
print("MinEle between range {} and {} is: ".format(i, j), s.getRangeMin(i, j))
print("MaxEle between range {} and {} is: ".format(i, j), s.getRangeMax(i, j))
