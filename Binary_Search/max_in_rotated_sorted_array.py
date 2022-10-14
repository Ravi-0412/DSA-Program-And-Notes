
# 1st method: time: O(logn), space: O(1)
# def findMax(arr):
#     start, end, n= 0, len(arr)-1, len(arr)
#     while start<= end:
#         mid= start + (end-start)//2
#         if arr[mid]> arr[(mid+1)%n]:  # this condition will only happen once in the whole array 
#                                      # and (mid+1)% 1 will give the index of minimum element
#             return arr[mid]
#         # if above condition not found then update the start and end in the unsorted part
#         # and there are two chances of unsorted part
        
#         # case 1: means ele will be present before mid 
#         # so update end in this case
#         elif arr[mid] < arr[start]: 
#             end= mid -1 

#         # case 2: means ele will be present from mid till end and mid can also be the max     
#         # so update 'start' in this case     
#         elif arr[mid] > arr[end]:
#             start= mid 
#         # if no such condition found then array is sorted in ascending order
#         # so in this case simply return nums[n-1]
#         else:
#             return arr[n-1]


# 2nd method: very better and concise wasy of above logic only
# logic: max and min will always lie in the unsorted part
# time: O(logn), space: O(1)

def findMax(nums):              
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) // 2
    
        if nums[left] >nums[mid]:   # means array from 'left' to 'mid' is unsorted
            right = mid-1            # so max will lie before mid 

        else:      # here it will guarantee that array from left to mid is sorted and 
        # mid to right is unsorted and mid can also be the max
        # so max will lie in this range only 
            left= mid
    # after loop will fail , start and end will point to 
    # the same ele and that will be the maximum ele
    # because both are merging towards the index of max ele in each iteration
    
    return nums[left]


# nums= [3,4,5,1,2]
# nums= [7,8,9,1,2,3]
# nums= [6,7,8,9,1,2]
# nums= [8,9,1,2]
# nums= [6,8,9,10,3,4,5]
# nums= [9,1,2,3]

# nums= [6,7,8,9,1]
# nums= [5,6,7,8,9,1,2,3,4]
# nums= [1,2,3,4]


# print(findMax(nums))

