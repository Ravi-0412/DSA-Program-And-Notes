# method 1: 
# will only work if there is no zero.

# logic: We just need to take product of all numbers & also keep tracking the largest negative number.
# Check if the product is negative then devide it by the largest negative number. 
# ( Basically we want to remove the largest negative number or you can say smallest abs valued negative number)

# time: O(n)

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mul= 1
        largestNegative= -9 # will give the largest negative number considering sign i.e -1 > -2
        for num in nums:
            if num < 0:
                largestNegative= max(largestNegative, num)
            mul*= num
        if mul >= 0:
            return mul
        # if negative then remove the largest negtaive ele from the multiplication.
        return abs(mul) // abs(largestNegative)


# method 2:
# Time: O(n)

# Handling all the corner cases 
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mul= 1  # will store the multiplication of whole array except zero.
        largest= max(nums) # will give the max ele in whole array.
        negativeCount= 0
        largestNegative= -9 # will give the largest negative number considering sign i.e -1 > -2
        for num in nums:
            if num < 0:
                largestNegative= max(largestNegative, num)
                negativeCount+= 1
            if num != 0:
                # for handling the cases when there is '0' with len(arr) >= 2.
                mul*= num
        if largest == 0 and negativeCount <= 1:
            # for handling the cases like [0], [0, -1]
            return 0
        if mul > 0:
            return mul
        # if negative then remove the largest negtaive ele from the multiplication.
        return abs(mul) // abs(largestNegative)
