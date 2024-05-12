# lOGIC: We have to select maximum number only . for this sort in reverse order.
# But if we are selecting  any number as ith number then it's value = nums[i] - i

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        ans = 0
        for i in range(k):
            ans += max(0, happiness[i] - i)
        return ans
