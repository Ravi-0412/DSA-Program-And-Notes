# this will form a matrix virtually in which every row and column will be sorted in ascending order.
# so we can apply the same binary search logic of Q : "378. Kth Smallest Element in a Sorted Matrix".

# Difference in both: 
# Here instead of comparing with matrix value we will compare with (row) *(col).
# Here did the coordinate shidt of rwo and col by '1' to directly compare with (row*col). 
# (If we will start from index '0' then we will compare with (row +1)*(col +1) and cnt+= col +1)

# Here we can say that we are maintaing the virtual matrix.

# time: O(n *log(m*n))

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # here 'start' and 'end' is the key not the index
        def count(mid):  # will give the number of elements which are smaller than or equal to 'mid'.
            # check in each row the no of elements greater than m. start from top right corner
            # in next row, you just have to check from latest col only as matrix is row wise and col wise sorted
            col, cnt= n, 0
            for row in range(1, m +1):
                while col>= 1 and (row)* (col)> mid:  # just doing opposite 
                    col-= 1
                cnt+= col   # after each col this will be the no of ele <= 'm'
            return cnt
        
        left, right= 1, m*n  # min will '1' and max will be (m*n) i.e last ele.
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid  # try to looking for a smaller value in the left side but 'mid' can also be the ans.
            else:  # we have to increase the count so we have to search beyond mid i.e 'mid +1'.
                left = mid + 1  
        return left