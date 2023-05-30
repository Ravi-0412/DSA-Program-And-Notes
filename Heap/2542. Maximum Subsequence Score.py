# Intuition: 1) we have to take sum from num1 and minimum from nums2.
# so order will not matter.
# 2) for maximum we have to maximise ele in both the array i.e maximize both the sum and the multiplier.

# logic: Taking each ele in nums2 as minimum, find the max score we can get.
# for this sorting can make our work easy.
# Bt we have to keep track of mapping of ele in both arrays. => zip(nums1, nums)

# Then sort the above zipped array into ascending or descending order(better descending because cur ele in num2 will be minimum auto)
# Also we have to remove ele when len(sub) > k , & removed one must be minimum.
# for this we will use minHeap. => want length almost k and also want to remove minimum.

# Note: Zip + sorting +  heap + slding window(poping)

# Time complexity: O( N * Log(N) + (N-k) * Log(k) )
# Space complexity: O(N) + O(k) = O(N+K)

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # for mapping the ele from num1 to nums2
        pairs= [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        # sort the above array 'pair' according to values of nums2 in descending order
        pairs= sorted(pairs, key= lambda p: p[1], reverse= True)
        
        # now consider each ele in num2 as minimum and find the maximum score we can get.
        ans= 0
        n1sum= 0
        minHeap= []
        # cur n2 will always minimum since we are traversing in descending order.
        for n1, n2 in pairs:
            n1sum+= n1
            heapq.heappush(minHeap, n1)  # we have to remove the min from num1 if len(heap)=>subsequence become greater than 'k'
            if len(minHeap) > k:
                n1pop= heapq.heappop(minHeap)
                n1sum-= n1pop
            if len(minHeap) == k:
                ans= max(ans, n1sum * n2)
        return ans
