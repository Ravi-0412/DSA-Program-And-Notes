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
            heapq.heappush(heap,(v,k))
        print(heap)
        # now add the ele into ans arr as many times they have occured(equal to their freq)
        ans= []
        while(len(heap)):
            temp = heapq.heappop(heap)
            for i in range(temp[0]):     # temp[0] will contain the fre of the ele
                ans.append(temp[1])      # temp[1] will contain the ele
        return ans


# method 2 :(try to understnd the method given in dicussion, link is there in xl file)



# another method: try to understand
https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/917795/C%2B%2BPython-Sort


# another method:(try to understand)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums,reverse=1),key=nums.count)