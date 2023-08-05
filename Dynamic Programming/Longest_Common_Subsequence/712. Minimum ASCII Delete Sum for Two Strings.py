# Exactly same as : "583. Delete Operation for Two Strings".
# Just we need to add the 'Ascii value' of char we are deleting.

# Exactly written same code of above Q only.

# Time: O(n^2)

class Solution:
    @lru_cache(None)
    def minimumDeleteSum(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            sum = 0
            if word1:
                for c in word1:
                    sum += ord(c)
                    
            if word2:
                for c in word2:
                    sum += ord(c)
            return sum
        ans = 0
        if word1[0] == word2[0]:
            ans = self.minimumDeleteSum(word1[1 : ], word2[1: ])
        else:
            ans = min(ord(word1[0]) + self.minimumDeleteSum(word1[1 : ], word2), ord(word2[0]) + self.minimumDeleteSum(word1, word2[1: ]))
        return ans
    
    