# difference between this Q and "240. search in 2D matrix" is that 
# here all elements will be surely in ascending order combining whole as row wise or column wise.

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
# time: O(log*m + log*n)
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


