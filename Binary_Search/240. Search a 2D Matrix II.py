# 1st method: Brute force O(N^2)

# 2nd method: just apply binary search in each row
# time: O(mlogn)


# 3rd method: 
# it's is pretty nicee and easy problem , it's approach is soo nicee
# logic: just start checking from top right corner and
# if not found then update the value of iterating variable properly
# where we can get the element just like binary search
# Time: O(m+n)

# why we are not checking from (0,0)?
# ans: because every time we will not find the ele i.e for both the smaller and greater than case, we will have two choice for each.
# in this way we will have to traverse the each cell exactly one time.
# so time: O(n*m) only

# but when we traverse from top right then in unequal case we will have only one choice.
# key greater then check in next row and if smaller check in pre col.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col= len(matrix), len(matrix[0])
        down, left= 0 , col -1
        while down< row and left >=0:  # 'i' will always go down(max till row-1) and 'j' will always go left max till '0'
            # if found then return True
            if matrix[down][left]== target:
                return True
            elif matrix[down][left] > target: # it means target will be present on the previous col
                                        # as all col is also sorted and we need to search the ele 
                                        # lesser than current one
                left-= 1
            elif matrix[down][left] < target:  # it means target will be present on the next rows
                                        # as all row  is also sorted and we need to search the 
                                        # ele greater than current one
                down+= 1
        return False


# 4th method: you can also start searching from bottom-left point
# and change the variable accordingly

# Note: Only in bove two cases we can make a decision where to move
# and in case if we start from other corner we won't be able to make
# decision where to move, there will be more than one possibility in other cases