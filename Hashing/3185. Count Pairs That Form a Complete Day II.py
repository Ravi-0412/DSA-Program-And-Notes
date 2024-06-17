# Logic: Find the number of pairs divisible by 'k' where k = 24.

# How to do?
# for each number 'nums[i]' how can we get the pairs ?
# => find the remainder 'nums[i] % k' then number we will need to make sum divisble by 'k' i.e needed = '(k - remainder) % k' 
# so add the count of 'needed' for each number.

# and for 'remainder' increase the count.

# Tim : O(n)

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        k = 24
        n = len(hours)
        count = collections.defaultdict(int)
        ans = 0
        for i in range(n):
            remainder = hours[i] % k
            needed = (k - remainder) % k
            ans += count[needed]
            count[remainder] += 1
        return ans