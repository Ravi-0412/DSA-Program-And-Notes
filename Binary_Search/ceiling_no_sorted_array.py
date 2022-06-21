# the same approach can be used to find th index of an element 
# if even not in the sorted array like: if element would be in the 
# array what would be its index
# we are just doing the same thing only i.e; finding the proper
# index of the given number

# 1st one 
# def ceiling_number(arr,num):
#     n= len(arr)
#     low= 0
#     high= n-1
#     # wherever this condition will fail(while loop) ,low will give the index of ceiling ele
#     # since when this loop will fail(low= high+1) and high was pointing to ceil 
#     # before this loop fail so now low will point to ceiling ele after the loop fail
#     # so arr[low] will become greater than the target element after loop will fail
#     # only this one is tricky like what ele will give the ceiling 
#     # other things are exactly same as we do in binary search
#     while(low<= high):
#         mid= int(low+ (high- low)/2)
#         if arr[mid]== num: 
#             return arr[mid]
#         elif arr[mid]< num: 
#             low= mid+ 1
#         else:
#             high= mid-1
#     return arr[low]


# Another method
def ceiling_number(arr,num):
    n,low, high= len(arr), 0, len(arr)-1
    ans= None
    while(low<= high):
        mid= low+ (high- low)//2
        if arr[mid]== num: 
            return arr[mid]
        elif arr[mid]< num:         
            low= mid+ 1
        else: # arr[mid]> num
            # this can be the possible ans 
            # so store this ans in the res variable
            ans= arr[mid]
            high= mid-1
    return ans


arr= [2,3,5,9,14,16,18]
print(ceiling_number(arr,14))
print(ceiling_number(arr,15))
print(ceiling_number(arr,4))
print(ceiling_number(arr,9))
print(ceiling_number(arr,8))
 
