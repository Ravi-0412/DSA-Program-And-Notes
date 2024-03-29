# time: O(n)
# https://leetcode.com/problems/single-number-iii/solutions/68900/accepted-c-java-o-n-time-o-1-space-easy-solution-with-detail-explanations/
# Read comment by "KaiPeng21' in above post along with original post

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x1= 0
        for num in nums:
            x1^= num
        # x1 will contain the xor of two number which is not repeating
        # now we have to find the two non repeating no.
        rightmost_set_bit= x1 & (-x1)  # at this position of set bit the no of ele with bit set must be odd and no ele with bit not set must be also odd only.
        
        # using this set bit at rightmost position we can divide the array into two parts and these two no should lie in these parts only.
        # both the non repeating no will lie in diff part as both of their bit can't be set at that position and xor in both the diff gr will the ans
        num1,num2= 0,0
        for i in range(len(nums)):
            # 1st: if bit set then and num will be >0 (and no of such number will be odd only) 
            if rightmost_set_bit & nums[i]: 
                num1^= nums[i]
            else:  # 2nd: if bit not set then and num will be ==0 (and no of such number will be odd only)
                num2^= nums[i]
        return [num1,num2]


# just another way of finding 2nd number
# logic: as x1 will contain xor of two non repeating number
# so after getting 1st number , we can do xor of 1st no with x1 to get the 2nd no
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x1= 0
        for num in nums:
            x1^= num
        rightmost_set_bit= x1 & (-x1)
        num1= 0
        for i in range(len(nums)):
            if rightmost_set_bit & nums[i]:
                num1^= nums[i]
        return [num1,num1^ x1]


# shorter version of above one
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:    
        x1= reduce(xor, nums)
        rightmost_set_bit= x1 & (x1-1) ^x1  # or x1 ^ (-x1)
        num1= reduce(xor,filter(lambda x: x & rightmost_set_bit, nums))
        return (num1, num1^ x1)


    