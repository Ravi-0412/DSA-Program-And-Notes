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

# 2nd method : Best one(Template 2)
# minimum and maximum element will always in unsorted part
# and there will be only one sorted and unsorted part i.e 1) if left to mid is unsorted then mid to right will be unsorted (<=>)
# 2) if right to mid is unsorted then left to mid must be sorted(<=>)

class Solution:
    def findMin(self, nums: List[int]) -> int:              
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:   # means array from 'mid' to 'right' is unsorted
                left = mid + 1            # so minimum will lie in this part only i.e beyond mid

            else:      
            # here it will guarantee that array from 
            # mid to right is sorted and start to mid is unsorted and mid can also be minimum
                right = mid
        # after loop will fail , start and end will point to 
        # the same ele and that will be the minimum ele
        # because both are merging towards the index of min ele in each iteration
        return nums[left]


# very basic
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

# but this similar thought logic will work in 'finding the max element in rotated sorted array' 
# in finding the max the above logic will not work(reason same as this one only).
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end= 0, len(nums)-1
        while(start<end):
            mid= start+ (end-start)//2
            
            # if nums[start...mid] is unsorted means min ele will lie within this            
            if nums[start]> nums[mid]:
                end= mid        # as end can also be the minimum
    
            # here means nums[start...mid] is not unsorted 
            # then min will lie beyond mid  as min or max will always lie in unsorted part    ##* my mistake(again and again) :

            #  as array can be already sorted then it will not work
            # or if array become sorted from start to mid after changing start
        
            # means this condition doesnt fully guarantte that array beyond mid will be sorted

            else:
                start= mid+1
        return nums[start]


# max in rotated sorted array
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
