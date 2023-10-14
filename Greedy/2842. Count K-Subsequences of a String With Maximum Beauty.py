# Observation:
# 1) Same k length subsequence will have same 'beauty' score because char freq is mattering.
# so subsequenece arrangement won't matter only char in sub will matter.

# 2) for maximum beauty we will choose char with bigger frequency first.
# for this find the char with a freq and sort them in descending order of frequency.


# time complexity of the combination function, we can say that to generate valid combinations exactly once, 
# it will take O(n C r), and for getting r combinations, it is O(r)

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        counter = Counter(s)  # will store [char : freq]
        if len(counter) < k: return 0
        freq = Counter(counter.values())   # will store [char_freq : count_such_char]
        pairs = list(sorted(freq.items(), reverse=True))  # will store [char_freq : count_such_char] in descending order of char_freq
        res = 1
        for fc, no_char in pairs:
            if no_char <= k:
                # we can include all the char and after including them
                # their arrangment will matter i.e for 'no_char' no of places 
                # we will have 'fc' no of choices for each place so pow(fc, no_char)
                res = (res * pow(fc, no_char)) % mod
                k -= no_char
            else:
                # then we need to choose remaining 'k' char from 'no_char' and for 
                # remaining 'k' choices we will have 'fc' choices for each.
                res = (res * comb(no_char, k) * pow(fc, k)) % mod
                break  # we have filled all 'k' places so now return ans
        return res % mod