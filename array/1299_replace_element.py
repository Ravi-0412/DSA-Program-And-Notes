# # 1st method(myslef): Brute force but haven't get accpeted due to time limit 
# # but gives correct output for all cases
# # this approach gives best case: o(n) when maximum element is last or 2nd last
# # for above case there is no need of for loop
# # and without 1st for loop , answer will be always correct, there is no need 
# # of 1st for loop. just replace 'k' with '0' in arr[k:n-1] in 2nd for loop
arr = [4,9,8,4,7]
n= len(arr)
#find the index of maximum element
k=arr.index(max(arr))
#arr[n-1]= -1  # writing here this will lead to wrong answer 
#replacing every element on left side of maximum value with maximum value
for i in range(0,k):
    if(i!= n-1):
        arr[i]= arr[k]
#replacing every element from maximum element to n-2(except last) 
# index element with greatest element on their right side
for num in arr[k:n-1]:
    # print(arr[k])
    greatest= -1000000
    j=k+1
    while(j<=n-1):
        if(arr[j]>=greatest):
            greatest= arr[j]
        j+= 1
    arr[k]= greatest
    k+= 1
arr[n-1]= -1
print(arr)


# # 2nd method(normal brute force): modified of 1st methode(commented lines)
# arr = [4,9,8,4,7]
# n= len(arr)
# k=0
# for num in arr[k:n-1]:
#     greatest= -1000000
#     j=k+1
#     while(j<=n-1):
#         if(arr[j]>=greatest):
#             greatest= arr[j]
#         j+= 1
#     arr[k]= greatest
#     k+= 1
# arr[n-1]= -1
# print(arr)

# # simple and straight foward brute force
# arr = [4,9,8,4,7]
# n= len(arr)
# for i in range(0,n-1):
#     greatest= -1000000
#     k= i+1
#     while(k<=n-1):
#         if(arr[k]>=greatest):
#             greatest=arr[k]
#         k+= 1
#     arr[i]= greatest
# arr[n-1]= -1
# print(arr)


# brute force but very concise and simple: Accepted 
# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         n= len(arr)
#         for i in range(n-1):
#             arr[i]= max(arr[i+1:])
#         arr[n-1] = -1
#         return arr


# 2nd method- time: o(n), space= o(n)
# logic: tranverse from right to left and store the element with max_ele_seen_so_far
# comparing the element while iterating
# and replace the iterating element with max_ele_seen_so_far

arr = [17,18,5,4,6,1]
n= len(arr)
max_ele_seen_so_far= arr[n-1]
arr[n-1]= -1
for i in range(n-2,-1,-1):
    temp=arr[i]
    arr[i]= max_ele_seen_so_far
    if(temp>=max_ele_seen_so_far):
        max_ele_seen_so_far= temp
print(arr)





