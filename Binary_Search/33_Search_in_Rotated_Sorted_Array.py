# 1st method: first finding the index of min ele and calling the binary search on left side (before pivot) 
# and right side from pivot till end
# ele from index 0 till before index of  min ele will be sorted in ascending order and
# ele from index of min ele till last index will be sorted in ascending order
# so just apply binary search on both the parts after finding the index of pivot ele

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        # 1st find the index of minimum ele(here pivot index) 
        pivot_index= self.BinarySearchPivot(nums,0,n-1)
        # now apply binry search from index 0 before index of minimum ele
        left= self.BinarySearch(nums,target,0,pivot_index-1)
        if left== -1:
            # if not found in left side 
            # apply binary search from index of min ele till last index
            right= self.BinarySearch(nums,target,pivot_index,n-1)
            if right== -1:
                return -1
            else:
                return right
        return left
    
    def BinarySearchPivot(self,arr,start, end):
        n= len(arr)
        while start<= end:
            mid= start + (end-start)//2
            if arr[mid]> arr[(mid+1)%n]:  # this condition will only happen once in the whole array 
                                         # and (mid+1)% 1 will give the index of minimum element
                return (mid+1)%n
            # if above condition not found then update the start and end in the unsorted part
            # and there are two chances of unsorted part
            
            # case 1: means ele will be present till mid and mid can also be the minimum
            # so update end in this case
            elif arr[mid] < arr[start]: 
                end= mid

            # case 2: means ele will be present after mid till end      
            # so update 'start' in this case     
            elif arr[mid] > arr[end]:
                start= mid +1
            # if no such condition found then array is sorted in ascending order
            # so in this case simply return 0
            else:
                return 0
            
    def BinarySearch(self,arr,target,low,high):
        start,end= low,high
        while(start<= end):
            mid= start + (end-start)//2
            if arr[mid]== target:
                return mid
            elif arr[mid]<target:
                start= mid+1
            else:
                end= mid-1
        return -1


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
        # so we can check if target exist bw start and mid
        # if it exists then we can apply binary search directly

            if arr[start] <=target<=arr[mid]:
                return search(arr, target,start, mid)
            else: # if not present then check in other part
                return search(arr, target,mid+1,end)

        # if above part is not sorted then it other part from mid+1 to end must be sorted
        # check if target lies in this range        
        elif arr[mid+1] <=target<=arr[end]:  # if lies call binary search
                return search(arr, target,mid+1,end)
        
        # if not lies from 'mid+1' to end then it must be before it
        else: # you can write this else ij above elif jujst like the 1st one 
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




        

        