# 1st method: Brute force O(N^2)

# 2nd method: just apply binary search in each row
# time: O(mlogn)


# 3rd method: 
# it's is pretty nicee and easy problem , it's approach is soo nicee
# logic: just start checking from top right corner and
# if not found tehn update the value of iterating variable properly
# where we can get the element just like binary search
# Time: O(m+n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col= len(matrix), len(matrix[0])
        i, j= 0 , col -1
        while i< row and j >=0:  # ending conding will be this as 
                                # 'i' will always go down(max till row-1) and
                                # 'j' will always go left max till '0'
            # if found then return True
            if matrix[i][j]== target:
                return True
            elif matrix[i][j] > target: # it means target will be present on the previous col
                                        # as all col is also sorted and we need to search the ele 
                                        # lesser than current one
                j-= 1
            elif matrix[i][j] < target:  # it means target will be present on the next rows
                                        # as all row  is also sorted and we need to search the 
                                        # ele greater than current one
                i+= 1
        return False

# 4th method: you can also start searching from bottom-left point
# and change the variable accordingly

# Note: Only in bove two cases we can make a decision where to move
# and in case if we start from other corner we won't be able to make
# decision where to move, there will be more than one possibility in other cases