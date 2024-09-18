# method 1 : Brute force (TLE)

# for update: we have to update all prefixSum value from that index to last index by diff= val- nums[index]

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums= nums
        n= len(nums)
        self.prefixSum= [0] * (n+1)   # using 1-based indxing for prefix sum.
        for i in range(1, n + 1):
            self.prefixSum[i]= self.nums[i-1] + self.prefixSum[i-1]
        

    def update(self, index: int, val: int) -> None:
        diff= val- self.nums[index] 
        self.nums[index]= val
        for i in range(index + 1, len(self.nums) + 1):
            self.prefixSum[i]= diff + self.prefixSum[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right + 1] - self.prefixSum[left]


# Method 2: segement Tree (Q is based on this only)

# vvi: Now from here intro of segment tree starts

# why came ?
# In case when we are updating and we want query result also then it reduces the time complexity a lot.

# If we use the prefixSum method then in this case if we want to update then,
# we have to update all prefixSum value from that index to last index by diff= val- nums[index]
# time: O(n)

# But using segment tree we can do this in  O(logn).

# Note: Draw diagram from 'Rachit Jain or Kunal' video in notes

# space = O(2*n - 1)

class Node(object):
    def __init__(self, startInterval, endInterval):
        self.total = 0    # RangeSum of given interval
        self.start = startInterval    # start interval of that node
        self.end = endInterval        # end interval of that node
        self.left = None
        self.right = None

class NumArray(object):

    def __init__(self, nums: List[int]):

        def createSegmentTree(nums , l, r):
            # base case. All ele will be at leaf 
            if l == r:
                # when there is single ele, we will start returning to parent and will update the parent RangeSum(total) value.
                node = Node(l, r)
                node.total = nums[l]
                return node
            # make one node for current query
            node = Node(l, r)   # RangeSum for now will be '0', will assign later.
            # we need to take sum of values from its children to update the RangeSum of this current node.
            # Go bottom up and make tree Recursively
            
            # range from 'l' to 'mid' will go to left and 'mid+1' to 'r' will go to right.
            # mid = (r - l + 1) //2     # wrong , this will give len(interval) //2 but we need mid between given range only
            mid = (l + r)//2
            node.left = createSegmentTree(nums , l, mid)
            node.right = createSegmentTree(nums , mid + 1, r)

            # Now assign the value of 'RangeSum' to cur Node interval i.e 'node'
            # will be equal to sum of 'RangeSum' of its children.
            node.total = node.left.total + node.right.total
            return node  
            
        self.nums = nums
        n= len(nums)
        self.root = createSegmentTree(nums, 0, n -1)

    # just first seacrh the given index.
    def update(self, index: int, val: int) -> None:
        # There will be two cases
        def updateValue(node, index , val):
            # 1) if index lies completely outside the node interval.
            # In this case just return the 'RangeSum' value of that node
            # since from here no any node of cur subtree will get impacted.
            if index < node.start or index > node.end:
                return node.total
            # 2) index lies in node interval 
            # In this case all node will get updated . But we will update bottom up only after updating the value at given index.
            # ANd we can get any element as single entity at leaf only.
            # So we will update going bottom up recursively.
            if index >= node.start and index <= node.end:   # No need of this 'if' we can do directly also
                # Base case: when we get the proper ele
                if node.start == index and node.end == index:
                    # update the value and start returning from here and keep updating the parent also recursively.
                    node.total = val
                    return val   # returning value to update value of parent directly
                # 'RangeSum' for current node will be sum of updated values of its children
                # so call the function recursively for children and keep updating
                node.total = updateValue(node.left, index , val) + updateValue(node.right, index , val)
                return node.total

        self.nums[index] = val
        updateValue(self.root, index , val)

    def sumRange(self, left: int, right: int) -> int:
        # there is three cases possible(2 base case and one normal) and we have to add the 'RangeSum' of all cases recursively.

        def RangeSum(node, l, r):
        
            # 1) node interval is completely inside the given query interval
            # whole RangeSum will contribute to the ans
            if node.start >= l and node.end <= r :
                return node.total
            # 2) node interval is completely outside the query interval
            # Return the default value based on operator i. for sum : "0", multiply : "1"
            # minEle = return maxPossible , maxEle: return minPossible
            if node.start > r or node.end < l:
                return 0
            # 3) if node interval and query interval is overlapping
            # In this case we need to calculate the ans recursively from its left and right child and return the sum of that.

            # mid = (l + r) //2   # no need of finding 'mid' while find 'RangeSum' like 'creatingTree'. just pass the given range only in fn calls.
            return RangeSum(node.left , l, r) + RangeSum(node.right , l, r)

        return RangeSum(self.root, left, right)


