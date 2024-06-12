# 1st method is sorting
# since you have to arrange the ele in ascending order basically so sorting will always a solution
# time: O(nlogn)


# 2nd method:
# just count the no of 0,1,2 in an list of size '3' then store ans according to count.

# 3rd method(using double pointer): time=O(N),Space: O(1).. Q is made on this approach only

# it can't be done by two pointer so we have to take another pointer also for 
# handling the cases like after swapping if low points to 1 and there is more '0' in the middle
# this type of cases can't be handled by the two pointer e.g :[2,0,2,1,1,1,0,1,1]

# So we need one more pointer to put all '1' in middle automatically by swapping '0' and '2'.

# move the array 0 at front ,1 in the middle and 2 at the last
# final goal is to make this 'low' and 'high' pointer points to 
# 1st and last index of all consecutive 1's respectively.
# before low all will be zero and low will point to the first one
# after high all will be 2, high will point to the last one at last.

# This is known as  " dutch partitioning algorithm".

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        

        # current will max point till the last '1',  so 'curr' will never go beyond the 'high'.
        current,low=0,0
        high= len(nums)-1
        # after high all the elements will be two only and before 'low' all the 
        # ele will be '0' only
        while(current<=high):
            if nums[current]== 0:
                # swap it with nums[low] as low will be pointing to 1st one i.e before low all are '0'.
                nums[current],nums[low]= nums[low], nums[current] 
                low+= 1
                current+= 1 # we have made one correct move.
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

# Note vvi: keep above logic in mind, may be helpful in other problems also

# Also do by other method in sheet.

