# eaxctly same as 'longest substring with k distinct char'
# only change the condition i.e len(hashmap)<=k

class Solution:
    def longestKSubstr(self, s, k):
        freq= {}
        i, j= 0, 0
        ans= -1
        longest= ""  # will give any such string
        while j < len(s):
            freq[s[j]]= 1 + freq.get(s[j], 0)
            while len(freq) > k:
                freq[s[i]]-= 1
                if freq[s[i]]== 0:
                    del freq[s[i]]
                i+= 1
            ans= max(ans, j- i+ 1)  # for length we can update directly as here len(freq) <= k only.
            j+= 1
        return ans