# Note vvvi: Few observations on segment tree implementation:
# 1) we are find the 'mid' only while 'creating' the tree, not in operation like 'RangeSum' and 'update'.
# No need of finding 'mid' in these cases.
# After finding the mid , we make left node from index (l, mid) and right node from (mid + 1, r)

# 2) RangeSum(l, r)
# In this for base case we are checking cases on node interval like: i) completely inside
# ii) completely outside   iii) overlapping      with given range
# Note: Here in each function call we are passing the same range for left and right i.e (l, r)

# 3) updateVal
# Here we are checking the cases on 'index' not on 'node interval ' like :
# i) if index is completely outside the node interval
# ii) if inside the node interval => under this finding the ele 1st recursively.

# Note: This is the difference between 'RangeSum' function and 'updateVal' function.
# keep this in mind and also the reasons why in both we are checking differently and 
# why 'mid' is not required in 'RangeSum' and 'updateVal' function.

# Some points regarding this method of implementing the segment tree:
# 1) follows the full binary tree property (all node will have exactly two node except the leaf node)
# 2) No of nodes = 2*n - 1 . (n = length of given array)
## How? => Total no of nodes = 2^h - 1= 2^(logn) - 1 == 2*n - 1

# So time complexity to create segment tree = O(n)

# 3) Time complexity for update and getRangeSum : O(logn)


# Template to use in other Q:
# Just above code only , only removed the comment.

class Node:
    def __init__(self, startInterval, endInterval):
        self.total = 0    # RangeSum of given interval
        self.start = startInterval    # start interval of that node
        self.end = endInterval        # end interval of that node
        self.left = None
        self.right = None

class SegmentTree:

    def __init__(self, nums: List[int]):          
        self.nums = nums
        n= len(nums)
        self.root = self.createSegmentTree(nums, 0, n -1)
    
    def createSegmentTree(self, nums , l, r):
        if l == r:
            node = Node(l, r)
            node.total = nums[l]
            return node

        node = Node(l, r)   # RangeSum for now will be '0', will assign later.

        mid = (l + r)//2
        node.left = self.createSegmentTree(nums , l, mid)
        node.right = self.createSegmentTree(nums , mid + 1, r)

        node.total = node.left.total + node.right.total
        return node

    def update(self, index: int, val: int) -> None:
        
        def updateValue(node, index , val):
            if index < node.start or index > node.end:
                return node.total

            if index >= node.start and index <= node.end:    # No need of this 'if' we can do directly also
                if node.start == index and node.end == index:
                    node.total = val
                    return val   # returning value to update value of parent directly
                
                node.total = updateValue(node.left, index , val) + updateValue(node.right, index , val)
                return node.total

        self.nums[index] = val
        updateValue(self.root, index , val)

    def sumRange(self, left: int, right: int) -> int:

        def RangeSum(node, l, r):
            if node.start >= l and node.end <= r :
                return node.total
            if node.start > r or node.end < l:
                return 0

            return RangeSum(node.left , l, r) + RangeSum(node.right , l, r)

        return RangeSum(self.root, left, right)
    


# Method 4: Fenwick Tree (Binary Indexed Tree)
# CraeteBIT takes : O(logn) for one call so will take O(n *logn) for craeting the BIT (calling for each index).
# Update = getSum= O(logn)

# Note: difference between 'Segment tree' and 'fenwick tree' is that 
# 1) in fenwick tree for finding range sum(i, j), we get by
# 'RangeSum(j) ( 0 to j)' - 'RangeSum(i)'.
# we need to go only from given node(index) to parent to find the RangeSum(i).

