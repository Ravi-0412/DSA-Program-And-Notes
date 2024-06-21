# Logic: 1) if we can include all customers value when owner is not grumpy
# i.e when grumpy[i] == 0
# so first store sum of such value say 'initialSum'

# 2) Now question reduces to how many maximum '1' we can include to the initial sum.
# for this just we have to find the maximum sum of subarray(customers) having size 'minutes'
# when owner is grumpy i.e grumpy[i] == 1.

# just same as 'maximum sum of a subarray of size k'.

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        initialSum = 0
        for i in range(n):
            initialSum += customers[i] if grumpy[i] == 0 else 0
        curSum = 0   
        i, j = 0 , 0
        ans = initialSum
        while j < n:
            if grumpy[j] == 1:
                curSum += customers[j]
            if j - i + 1 >= minutes:
                ans = max(ans, initialSum + curSum)
                # remove the value of ith index if 'grumpy[i] == 1'
                if grumpy[i] == 1:
                    curSum -= customers[i]
                i += 1
            j += 1
        return ans
        