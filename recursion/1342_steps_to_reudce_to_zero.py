# method1(submitted on leetcode)
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans= 0
        if num==0:
            return 0
        # if no is even
        if num%2==0:
            ans+= 1
            num= num//2
            smallAns= Solution().numberOfSteps(num)
            ans+= smallAns
        else: # if no is odd
            ans+= 1
            num= num-1
            smallAns= Solution().numberOfSteps(num)
            ans+= smallAns
        return ans


# concise way of writing the above code
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num==0:
            return 0
        if num%2== 0:  # if even
            return 1+ self.numberOfSteps(num//2)
        else:
            return 1+ self.numberOfSteps(num-1)
