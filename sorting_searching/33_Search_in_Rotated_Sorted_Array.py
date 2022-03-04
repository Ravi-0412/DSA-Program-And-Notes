# 1st method: first finding the pivot and calling the binary search on left side (till pivot) 
# and right side after pivot

# this solution will not find the corect position of Pivot if array is already sorted
# but will give the corect output at final since we are appying on both the sorted 
# array only so whatever be the value returned by the pivot function we will get the correct value at the final

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n= len(nums)
#         pivot_index= self.BinarySearchPivot(nums,0,n-1)
#         # print(pivot_index)
#         left= self.BinarySearch(nums,target,0,pivot_index)
#         if left== -1:
#             right= self.BinarySearch(nums,target,pivot_index+1,n-1)
#             if right== -1:
#                 return -1
#             else:
#                 return right
#         return left
    
#     def BinarySearchPivot(self,arr,low,high):
#         start,end=low,high
#         while(start<end):
#             mid= start + (end-start)//2
            # pivot means index about which array is rotated
            # and this will be also equal to the index of max ele
            # after rotation
            # case 1: when the num will be greater then the next no
            # that will be the index of pivot ele 
            # OR  # case 2
            # ele at mid-1 > ele at mid then 'mid-1' will also give the index 
            #of pivot ele  as before(till pivot) and after pivot both the 
            # subarrays will be in ascending order
    
            # four cases will be there in total
            # case1:
            # if arr[mid]>arr[(mid+1)%(end+1)]:
            #     return mid
            
            # case 2: if mid- 1 ele is greater than  mid ele
            # elif mid>start and arr[mid]<arr[mid-1]:
            #     return mid-1  
            
            # case 3: when all ele after middle is smaller than start
            # it means pivot lie bw start and mid -1, since this means
            # we are in unsorted part and pivot and smallest ele  will always like in unsorted part
            # as there will only one sorted and unsorted part and unsorted part 
            # will give the index of maximum and minimum element

            # elif arr[mid] <= arr[start]:  
            #     end= mid-1
                
            # case 4: if ele at start is less than the middle
            # then pivot will exist after the middle 
            
        #     else:
        #         start= mid+1
        # return -1 # means array is not in correct format or already in ascending order 
   
    # def BinarySearch(self,arr,target,low,high):
    #     start,end= low,high
    #     while(start<= end):
    #         mid= start + (end-start)//2
    #         if arr[mid]== target:
    #             return mid
    #         elif arr[mid]<target:
    #             start= mid+1
    #         else:
    #             end= mid-1
    #     return -1


# method2: By recursion
#logic: just finding the sorted part and checking whether ele lies 
# in this or not .. if lies then call the binary search

def search(arr, target, low, high):
    start, end= low, high
    while(start<end):
        mid= start + (end-start)//2
        if arr[mid]== target:
            return mid

        elif arr[start] <= arr[mid]: # means array is sorted from start to mid
        # so we can check if target exist bw start and end
        # if it exists then we can apply binary search directly

            if arr[start] <=target<=arr[mid]:
                return search(arr, target,start, mid)
            else: # if not present then check in other part
                return search(arr, target,mid+1,end)

        # if above part is not sorted then it other part from mid+1 too end must be sorted
        # check if target lies in this range        
        elif arr[mid+1] <=target<=arr[end]:  # if lies call binary search
                return search(arr, target,mid+1,end)
        
        # if not lies from 'mid+1' to end then it must be before it
        else:
            return search(arr, target,start,mid)
    return -1

# arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
arr= [5,6,1,2,3,4]
key =  3
i = search(arr, key, 0, len(arr)-1)
if i != -1:
    print ("Index: % d"% i)
else:
    print ("Key not found")




        

        