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
        # both the non repeating no will lie in diff part as both can't have their bit set at that position and 
        # xor in both the diff gr will the ans.
        num1,num2= 0,0
        for i in range(len(nums)):
            # 1st: if bit set then and num will be >0 (and no of such number will be odd only) 
            if rightmost_set_bit & nums[i]: 
                num1^= nums[i]
            else:  # 2nd: if bit not set then and num will be ==0 (and no of such number will be odd only)
                num2^= nums[i]
        return [num1,num2]

# Method 2 :
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
    

# How to solve these type of question (finding two number):
# 1) Think how we can get xor of these two number.
# so 1st find the xor such that xor = xor of two number we have to find.
# 2) Now we have to separate two numbers from above 'xor'
# a) for this 1st find the rightmost_set_bit of above xor (x  & -x).
# b) Now take two set(variable) with initial value = 0 , where each set will store one ans.
# VVI: c) Repeat the same step from start which we had done to get 'xor' and 
# and keep updating the set1 and set after checking the condition : rightmost_set_bit & nums[i]
# d) At last return both numbers

# e.g: In this question , we got x1 = xor of both numbers by 'taking xor of whole array'.
# so to get answer again traverse whole array and update both sets(num1, num2).

# Related Question:
# 1) Repeat and Missing Number Array

# Logic: Here we will get x1 = xor of both answer number by:
# a) Traversing whole array 
# b) Then traversing numbers from '1' to 'n'.
# so to get answer again traverse both array(that we traversed initially) and update both the set 
# after checking condition. 'rightmost_set_bit & 1'.