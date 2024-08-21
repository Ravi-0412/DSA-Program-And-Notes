# Logic:  
# Since we have to include all the given number in permutation.
# Logic: This Q reduces to 'Find the next greater number than the given number only using the digit of the given number'.
# and for finding this we can start from righmost side.

# Note: No need to traverse whole number we only need to rearrange numbers from index 'i -1' to last index such that
# nums[i] > nums[i -1] i.e find the 1st index 'i-1' which breaks the ascending order rule from last.
# it means we have got a smaller number at 'i-1' so we can rearrange ele from index 'i-1' to last index to get
# our ans i.e next greater number.

# Steps:
# 1) 
# i.e find 'i-1' such that nums[i] > nums[i - 1]  then ,
# (from index 'i' to last ele, element will be in descending order.

# Now we have to rearrange all numbers from 'i-1' to last to get the ans.
# Numbers before 'i-1' won't matter in ans. Replacing with any number before 'i-1' will give larger number than expected.

# 2) We will have to bring 1st number greater than nums[i-1] from right side i.e from index 'i' to last
# at index 'i-1'.
# So find the 1st element greater than 'nums[i-1]' from right.
# ie. we have to search j' from last such that nums[j] > nums[i-1] 

# 3) Now we have found correct number for index 'i-1' which is at index 'j'.
# so swap(i-1, j)

# 4) After swapping, number from index 'i' to last will be in descending order only
# So to get minimum number value from index 'i' to last, we will have to reverse array from index 'i' to last.

# 5) Finally you will get the ans.

# For visualisation take e.g : [9, 4, 8, 3, 6, 5, 2, 1]
# i = 4, j = 5

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n= len(nums)
        i= n- 1  # will point to the index such that nums[i] < nums[i-1] from the right.
        j= n- 1  # will point to the index such that nums[j] > nums[i -1] from the right.

        # 1) first find 'i'.
        while i> 0 and nums[i-1] >= nums[i]:
            i-= 1
        if i== 0:
            # Means number given number is the largest number so just return the smallest number
            return nums.reverse()
        # 2)  find 'j'.
        while nums[i-1] >= nums[j]:
            j-= 1
        # 3) now swap the 'j' and 'i-1'.
        nums[j], nums[i-1]= nums[i-1], nums[j]
        # 4) reverse the arr from index 'i' to last.
        # return nums[:i] + (nums[i+1:])[::-1]   # this will not work. because 'nums[:i]: create another array but nums[i:] modifies the same arr'.
        nums[i:]= nums[i:][::-1]


# Java code:
"""
class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int i = n -1, j = n-1 ;
        while(i > 0 && nums[i -1] >= nums[i])
            i --;
        if(i == 0) {
            reverse(nums, 0, n-1);
            return ;
        }
        while(nums[i-1] >= nums[j]) 
            j --;
        swap(nums, i-1, j);
        reverse(nums, i , n - 1);
    }

    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public void reverse(int[] nums, int i, int j){
        while(i < j) {
            swap(nums, i, j) ;
            i ++;
            j --;
        }
    }
}
"""