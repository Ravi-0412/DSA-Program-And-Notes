# method 1: DP + memoisation
# was giving TLE due to O(n^2)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        @lru_cache(None)
        def solve(i, j, card):
            if i > j:
                return 0
            if card == 0:
                return 0
            start= cardPoints[i] + solve(i+1, j, card-1)
            end=   cardPoints[j] + solve(i, j-1, card -1)
            return max(start, end)

        n= len(cardPoints)
        return solve(0, n-1, k)


# method 2: using sliding window
# How to think this?
# Ans: After chooisng 'k' cards whatever way we choose, we will be left with a continous subarray of size= 'n -k' cards.
# Because you can’t choose 2nd element from the beginning unless 
# you have chosen the first one. Similarly, you can’t choose 2nd element from last unless you have chosen the last one.

# And for getting the ans maximum, sum of left subarray should be minimum.
# So now our problem reduces to "Find the smallest sum subarray of size 'n -k' ".
# then our ans= sum(arr) - 'smallest sum of subarray of size 'n -k' '.

# time: O(n)

# Note vvi: Don't go on finding the exact ans what they told, think in reverse way and find the opposite like here.
# It will work in a lot of Good Q and becomes very easy to calculate.

# vvi: First try to reduce the problem into already any done problem either directly or indirectly .

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n= len(cardPoints)
        if k== n: 
            return sum(cardPoints)
        size= n- k
        i, j= 0, 0
        minSum= float('inf')
        curSum= 0
        while j < n:
            curSum+= cardPoints[j]
            if j- i + 1 >= size:
                minSum= min(minSum, curSum)
                curSum-= cardPoints[i]
                i+= 1
            j+= 1
        
        return sum(cardPoints) - minSum


# Related Q: 
# "Maximize sum of K corner elements in Array".
# https://www.geeksforgeeks.org/maximize-sum-of-k-elements-in-array-by-taking-only-corner-elements/


# Also try by frontsum and backsum logic later.
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/solutions/597825/simple-clean-intuitive-explanation-with-visualization/