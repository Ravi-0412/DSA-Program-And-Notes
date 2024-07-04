# Exactly same Q as "132. Palindrome Partitioning II".

# Wrote excatly same logic.

#Note vvi: we don't have to check divisible of '5' , we have to check power of '5'.

# Note: 'Eading zero means' that substring should not start with '0'.
# my mistake: I was thinking there should be consecutive zeroes.

# Recursion + memoisation
# Time: O(n^2*log(5))
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        num = int(s, 2)
        if num == 0 :
            return -1

        def containsLeadingZero(j):
            if s[j] == '0':
                return True
            return False
        
        def isPowerOf5(num):
            while num >= 5:
                num /= 5
            # This means by keep on dividing 'num' by '5' we can bring the num to '1' means power of '1' else not.
            return num == 1
        
        # if num % 5 == 0:   # we don't have to check divisible of '5' , we have to check power of '5'.
        #     return 1
        if not containsLeadingZero(0) and isPowerOf5(num):
            return 1
        
        @lru_cache(None)
        def solve(i):
            if i == len(s):
                return 0
            if not containsLeadingZero(i) and isPowerOf5(int(s[i: ] , 2)):
                return 1
            ans = float('inf')
            for j in range(i , len(s)):
                num = int(s[i: j + 1], 2)
                if not containsLeadingZero(i) and isPowerOf5(num):
                    ans= min(ans, 1 +  solve(j + 1))
            return ans
        
        ans = solve(0)
        return ans if ans != float('inf') else -1


# Note: writing 'isPowerOf5' like this will error.
# Because for some power of '5' like 125, it will give power= '3.0000000000000004' hence will return False
# Don't know why. so better do  manually
        # def isPowerOf5(num):
        #     if num <= 0:
        #         return False
        #     power = math.log(num, 5)
        #     return power.is_integer()