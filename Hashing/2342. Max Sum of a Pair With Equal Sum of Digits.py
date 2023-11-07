# Logic: for a sum_of_digit store the maximum and second maximum number.

# Time = space = O(n)

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def sumOfDigit(num):
            sum = 0
            while num:
                num, r = divmod(num, 10)
                sum += r
            return sum

        digitSum = {}
        for num in nums:
            sum = sumOfDigit(num)
            if sum in digitSum:
                first , second = digitSum[sum]
                if num > first:
                    second , first = first , num
                elif num > second:
                    second = num
                digitSum[sum] = [first, second]
            else:
                digitSum[sum] = [num, 0]

        ans = -1
        for key, values in digitSum.items():
            num1, num2 = values
            if num2 != 0:
                ans = max(ans, num1 + num2)
        return ans 


# Shorter way of writing above logic.
# Logic: Since we need maxSum so we can store only maxNo corresponding to a digitSum.
# No need to store the second_max_no . We can use current number to get the ans with already stored number.

# Just like Two sum. Just instead of 'num' as key, we will use 'sum_of_digit'.

# Time = space= O(n)

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def sumOfDigit(num):
            sum = 0
            while num:
                num, r = divmod(num, 10)
                sum += r
            return sum

        digitSum = {}  # [digit_sum : max_num]
        ans = -1
        for num in nums:
            sum = sumOfDigit(num)
            if sum in digitSum:
                ans = max(ans, digitSum[sum] + num)
                digitSum[sum] = max(digitSum[sum], num)
            else:
                digitSum[sum] = num
        return ans

# Note: When you have to find largest/smallest pair among all possible then apply the same above logic.

# Note vvi: Whenver you are asked to 'find pair' or 'count pairs' apply two sum logic.
# in case of 'pair count' store 'frequency' as value.

