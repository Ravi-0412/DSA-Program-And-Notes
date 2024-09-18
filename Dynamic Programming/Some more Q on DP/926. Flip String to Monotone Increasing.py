# Just exact same q as: "926. Flip String to Monotone Increasing"
# Time = O(n). space = O(1)

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cnt1 = 0
        res = 0
        for x in s:
            if x == '0':
                res = min(res + 1, cnt1)
            elif x == '1':
                 # Fine for 'b' in the tail
                cnt1 += 1
        return res
