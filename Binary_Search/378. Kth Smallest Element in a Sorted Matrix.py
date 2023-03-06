# method 1: Brute force
# using heap
# time: O(n^2 *log(n^2))
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap= []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heapq.heappush(heap, -1*matrix[r][c])
                if len(heap)> k:
                    heapq.heappop(heap)
        return -1*heap[0]


# method 2: using binary search
# time: O(n*log(A)), A= difference between minimum value and maximum value in the matrix.
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1321862/Python-Binary-search-solution-explained
# logic explanation: 
# We have a way to count how many numbers are less than or equal to x in the table 
# (let's call this function count(x)). We can simply apply binary search over the range [matrix[0][0], matrix[-1][-1]] 
# and iteratively check if mid has atleast k numbers less than or equal to mid.

# 1) If count(mid) < k, there are less than k numbers which are less than or equal to mid in the table. 
# So mid or any integer left than it can't be our answer. So eliminate search space loeft than mid by doing left = mid+1.
# 2) If count(mid) >= k, there are atleast k numbers (maybe more) which are less than or equal to mid in the table. 
# So, mid is a possible valid solution. But there can be a smaller number than mid as well which has count(.) >= k. 
# So, we mark current mid as possible answer ans and check for lower range as well by doing right = mid

# template 2 only.

class Solution(object):
    def kthSmallest(self, matrix, k):
        # here 'start' and 'end' is the key not the index
        def count(m):   # will give the number of elements which are smaller than or equal to 'mid'.
            # check in each row the no of elements greater than m. start from top right corner
            # in next row, you just have to check from latest col only as matrix is row wise and col wise sorted
            col, cnt= len(matrix[0]) -1, 0
            for row in range(len(matrix)):
                while col>= 0 and matrix[row][col]> m:  # just doing opposite 
                    col-= 1
                cnt+= col + 1   # after each col this will be the no of ele smaller than 'm'
            return cnt
        
        left, right= matrix[0][0], matrix[-1][-1]  # min will be at (0,0) and max will be at (n-1,n-1) i.e last ele. our ans can be in this range only.
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:   #
                right = mid  # try to looking for a smaller value in the left side but 'mid' can also be the ans.
            else:  # we have to increase the count so we have to search beyond mid i.e 'mid +1'.
                left = mid + 1  
        return left


# i was thinking since we are finding the mid and updating the start and mid acc to the mid.
# but mid may not be the ele in the matrix but we are updating these values according to the matrix value only so we will get the correct ans at last.
# so after while loop ans will be the ele that will be in matrix itself.
# after every valid(>=) equal to case, it will go closer and closer to the the ele present in the matrix for the ans.

# also try to understand the O(n) approach and do it later
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85170/O(n)-from-paper.-Yes-O(rows)
