# Method 1: Brute force
# Time: O(n*logn + n * k)
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        for n in sorted(count):  # will return a list of keys in sorted order
            if count[n] > 0:
                # then next 'k' element must have frequency >= count[n]
                need = count[n]
                for i in range(n,n+k):
                    if count[i] < need:
                        return False
                    count[i] -= need
        return True


# Method 2:
# Logic: Just try to form divide array into size of 'k' such that all
# elements are consecutive.

#  steps:
# 1) Count the frequency of all elements.
# 2) Now we have to traverse ele one by one in ascending order(smallest first) and 
# try to subdivide array into size of 'k' with first ele as smallest element in remaining unused element.
# 2.1) we have to use same element again if its freq > 1.
# so in cases when you have to reuse element again and again in either
# ascending or descending order then think of heap.

# Note: All elements used in current group should be added again 
# if there frequency is > 1. 
# for this take a temporary element to keep tarck of such element.

# Time: O(n *logk + 2*n) , 2*n: for temporary array

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        freq = Counter(nums)
        minHeap = []
        for key, val in freq.items():
            heapq.heappush(minHeap, [key, val])
        while minHeap:
            if len(minHeap) < k:
                return False
            temp = []   # for inserting the poped number again if they have frequency > 1.
            num1, f1 = heapq.heappop(minHeap)
            if f1 > 1:
                temp.append([num1, f1- 1])
            for i in range(k - 1):
                num2, f2 = heapq.heappop(minHeap)
                if num1 + 1 != num2:
                    return False
                if f2 > 1:
                    temp.append([num2, f2- 1])
                num1 = num2
            for i in range(len(temp)):
                num, f = temp[i]
                heapq.heappush(minHeap, [num, f])
        return True

# No need to push 'freq' with 'num' in heap.
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        freq = Counter(nums)
        minHeap = []
        for key in freq.keys():
            heapq.heappush(minHeap, key)
        while minHeap:
            if len(minHeap) < k:
                return False
            temp = []
            num1 = heapq.heappop(minHeap)
            freq[num1] -= 1
            if freq[num1] > 0:
                temp.append(num1)
            for i in range(k - 1):
                num2= heapq.heappop(minHeap)
                if num1 + 1 != num2:
                    return False
                freq[num2] -= 1
                if freq[num2] > 0:
                    temp.append(num2)
                num1 = num2
            for num in temp :
                heapq.heappush(minHeap, num)
        return True


# Related q:
# 1) 846. Hand of Straights
# 2) VVI: 659. Split Array into Consecutive Subsequences





        