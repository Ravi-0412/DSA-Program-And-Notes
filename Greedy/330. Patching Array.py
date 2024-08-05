# Logic: 
"""
Think about this example: nums = [1, 2, 3, 9]. We naturally want to iterate through nums from left to right
and see what we would discover. After we encountered 1, we know 1...1 is patched completely. 
After encountered 2, we know 1...3 (1+2) is patched completely. 
After we encountered 3, we know 1...6 (1+2+3) is patched completely. 
After we encountered 9, the smallest number we can get is 9. 
So we must patch a new number here so that we don't miss 7, 8. To have 7, the numbers we can patch is 1, 2, 3 ... 7.
Any number greater than 7 won't help here. Patching 8 will not help you get 7. 
So we have 7 numbers (1...7) to choose from. 
I hope you can see number 7 works best here because if we chose number 7, 
we can move all the way up to 1+2+3+7 = 13. (1...13 is patched completely) 
and it makes us reach 'target' as quickly as possible. 
After we patched 7 and reach 13, we can consider last element 9 in nums. 
Having 9 makes us reach 13+9 = 22, which means 1...22 is completely patched. 
If we still did't reach n, we can then patch 23, which makes 1...45 (22+23) completely patched. 
We continue until we reach 'target'.

Note: We track the next missing number and if we have not reached the next missing number
then we will add missing number else we will add current element nums[i].
"""
class Solution:
    def minPatches(self, coins: List[int], target: int) -> int:
        n = len(coins)
        coins.sort()
        miss = 1
        ans = 0
        i = 0
        while miss <= target:
            if i < n and miss >= coins[i]:
                # if missing number is already reachable then add current number then next missing = miss + coins[i]
                miss += coins[i] 
                i += 1
            else:
                # add missing number then next miss = miss + miss
                miss += miss
                ans += 1   # increment ans
                # i += 1  # we can't increment 'i' here . will give more ans than expected.
        return ans


# Similar question:
# 1) 2952. Minimum Number of Coins to be Added
# Exact same question just sort and apply same logic.