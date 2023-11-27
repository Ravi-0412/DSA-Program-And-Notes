# Just extension  of "525. Contiguous Array"

# Here we also need to take care of individual count of 'vowel' and consonant.
# FOr this also we will store index in a list w.r.t to count. [cnt: [indexes]]
# And we will check for each index if count of both is divisible by 'k' or not.

# For finding count in O(1), we will use prefix sum.

# Time : O(n^2)

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        prefix_v = [0] *(n + 1)
        prefix_c = [0]*(n + 1)
        for i in range(1, n + 1):
            if s[i-1] in "aeiou":
                prefix_v[i] = 1 + prefix_v[i-1]
            else:
                prefix_v[i] = prefix_v[i-1]
            if s[i -1] not in "aeiou":
                prefix_c[i] = 1 + prefix_c[i-1]
            else:
                prefix_c[i] = prefix_c[i-1]
    
        freq= collections.defaultdict(list)
        freq[0] = [-1]
        cnt = 0
        ans = 0
        for i in range(n):
            if s[i] in "aeiou":
                cnt += 1
            else:
                cnt -= 1
            if cnt in freq:
                l = len(freq)
                for j in freq[cnt]:
                    if ((prefix_v[i + 1] - prefix_v[j + 1]) * (prefix_c[i + 1] - prefix_c[j + 1])) % k == 0:
                        ans += 1     
            freq[cnt].append(i)
        return ans
