# using min heap
# time: O(nlogn)
# but not able to break the tie for equal fre elements
import heapq
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count= {}
        for num in nums:
            count[num]= 1+ count.get(num, 0)
        heap= []  
        # create a min heap with freq , key 
        for k,v in count.items():
            heapq.heappush(heap,(v,-1*k))   # added the num with negative sign to bring the num with larger value first in case of equal frequency
        # now add the ele into ans arr as many times they have occured(equal to their freq)
        ans= []
        while(len(heap)):
            temp = heapq.heappop(heap)
            for i in range(temp[0]):     # temp[0] will contain the fre of the ele
                ans.append(-1*temp[1])      # temp[1] will contain the ele
        return ans

# method 2: can be optimised to O(n) using bucket sort


# another method: try to understand
https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/917795/C%2B%2BPython-Sort


# another method:(try to understand)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums,reverse=1),key=nums.count)

# try to understans this also
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        return sorted(sorted(nums, reverse=True), key=lambda x: d[x])