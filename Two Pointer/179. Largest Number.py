# just keep swapping to bring largest number at first place , 2nd place and so on by comparing the string concatenation value of both.

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # first convert nums values into string since we want number to be greater after string concatenation not by actual addition.
        # Because we have to sort according the first digit of every number.
        nums= list(map(str, nums))
        # for i, n in enumerate(nums):   # this will also convert into string.
        #     nums[i]= str(n)
        
        # now check from each index sum of two number at a time,if next number(larger index) is greater then swap both
        # so finally after one iteration we will get the largest number at 1st index and so on.
        for i in range(len(nums) -1):
            j= i+ 1  # j will always start from 'i+1'.
            while j < len(nums):
                if nums[j] + nums[i] > nums[i] + nums[j]:
                    nums[j], nums[i]= nums[i], nums[j]
                j+= 1
        return str(int("".join(nums)))   # first all will get converted into integer then into list
        # return "".join(nums)   # This will give error in case when there will be all '0' in the list.
        # like [0,0,0]  then it will return "000" but we only need to return "0".
        # so first converted into int(to make a single '0') then into list.
