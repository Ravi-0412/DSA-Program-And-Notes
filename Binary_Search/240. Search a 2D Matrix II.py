# 1st method: Brute force O(N^2)

# 2nd method: just apply binary search in each row or each column
# time: O(mlogn)


# 3rd method: 
# Exactly same as method 3 of q : "74. Search a 2D Matrix" because here matrix is sorted row wise and column wise.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col= len(matrix), len(matrix[0])
        down, left= 0 , col -1
        while down < row and left >=0:  # 'i' will always go down(max till row-1) and 'j' will always go left max till '0'
            # if found then return True
            if matrix[down][left]== target:
                return True
            elif matrix[down][left] > target: # it means target will be present on the previous col
                                        # as all col is also sorted and we need to search the ele 
                                        # lesser than current one
                left -= 1
            elif matrix[down][left] < target:  # it means target will be present on the next rows
                                        # as all row  is also sorted and we need to search the 
                                        # ele greater than current one
                down+= 1
        return False

# Note Vvi: 
# Difference from Q :"74. Search a 2D Matrix"
# This current Q only guarantee the row and col are sorted not whole ele is sorted.
# so we can't all apply methods of Q :"74".

# Note: Here we can't decide the row number checking 1st and last value of any row.

# 4th method: you can also start searching from bottom-left point
# and change the variable accordingly

# Note: Only in bove two cases we can make a decision where to move
# and in case if we start from other corner we won't be able to make
# decision where to move, there will be more than one possibility in other cases.