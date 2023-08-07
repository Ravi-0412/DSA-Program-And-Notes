# Observation: a)  when we will put all elements in an 1d array row wise then they will in increasing order only.
# b) It will be also sorted row wise and column wise.

# Because of two things given in Q : 1) Each row is sorted in non-decreasing order. 
# 2) The first integer of each row is greater than the last integer of the previous row.

# Method 1:
# Note vvi: Using the observation 'when we will put all elements in an 1d array row wise then they will in increasing order only'
# Also Here we can find the exact row of any element.But in Q :'240' we can't 

# so we can first find in which row element lies by comparing the 1st and last ele of that row.
# and then we can apply the binary search on that row.

# time: O(m+ log*n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col= len(matrix), len(matrix[0])
        for i in range(row):  # O(m)
            if matrix[i][0] <= target <= matrix[i][col-1]:
                return self.binary_search(matrix[i], target)
    
    def binary_search(self,arr,key):
        n= len(arr)
        low=0
        up= n-1
        while low< up:
            mid= low+ (up-low)//2
            if(arr[mid]>= key):    
                up= mid         
            else:
                low= mid+1
        return True if arr[low]== key else False


# method 2: little more optimised
# instead of searching in which row target lies linearly, we can use binary search.
# time: O(log*m + log*n)= O(log m*n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col= len(matrix), len(matrix[0])
        start, end= 0, row-1
        # finding the row in which our target belong using binary search.
        while start<=end:
            mid= start+ (end-start)//2
            if matrix[mid][0]<= target<= matrix[mid][col-1]:
                return self.binary_search(matrix[mid],target)
            elif matrix[mid][0]> target:  # if target is smaller than first ele also then search in the pre row.
                end= mid-1
            elif matrix[mid][col-1]< target:  # if target is greater than last ele also then search in the next row.
                start= mid+1
    
    def binary_search(self,arr,key):
        n= len(arr)
        low=0
        up= n-1
        while low< up:
            mid= low+ (up-low)//2
            if(arr[mid]>= key):    
                up= mid         # agar hmko target ele hi find karna h kisi smaller index pe then do this
            else:
                low= mid+1
        return True if arr[low]== key else False
    

# Method 3: 
# Using the observation row wise and column wise will be sorted also.
# Note: whenever you find row wise and column wise sorted apply this logic.

# it's is pretty nicee and easy method , it's approach is soo nicee
# logic: just start checking from top right corner and
# if not found then update the value of iterating variable properly
# where we can get the element just like binary search

# why we are not checking from (0,0)?
# ans: because every time we will not find the ele i.e for both the smaller and greater than case, we will have two choice for each.
# if target is smaller choices: left or up , if greater choices: right or down
# in this way we will have to traverse the each cell exactly one time.
# so time: O(n*m) only

# but when we traverse from top right then in unequal case we will have only one choice.
# if target is smaller choices: left , if greater choices: down

# Time: O(m+n)  , bigger than method '2'.

# Note Q: "240. Search a 2D Matrix II" is exactly same as this method only because :matrix is sorted row wise and column wise 

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


# Method 3: Using binary search directly
# How we can we think of this ?
# Ans: Using the observation 'when we will put all elements in an 1d array row wise then they will in increasing order only'.
# so we can treat this maxtrix as just 1D array.

# Time: O(log(m*n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col= len(matrix), len(matrix[0])
        start, end = 0, row * col - 1
        while start <= end:
            mid = start + (end - start)//2
            # getting coordinates of mid
            r = mid //col
            c = mid - r*col
            if matrix[r][c] == target:  # mid == target
                return True
            if matrix[r][c] > target:   # mid > target
                end = mid -1
            else:                       # mid < target
                start = mid + 1 
        return False
    

# Similar Q: "240. Search a 2D Matrix II"
# exactly same thing as 'method 2'.
# https://github.com/Ravi-0412/DSA-Program-And-Notes/blob/main/Binary_Search/240.%20Search%20a%202D%20Matrix%20II.py