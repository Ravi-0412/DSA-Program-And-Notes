# time: O(n)
# logic: first reverse rows then take transpose.

# Tranpose of a matrix = Rotation along diagonal :
# 1st row ele => 1st col
# 2nd row ele => 2nd col and so on.

# Intuition: All rotations are composite reflections (in fact, all transformations are composite reflections);
#  in this case, a reflection across the vertical line of symmetry, then a reflection across the diagonal. 

class Solution:
    def rotate(self, A):
        row,col= len(A), len(A[0])
        # first reverse the row not the element inside the row.
        
        l = 0
        r = row -1
        while l < r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1
        # now rotate the element w.r.t diagonal. we are taking the transpose only.
        for r in range(row):
            for c in range(r, col):   # starting from 'r' to avoid swaping twice for already swapped element.
                # column 'c' me hmko 'r' se element to swap karna h.
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

# 
# https://leetcode.com/problems/rotate-image/solutions/18884/seven-short-solutions-1-to-7-lines/

# Note vvvi:
# for anticlokwise 90 degree, reverse the column and then take the transpose i.e rotate along diagonal.

# For clockwise:
# 90: Reverse Rows + Transpose
# 180: Reverse Rows + Reverse columns
# 270 : Transpose + Reverse Columns

# For anticlocwise: Just do opposite operation of clockwise.
# 90 => reverse columns + transpose
# 180 => Reverse columns + reverse rows
# 270 => Reverse columns + Transpose

# other way for both clockwise and anticlock wise:
# 180 => rotate 2 times by '90'
# 270 => rotate 3 times by '90' and so on.