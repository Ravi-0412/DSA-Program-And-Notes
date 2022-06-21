# the same approach can be used to find th index of an element 
# if even not in the sorted array like: if element would be in the 
# array what would be its index
# we are just doing the same thing only i.e; finding the proper
# index of the given number

# 1st method
def floor_number(arr,num):
    n= len(arr)
    low= 0
    high= n-1
    # wherever this condition(while loop) will fail , high will give the index of floor ele
    # since when this loop will fail(low= high+1) and high was pointing to ceil 
    # before this loop fail, so after loop fail high will be point to the floor 
    # of the target element
    # so arr[low] will become greater than the target element after loop will fail
    # only this one is tricky like what ele will give the floor 
    # other things are exactly same as we do in binary search
    while(low<= high):
        mid= int(low+ (high- low)/2)
        if arr[mid]== num: 
            return arr[mid]
        elif arr[mid]< num: 
            low= mid+ 1
        else:
            high= mid-1
    return arr[high]

# 2nd method
# def floor_number(arr,num):
#     n,low, high= len(arr), 0, len(arr)-1
#     ans= None
#     while(low<= high):
#         mid= low+ (high- low)//2
#         if arr[mid]== num: 
#             return arr[mid]
#         elif arr[mid]< num: # this can be the possible ans 
#             # so store this ans in the res variable
#             ans= arr[mid]
#             low= mid+ 1
#         else:
#             high= mid-1
#     return ans

arr= [2,3,5,9,14,16,18]
print(floor_number(arr,14))
print(floor_number(arr,15))
print(floor_number(arr,4))
print(floor_number(arr,9))
print(floor_number(arr,8))
 
