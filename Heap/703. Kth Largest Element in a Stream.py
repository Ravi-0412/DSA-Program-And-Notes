# add will give ans in O(1) only

import heapq
class KthLargest:   
    def __init__(self, k: int, nums: List[int]):
        self.k= k
        self.nums= nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:  # will run 'n-k' times only as there will be only one extra ele in heap always
            heapq.heappop(self.nums)
        return self.nums[0]
