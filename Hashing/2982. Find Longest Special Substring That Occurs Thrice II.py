# Logic:  Just count the substring ending at each char 'i' (a-z) for evert possible length(1-n).

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        # count = [[0 for j in range(n + 1)] for _ in range(26)]   # writing like this TLE
        count = [[0] * (n + 1) for _ in range(26)]

        # count[i][j] stores the count of special substrings of length j ending with the character at index i.
        ind = ord(s[0]) - ord('a')  # getting index of char
        count[ind][1] = 1
        pre = s[0]
        ans = -1

        length = 1
        for i in range(1, n):
            ind = ord(s[i]) - ord('a')
            if s[i] == pre:
                length += 1
                count[ind][length] += 1
            else:
                count[ind][1] += 1
                pre = s[i]
                length = 1
        
        for i in range(26):
            presum = 0
            for j in range(n, 0, -1):   # 'j': length 
                presum += count[i][j]
                if presum >= 3:
                    ans = max(ans , j)
                    break
        return ans


# Note=> But writing like : count = [[0 for j in range(n + 1)] for _ in range(26)]
# workimg for other people. Have to see this.
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/solutions/4482233/python3-two-pointer-count-substring-length/
    
# Have to analyse this properly.


        