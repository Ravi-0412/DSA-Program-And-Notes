# method 1: Brute force
# using heap
# time: O(n^2 *log(n^2))
# space : O(n^2)
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap= []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heapq.heappush(heap, -1*matrix[r][c])
                if len(heap) > k:
                    heapq.heappop(heap)
        return -1*heap[0]
    
# methopd 2: VVI (very good approach)
# modifying heap and using the sorted rows and columns benefit.
# logic: Since each of the rows in matrix are already sorted, we can understand the problem as 
# "finding the kth smallest element from amongst M sorted rows."
    
# We start the pointers to point to the beginning of each rows as all next smaller ele will be connected to this pointer only.
#  then we iterate k times to find the ans.
# for each time ith, the top of the minHeap is the ith smallest element in the matrix. 
# We pop the top from the minHeap then add the next element which has the same row & next col with the poped one
# as this ele can be next minimum.

# Time: O(k* log(min(k, m)) + O(k*logk))
# Space: O(K)
class Solution(object):
    def kthSmallest(self, matrix, k):
        m, n= len(matrix), len(matrix[0])
        minHeap= []
        # insert first 'k' values of all rows i.e values of 1st col as smallest ele will be from these 'k' elements.
        for r in range(min(k, m)):  # max this much row we will have to visit to get the ans.
            heapq.heappush(minHeap, (matrix[r][0], r, 0))   # every smaller ele will be connected to these ele only.
        
        # now start poping and add the next smaller ele w.r.t poped ele and that will be in the next col of same row.
        while k > 1 :  # pop the first 'k-1' smallest ele 
            num, r, c= heapq.heappop(minHeap)
            k-= 1
            if c + 1 < n:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))  # next smaller ele will next to this poped ele or will be already in the heap.
        return minHeap[0][0]  # now kth smallest will be on the top of heap.



# method 3: using binary search (more optimised)
# time: O((m + n) *log(A)), A= difference between minimum value and maximum value in the matrix.
# logic explanation: 
# We have a way to count how many numbers are less than or equal to x in the table 
# (let's call this function count(x)). We can simply apply binary search over the range [matrix[0][0], matrix[-1][-1]] 
# and iteratively check if mid has atleast k numbers less than or equal to mid.

# 1) If count(mid) < k, there are less than k numbers which are less than or equal to mid in the table. 
# So mid or any integer left than it can't be our answer. We have to increase our mid and for this we will incr 'left' i.e left = mid+1.
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
                cnt+= col + 1   # this much will be the no of ele <= 'm' in 'i'th row
            return cnt
        
        left, right= matrix[0][0], matrix[-1][-1]  # min will be at (0,0) and max will be at (n-1,n-1) 
                                                    # i.e last ele. our ans can be in this range only.
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:   #
                right = mid  # try to looking for a smaller value in the left side but 'mid' can also be the ans.
            else:  # we have to increase the count so we have to search beyond mid i.e 'mid +1'.
                left = mid + 1  
        return left


# we can write 'count(mid)' like this also. Replaced inner 'while' with 'if'.
def count(m):
    row , col = len(matrix) , len(matrix[0])  # declaring globally giving error so did inside function.
    r, c = 0, col - 1
    cnt = 0
    while r < row and c >= 0:
        if matrix[r][c] > m:
            c -= 1
        else:
            cnt += c + 1
            r += 1
    return cnt


# also try to understand the O(n) approach and do it later
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85170/O(n)-from-paper.-Yes-O(rows)


# Similar Q:
# i) Find median in row wise sorted matrix
# ii) 668. Kth Smallest Number in Multiplication Table
# iii) 2560. House Robber IV
