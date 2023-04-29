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
        

# Method 2: using sum function of python (got accepted.)
# sum function is very very fast 

# note: for finding ans , if range is less than n//2 then directly calculating from nums array like "return sum(self.nums[left: right + 1])".
# if greater then we are taking the help of whole sum array and subtracting the sum which is not in range.

class NumArray:
    
    def __init__(self, nums: List[int]):
        self.nums= nums
        self.sums= sum(nums)
        

    def update(self, index: int, val: int) -> None:
        self.sums+= val - self.nums[index]
        self.nums[index]= val
        

    def sumRange(self, left: int, right: int) -> int:
        if right - left < len(self.nums)//2:
            return sum(self.nums[left: right + 1])
        return self.sums - sum(self.nums[: left]) - sum(self.nums[right + 1 : ])
        
# method 3: Do by Segment Tree after studying

# method 4: Do by "Binary Indexed Tree" after studying.

# Note: all link soultion in sheet