# 1st method is sorting
# since you have arrange the ele in ascending order basically so sorting will always a solution
# time: O(nlogn)


# 2nd method:
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



# 3rd method(using double pointer)
# move the array 0 at front ,1 in the middle and 2 at the last
# final goal is to make this 'low' and 'high' pointer points to 
# 1st and last index of all consecutive 1's respectively
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # it can't be done by two pointer so we have to take another pointer also for 
        # handling the cases like after swapping if low points to 1 and there is more '0' 
        # in the middle, this type of cases can't be handled by the two pointer e.g :[2,0,2,1,1,1,0,1,1]
        # current will max point till the last '1', the main aim of curr is to put '0' at 
        # start and '2' at the end  and '1' at the mid so 'curr' will never go beyond the 'high'
        current,low=0,0
        high= len(nums)-1
        # after high all the elements will be two only and before 'low' all the 
        # ele will be '0' only
        while(current<=high):
            if nums[current]== 0:
                # swap it with nums[low] as before low all will be '0' only
                nums[current],nums[low]= nums[low], nums[current] 
                low+= 1
                current+= 1
            elif nums[current]== 1:
                # don't swap as main aim to curr to put '1' in the middle, simply incr curr by 1
                current+= 1
            # if nums[current] ==2:
            else:
                # # swap it with nums[high] as after high all will be '2' only
                nums[current], nums[high]= nums[high], nums[current]
                high-= 1
                # don't move the current since after swapping in this
                # cases current can contain 1 also
        return nums

