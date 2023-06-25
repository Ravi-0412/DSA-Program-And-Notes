# Logic: Don't worry about forming the actual string.
# Just find how many maximum char we can delete.
# vvi: what does matter is only first and the last character.

# first is the first character of the actual concatenated string
# last is the last character of the actual concatenated string
# index is the index of the word in the array words which we are processing.

# We can only delete either last== w[0] or w[-1] == first & we have to take maximum of both. 

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        @lru_cache(None)
        def solve(ind, first, last):  
            if ind >= len(words):
                return 0
            w= words[ind]
            # we have two choices for merging i.e join(x, y) or join(y, x) 
            # And we will take where we can delete the maximum
            return max((last == w[0]) + solve(ind + 1, first , w[-1]) , (w[-1] == first) + solve(ind + 1, w[0] , last))
        

        max_delete = solve(1, words[0][0], words[0][-1])  # we will start checking from index '1'.
        return len("".join(words)) - max_delete     # total length of words - max_delete