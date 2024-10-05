# method 1: Brute Force
# for each substring find the variance.
# Variance = 'max(frequency) of a char' - 'min(frequency) of a char' 
# time:O(n^3)


# optimised one.
# As we have to find the " largest difference between the number of occurrences of any 2 characters present in the string".

# Having an input string we do not know which characters c1 and c2 are. 
# But we can try all possible pairs (c1,c2) assuming that freq[c1] ≥ freq[c2] .
# For the choosed characters c1 and c2 , we can transform the initial string to the array of the same size by applying the following rules:
# c1 converts into 1
# c2 converts into −1
# any other character converts into 0

# So now we have the array consisting of −1, 0 and 1 with the property that the difference between freq[c1] — freq[c2]
# on substring is simply the sum of all array elements on the corresponding subarray. 
# Thus our problem becomes Maximum subarray problem which can be solved by Kadane algorithm.

# time: O((26*25)/2 *n *2), n= len(s)

# correct only but Leetcode compiler is not working properly.

# More explanation in notes: page no = 157


class Solution:
    def largestVariance(self, s: str) -> int:
        freq = Counter(s)   # to check if picked char exist or not
        charSet = list(set(s))
        n = len(charSet)
        ans = 0
        for i in range(n):
            for j in range(i +1, n):
                c1, c2 = charSet[i], charSet[j]
                # we only calculate the variance if char is different and
                # 2) we can only apply Kedane's if picked char exist.
                if c1 == c2 :
                    continue
                # Now traverse the whole string and apply kedane's
                # we will apply kedanes two time. 
                # one for reversed string also to handle the cases "baa", "abbbbb","aabbbbb", etc.
                for k in range(2):
                    count1, count2 = 0, 0 # will keep track of count of c1 and c2 in substring we have traversed till now
                    for c in s:
                        if c == c1:
                            count1 += 1
                        if c == c2:
                            count2 += 1
                        # check if count1 < count 2 then reset both count = 0
                        # like we do in Kedane's when curSum < 0 then we make curSum = 0
                        if count1 < count2 :
                            count1 , count2 = 0, 0
                        # check if count of both char is >0 .
                        if count1 > 0 and count2 > 0:
                            ans = max(ans, count1 - count2)
                    
                    # Now reverse the string and do the same process again
                    s = s[::-1]
            return ans




# Try to understand this logic also.
# https://leetcode.com/problems/substring-with-largest-variance/solutions/2579146/%22Weird-Kadane%22-or-Intuition-+-Solution-Explained/


