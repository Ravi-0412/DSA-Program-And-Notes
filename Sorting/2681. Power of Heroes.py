# logic: https://leetcode.com/problems/power-of-heroes/solutions/3520202/c-java-python3-explanation-and-stepping-through-the-code/?orderBy=most_votes

# write the logic in notes.

# time: O(n*logn)

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        n= len(nums)
        mod= 10**9 + 7
        nums.sort()
        s= [0]*n
        ans= nums[0]**3  # for index '0'
        for i in range(1, n):
            ans+= nums[i]**3 
            s[i]= nums[i-1] + 2*s[i-1]
            ans= (ans + (nums[i]**2) * s[i]) % mod
        return ans
