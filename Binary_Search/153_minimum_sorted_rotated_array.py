# 1st method: Time: o(n), space: o(1)
# just traverse the array from left to right wherever 
# you will find the currnet ele greater than next element that 
# index will be the index of maximum ele and next will be the index 
# of minimum ele
# use '%' with next ele to compare because largest ele can be at 'n-1'
# then smallest will be at '(n-1+1)%n'
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n= len(nums)
        if n==1:
            return nums[0]
        for i in range(0,n):
            if nums[i]>nums[(i+1)%n]:
                return nums[(i+1)%n]


# not a good one
# just copy paste of video
# time: O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n= len(nums)
        pivot_index= self.BinarySearchPivot(nums,0,n-1)
        print(pivot_index)
        return nums[(pivot_index+1)%n]
    
    def BinarySearchPivot(self,arr,low,high):
        start,end=low,high
        while(start<end):
            mid= start + (end-start)//2
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
            if arr[mid]>arr[(mid+1)%(end+1)]:
                return mid
            
            # case 2: if mid- 1 ele is greater than  mid ele
            elif mid>start and arr[mid]<arr[mid-1]:
                return mid-1  
            
            # case 3: when all ele after middle is smaller than start
            # it means pivot lie bw start and mid -1, since this means
            # we are in unsorted part and pivot and smallest ele  will always like in unsorted part
            # as there will only one sorted and unsorted part and unsorted part 
            # will give the index of maximum and minimum element
            elif arr[mid] <= arr[start]:  
                end= mid-1
                
            # case 4: if ele at start is less than the middle
            # then pivot will exist after the middle 
            else:
                start= mid+1
        return -1 # means array is not in correct format or already in ascending order 




# 2nd method : Better one
# minimum and maximum element will always in unsorted part
# and there will be only one sorted and unsorted part

class Solution:
    def findMin(self, nums: List[int]) -> int:              
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:   # means array from 'mid' to 'right' is unsorted
                left = mid + 1            # so minimum will lie beyond mid

            else:      
            # here it will guarantee that array from 
            # mid to right is sorted and start to mid is unsorted and mid can also be minimum
                right = mid
        # after loop will fail , start and end will point to 
        # the same ele and that will be the minimum ele
        # because both are merging towards the index of min ele in each iteration
        return nums[left]


# myself got at revision time (18/06/2022)
# so good 
def findMin(self, arr):
    start, end, n= 0, len(arr)-1, len(arr)
    while start<= end:
        mid= start + (end-start)//2
        if arr[mid]> arr[(mid+1)%n]:  # this condition will only happen once in the whole array 
                                     # and (mid+1)% 1 will give the index of minimum element 
                                     # and mid will give the max ele
            return arr[(mid+1)%n]
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
        # so in this case simply return nums[0]
        else:
            return arr[0]


# below method will give the incorrect result
# my mistake

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end= 0, len(nums)-1
        while(start<end):
            mid= start+ (end-start)//2
            
            # if nums[start...mid] is unsorted means min ele will lie within this            
            if nums[start]>=nums[mid]:
                end= mid        # as end can also be the minimum
    
            # here means nums[start...mid] is not unsorted 
            # then min will lie beyond mid  as min or max will always lie in unsorted part    ##* my mistake(again and again) :

            #  as array can be already sorted then it will not work
            # or if array become sorted from start to mid after changing start
        
            # means this condition doesnt fully guarantte that array beyond mid 
            # will be unsoretd

            else:
                start= mid+1
        return nums[start]