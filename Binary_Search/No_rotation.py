# no of rotation will be equal to index of minimum element in the array
# so just we have to find the minimum element index
# minimum/max ele will always exist in the unsorted part
class Solution:
    def findKRotation(self,arr,  n):
        start, end, n= 0, len(arr)-1, len(arr)
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