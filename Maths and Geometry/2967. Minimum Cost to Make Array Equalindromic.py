# In this type of question where we have to make all element same and we told to find minimum cost
# We have to think of median.

# So question reduces to "find nearest palindrome to median"

class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        def checkPalindrome(num):
            rev , temp = 0, num
            while temp:
                r = temp % 10
                rev = rev * 10 + r
                temp //= 10
            return rev == num
        
        def palindromeLeft(num):
            while checkPalindrome(num) == False:
                num -= 1
            return num
        
        def palindromeRight(num):
            while checkPalindrome(num) == False:
                num += 1
            return num
        
        def findCost(x):
            ans = 0
            for num in nums:
                ans += abs(num - x)
            return ans

        n = len(nums)
        nums.sort()
        # find median
        median = nums[n//2] if n % 2 else (nums[n //2 - 1] + nums[n // 2]) // 2
    
        # finding 1st number to the left of median(including) which is a palindromic number
        left = palindromeLeft(median)
        # finding 1st number to the right of median(including) which is a palindromic number
        right = palindromeRight(median)
        
        # find the cost from 'left' and 'right' palindromic and take minimum of both.
        ans = min(findCost(left) , findCost(right))
        return ans
        