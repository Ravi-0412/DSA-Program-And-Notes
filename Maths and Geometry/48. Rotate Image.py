# time: O(n)
# logic: first take row then take transpose 

class Solution:
    def rotate(self, A):
        row,col= len(A), len(A[0])
        # first reverse the row not the element inside the row.
        # for c in range(col):
        #     for r in range(row//2):
        #         A[r][c], A[row-r-1][c]= A[row-r-1][c], A[r][c]
        
        l = 0
        r = row -1
        while l < r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1
        # now rotate the element w.r.t diagonal. we are taking the transpose only.
        for r in range(row):
            for c in range(r, col):   # starting from 'r' to avoid swaping twice for already swapped element.
                A[r][c], A[c][r]= A[c][r], A[r][c]
        
# another way of writing the same logic
class Solution:
    def rotate(self, A):
        row,col= len(A), len(A[0])
        # first reverse the row not the element inside the row.
        A.reverse()
        # now rotate the matrix w.r.t diagonal
        for r in range(row):
            for c in range(r):
                A[r][c], A[c][r] = A[c][r], A[r][c]


# go through these links while revising.

#https://leetcode.com/problems/rotate-image/solutions/1449737/rotation-90-code-180-270-360-explanation-inplace-o-1-space/
# https://leetcode.com/problems/rotate-image/solutions/18872/a-common-method-to-rotate-the-image
# https://leetcode.com/problems/rotate-image/solutions/18884/seven-short-solutions-1-to-7-lines/


# for anticlokwise, reverse the column and then take the transpose.
# 90: Transpose + Reverse Rows
# 180: Reverse Rows + Reverse columns
# 270 : Transpose + Reverse Columns