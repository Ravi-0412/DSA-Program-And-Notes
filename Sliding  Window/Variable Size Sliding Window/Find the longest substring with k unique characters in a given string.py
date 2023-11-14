# for max ans, longest ke liye jitna se jitna char repeat karne chahiye with 

# Note: To check the number of unique char at any point of time we will use hashmap.
# len(ahshmap): will tell no of unique char at any point of time.

# time: O(n)= space 

# shorter way and concise way.
# Note: Try to solve every variable sliding window problem like this only.
# After seeing every char check for valid substring and update ans.

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
            if len(freq)== k and j - i + 1 > ans:
                longest= s[i: j +1]
                ans= max(ans, j- i+ 1)
            j+= 1
        return ans

    


