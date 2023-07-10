# method 1: Brute Force
# for each substring find the variance.
# Variance = 'max(frequency) of a char' - 'min(frequency) of a char' 
# time:O(n^3)



# optimised one.
# The basic idea is same: pick 2 chars, check the results for these particular 2 chars.
# Totaly less than 300 ways of picking 2 chars, not big deal.
# When 2 chars a,b are decided, we go through s, +1 when see 'a', -1 when see 'b'. Then, 
# The question becomes:
# -1, +1, +1, -1, +1, ...
# What is the maximum subarray?

# Typical Kadanes algorithm, which is essentially DP
# dp[i] is max subarray ending at i. We have dp[i] = max(dp[i-1],0) + s[i], which means if dp[i-1] <0, 
# we start a new subarray, if not, we connect current value to previous subarray.
# In this quesiton, we also need to ensure the subarray contains both 'a' and 'b', which can be done using has_a and has_b flag.
# time: O((26*25)/2 *n), n= len(s)

# NOte: Analyse this method properly

class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        chars = list(set(s))
		
		# Loop through each pari of (c1, c2)
        for i in range(len(chars)):
            for j in range(i+1, len(chars)):
                c1, c2 = chars[i], chars[j]
				
				# keep track of count(c1) - count(c2) 
                diff = 0 
				
				# max and min of diff
				# result should be maximum of (diff - min_diff, max_diff - diff)
				# e.g. "baabaa", at index = 0, min_diff = -1. when index = 5, diff = 4 - 2 = 2, result = diff - min_diff = 2 - (-1) = 3
                max_diff = min_diff = 0
				
				# diff at the previous occurance of c1/c2
                last_c1_diff = last_c2_diff = 0 
				
				# check wether we have met c1/c2 during the loop
                meet_c1 = meet_c2 = False
				
                for c in s:
                    if c == c1:
                        meet_c1 = True
                        diff += 1
						
						#  use last_c1_diff instead of diff because we have to make sure that c1 is in the rest part of the substring. 
						# e.g. [c1, c1, c2, c2, c2]
						# At index = 1, if we use diff = 2 -> max_diff = 2
						# At index = 4, diff = 2 - 3 = -1, result = max_diff - diff = 3. 
						# Though we have [c2, c2, c2] as a substring, c1 is not in this string and the result is invalid
                        max_diff = max(last_c1_diff, max_diff)
						
                        last_c1_diff = diff
                    elif c == c2:
                        meet_c2 = True
                        diff -= 1
                        min_diff = min(last_c2_diff, min_diff)
                        last_c2_diff = diff
                    else:
                        continue
					
					# update the result only when we have met both c1 and c2 
                    if meet_c1 and meet_c2:
                        res = max(diff - min_diff, max_diff - diff, res)
        return res

