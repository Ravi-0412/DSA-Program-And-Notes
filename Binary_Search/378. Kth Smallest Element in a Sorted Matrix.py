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
# time: O(n*log(A)), A= difference between minimum value and maximum value in the matrix
# but not getting how we updating 'end' and 'start'
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1321862/Python-Binary-search-solution-explained
class Solution(object):
    def kthSmallest(self, matrix, k):
        n, start, end= len(matrix), matrix[0][0], matrix[-1][-1]  # min will be at (0,0) and max will be at (n-1,n-1)
        # here 'start' and 'end' is the key not the index
        def count(m):
            # check in each row the no of elements greater than m. start from top right corner
            # in next row, you just have to check from latest col only as matrix is row wise and col wise sorted
            col, cnt= len(matrix[0]) -1, 0
            for row in range(len(matrix)):
                if col>= 0 and matrix[row][col]> m:  # just doing opposite 
                    col-= 1
                cnt+= col + 1   # after each col this will be the no of ele smaller than 'm'
            return cnt
        
        while start < end:
            mid= start + end//2
            # find the no of elements greater than mid
            if count(mid)< k:   # if less then incr the start to get the mid as bigger value
                start= mid +1
            else: # decr the end
                end= mid
        return start

# i was thinking since we are finding the mid and updating the start and mid acc to the mid.
# but mid may not be the ele in the matrix but since we are finding the count acc to the ele of matrix.
# so after while loop ans will be the ele that will be in matrix itself.
# after every valid(>=) equal to case, it will go closer and closer to the the ele present in the matrix for the ans.

# also try to understand the O(n) approach and do it later
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85170/O(n)-from-paper.-Yes-O(rows)
