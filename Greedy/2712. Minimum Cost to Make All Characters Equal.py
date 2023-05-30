# Approach
# start traversing through the array
# a. If you encounter different element i.e s[i] != s[i-1]:
# check from which side it is feasible for us to take less move to make it equal i.e
# i.e 1) either make 'i-1'th char equal to 'i'th char by flipping till index 'i-1' from front with cost of 'i' OR
# 2) make 'i'th char equal to 'i-1'th char with cost by flipping  till index 'i' from back with cost of 'n-i'.

# Maintain a variable ans and keep on adding the min value required for us.

# time: O(n)

class Solution:
    def minimumCost(self, s: str) -> int:
        ans= 0
        n= len(s)
        for i in range(1, n):
            if s[i] != s[i-1]:
                ans+= min(i, n-i)   
        return ans


# method 2: Try to do by this method also
# https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/solutions/3570183/cpp-prefix-and-suffix-sum/

