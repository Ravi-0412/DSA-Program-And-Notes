# method 1: just check if any element on right side 
# is greater than the ele on its lfet side
# submitted on GFG
# class Solution:
#     def arraySortedOrNot(self, arr, n):
#         for i in range(n-1):
#             if arr[i]>arr[i+1]:
#                 return False
#         return True


#another way of writing recursion function(better one)
# def sortedOrNot(arr, index):
#     if index== len(arr)-1:  # if index is the index of last ele of the array then True
#                             # as last ele will be always sorted
#         return True   
#      # check the value of next ele and call the function for next index
#     return (arr[index]<=arr[index+1]) and sortedOrNot(arr,index+1)
# # arr= [2,4,4,5,6,7,8]
# arr= [1,5,3,9,10,54]
# # print(sortedOrNot(arr,0))


# another method: best one
def sorted(arr):
    if len(arr)==1:
        return True
    return arr[0]<=arr[1] and sorted(arr[1:])

# arr1= [2,4,4,5,6,7]
# arr1= [1,5,3,9,10,54]
# print(sorted(arr1))



