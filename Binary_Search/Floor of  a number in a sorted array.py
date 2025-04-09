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
    while(low<= high):
        mid= int(low+ (high- low)/2)
        if arr[mid]== num: 
            return arr[mid]
        elif arr[mid]< num: 
            low= mid+ 1
        else:
            high= mid-1
    return arr[high]

arr= [2,3,5,9,14,16,18]
print(floor_number(arr,14))
print(floor_number(arr,15))
print(floor_number(arr,4))
print(floor_number(arr,9))
print(floor_number(arr,8))


# cieling and floor in same array. 
# just was checking whether my logic works or not so sorted.
# but it can be done in O(n) only.
# submitted on gfg
# https://practice.geeksforgeeks.org/problems/ceil-the-floor2802/1
def getFloorAndCeil(arr, n, x):
    arr.sort()
    low=0
    up= n-1
    ans= []
    while(low<= up):
        mid= low+ (up-low)//2
        if arr[mid]== x:
            return arr[mid], arr[mid]
        elif(arr[mid]> x):  # mid ans deta but mid hi bda h to ab kahan 'key' hmko mil sakta h. mid se phle
            up= mid-1
        elif(arr[mid]<x):
            low= mid+1
    if up>= 0:
        ans.append(arr[up])
    if up< 0:
        ans.append(-1)
    if  low<n:
        ans.append(arr[low])
    if low>= n:
        ans.append(-1)
    return ans