# 2) searching time i.e getting query is less in fenwick than segment 
# fenwick : O(logn), segment : O(4*logn)
# Because : we need to go only from given node(index) to parent to find the RangeSum(i).
# Here we don't go in other subtree like 'segment tree' (with that much cases).

# 2) Creation time is more in fenwick than segment
# fenwick : O(n*logn), segment : O(n)

# 3)
# Note vvi: You can't use 'Fenwick Tree' (Binary Indexed Tree) for finding 'min/max' in a given range.
# Reason: 
# it relies on the fact that the acummulative frequency from a to b is 'f(b)- f(a-1)', 
# and that property is not valid for the min/max functions
# i.e it stores value in range . if BIT[i] stores values in some range say (a, b) then, it will equal to 'f(b)- f(a-1)'.

# Note: tree will get formed correctly only but you will not get desired result in a range for 'min/max'.

# So for min/max use 'segment tree' only not fenwick tree.


# Note: 
# Now let's talk about function and some obseravtions:
# a) creating and update function:
# vvi: In these two function we are only updating values in 'next' of current node not in parent node.

# How we get 'next' of index i'.
# i) find 2's complement of 'i' => '-i'
# ii) And(&) with original given index 'i' => 'i & -i'
# iii) Add(+) with original given index => next(i) = i + (i & -i)


# b)for getting RangeSum
# we are taking sum of values from parent not from 'next'.

# How to get parent of 'i'.
# Ans: just swap the rightmost set bit to get the parent i.e unset last set bit 
# How to get this using bit?

# steps:
# i) find 2's complement of 'i' => '-i'
# ii) And(&) with original given index 'i' => 'i & -1'
# iii) subtract(-) with original given index => parent(i) = i - (i & -i)   # only diff from 'next'. here we are subtracting

# or in short
#  i &= i -1    # unset last set bit 


# Note: Draw diagram from Tushar video in notes

class NumArray:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.BIT = [0] *(self.n + 1)
        
        # create BIT
        for i in range(self.n):
            self.createBIT(i, nums[i])
    
    def createBIT(self, i, val):
        i += 1   # because BIT is following 1 based indexing not '0' based.
        # Keep adding the values starting from current index 'i' in BIT 
        # to other index by finding next until it goes out of range.
        # Going top to bottom(given node to leaf)
        while i <= self.n:
            self.BIT[i] += val
            i += (i & -i)    # next index where we need to update

    def update(self, index: int, val: int) -> None:
        # find the diff between values we will get after updating
        # After that we will add this 'diff' to all places where it can make impact i. next
        diff = val - self.nums[index]
        # update the value at given index
        self.nums[index] = val
        # Call the createBIT function to update the values at other places where it can make impact
        self.createBIT(index , diff)

    def getSum(self, i):
        sum = 0
        i += 1
        while i > 0:   # going bottom up so index value will decrease
            sum += self.BIT[i]
            # parent = i - (i & -i)
            # i = parent
            i &= i - 1
        return sum

    def sumRange(self, left: int, right: int) -> int:
        # We will get ans in BIT method by getSum(right) - getSum(left - 1)   , just like prefixSum way
        # for 'getSum(i)' we need to go bottom up starting from node 'i' to root and keep adding the value.
        return self.getSum(right) - self.getSum(left - 1)
                            # for understanding 'right + 1' - 'left' because we are storing value one index ahead.
    

# Template to use in other Q
# Above code only just removed the comment.

class segmentTree:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.BIT = [0] *(self.n + 1)
        
        # create BIT
        for i in range(self.n):
            self.createBIT(i, nums[i])
    
    def createBIT(self, i, val):
        i += 1   # because BIT is following 1 based indexing not '0' based.
        while i <= self.n:
            self.BIT[i] += val
            i += (i & -i)    # next index where we need to update

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.createBIT(index , diff)

    def getSum(self, i):
        sum = 0
        i += 1
        while i > 0:   # going bottom up so index value will decrease
            sum += self.BIT[i]
            i &= i - 1   # unset last set bit
        return sum

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(right) - self.getSum(left - 1)