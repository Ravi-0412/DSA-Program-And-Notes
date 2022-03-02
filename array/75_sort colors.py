# 1st method:
# just count the no of 0,1,2 & put the 0 first then 1 then 2 according to the the count value
# 0 will come till index 'count0-1' and same for others
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0= nums.count(0)
        count1= nums.count(1)
        count2= nums.count(2)
        for i in range(len(nums)):
            if(i<count0):
                nums[i]= 0
            if(i>= count0 and i<count0+count1):
                nums[i]= 1
            if(i>=count0+count1 and i<len(nums)):
                nums[i]= 2
        return nums


# 2nd method(using double pointer)
# move the array 0 at front ,1 in the middle and 2 at the last
# final goal is to make this 'low' and 'high' pointer points to 
# 1st and last index of all consecutive 1's respectively
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current,low=0,0
        high= len(nums)-1
        while(current<=high):
            # trying to move the 0 to the start of the array
            # means we have seen one more 0 and in search of another 0
            if nums[current]== 0:
                nums[current],nums[low]= nums[low], nums[current] 
                low+= 1
                current+= 1
            # trying to move the 1 to the middle of the array
            # means we have seen one more 1 and in search of another one 
            elif nums[current]== 1:
                current+= 1
            # moving the 2 to the end of the array
            else:
                nums[current], nums[high]= nums[high], nums[current]
                high-= 1
                # don't move the current since after swapping in above all 
                # cases current can contain 0 and 1 
        return nums

