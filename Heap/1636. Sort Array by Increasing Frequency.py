# method 1: 

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
            # add the num with negative sign to bring the num with larger value first in case of equal frequency
            heapq.heappush(heap,(v,-1*k))   
        # now add the ele into ans arr as many times they have occured(equal to their freq)
        ans= []
        while(len(heap)):
            temp = heapq.heappop(heap)
            for i in range(temp[0]):     # temp[0] will contain the fre of the ele
                ans.append(-1*temp[1])      # temp[1] will contain the ele
        return ans
    
# Shortcut of above method
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        # sorting nums
        # count[x] sorts by frequency, and if two values are equal, it will sort the keys in decreasing order.
        return sorted(nums, key=lambda x: (count[x], -x))  


# method 2: can be optimised to O(n) using bucket sort
# Try later

