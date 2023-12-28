# Intuition: 1) we have to take sum from num1 and minimum from nums2.
# so order will not matter.
# 2) for maximum we have to maximise ele in both the array i.e maximize both the sum and the multiplier(min el from nums2).

# logic: Taking each ele in nums2(say at index j) as minimum, find the max score we can get.
# after that take 'k' ele from nums1 such that those ele include index 'j' and nums2[j] is minimum

# for this sorting can make our work easy.
# Bt we have to keep track of mapping of ele in both arrays. => zip(nums1, nums)

# Then sort the above zipped array into ascending or descending order(better descending because cur ele in nums2 will be minimum auto)
# Also we have to remove ele when len(sub) > k , & removed one must be minimum.
# for this we will use minHeap. => want length atmost k and also want to remove minimum.

# say n1 -> nums1 , n2 -> nums2
# for (n1, n2):
# n2 will always minimum since we are traversing in descending order.
# So we can take any 'k' numbers from numbers that we have visited till now from nums1.
# if now q reduces to keep 'k' maximum ele in heap from nums1 at any point of time.

# From above idea, we also get intitution to use min heap.

# Note: Zip + sorting +  heap + slding window(poping)

# Time complexity: O( N * Log(N) + (N-k) * Log(k) )
# Space complexity: O(N) + O(k) = O(N+K)

# Note: Array length must be equal otherwise this logic won't work.

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # for mapping the ele from num1 to nums2
        pairs= [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        # sort the above array 'pair' according to values of nums2 in descending order
        pairs= sorted(pairs, key= lambda p: p[1], reverse= True)
        
        # now consider each ele in num2 as minimum and find the maximum score we can get.
        ans= 0
        n1sum= 0  # will store the sum of ele from nums1 that we have included till now.
        minHeap= []
        
        for n1, n2 in pairs:
            n1sum+= n1
            heapq.heappush(minHeap, n1)  # we have to remove the min from num1 if len(heap)=>subsequence become greater than 'k'
                                        # removing min because we have to maximise ans.
            if len(minHeap) > k:
                # then it is better to not include top of heap for cur num 'n2'.
                n1pop= heapq.heappop(minHeap)
                n1sum-= n1pop
            if len(minHeap) == k:
                # 'n2' is minimum till now from 'nums2' and maximum sum we can get when 'n2' will be minimum = n1sum * n2.
                ans= max(ans, n1sum * n2)
        return ans


# Note: Why won't sort both array in descending order.
# And traverse nums2 and for each ele of nums2 take 'k' max_ele from nums1.

# This won't work because this will not guarantee that ele of nums2 is one of the chosen indices of nums1.

# But ziping it together will guarantee this.
    


# Related Q:
# 1383. Maximum Performance of a Team    => Exactly same question