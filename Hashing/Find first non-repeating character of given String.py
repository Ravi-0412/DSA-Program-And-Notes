# 1) count the freq of each char
# 2) then check the count of each char of = 1 then return that index.
# because we are checking from start only so if 1st time we will get freq= 1 that will be ans.

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq= Counter(s)
        for i, c in enumerate(s):
            if freq[c]== 1:
                return i
        return -1

