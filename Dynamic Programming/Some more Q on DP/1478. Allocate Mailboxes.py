# Logic: 
"""
When K == 1, theres only 1 mailbox. So, we put it in the median of the what we are currently checking. For example [4,8,20], we put the mailbox at 8, and then we calculate the difference accordingly.

When K == len(houses), this is also trivial, you can put a mailbox at every house, so distance will be 0.

So with base cases considered, we now go to higher numbers of K. What if K == 2? Then we can portion one part of the house into one group, put a mailbox there, and the remaining houses will be another group putting another mailbox. E.g

[1, 300, 301, 302] can be thought as:
[1], [300, 301, 302] OR
[1, 300], [301, 302] OR
[1, 300, 301], [302]

So this is when K == 2. Right now we can visually see that the first answer is the best.

Consider further, if K == 3. Then decide where we want to put the first group, and then solve the subproblems recursively. Same example as above.

[1] (first group) [300,301,302] will be split into another 2 groups. So it will recursively call
[300] [301, 302]
[300, 301] [302]

OR
[1, 300] - > first group, [301, 302] - > split this into another 2 groups. Then
[301], [302]

Note: In general, we pick a place to form one group, then, the remaining elements must form K - 1 groups, 
and we try to minimise the answer.
"""

# Time: O(n^3)

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        # Sort the houses, to calculate in forward direction only
        houses.sort()
        
        # Memoization table, using a dictionary is easier but slower
        memo = [[[-1 for i in range(len(houses))] for j in range(len(houses))] for _ in range (k + 1)]
        
        # left = left index of sorted houses, right = including right index, num = number of mailboxes we can place for this group
        def helper(left, right, num): 
            # Too many mailboxes, too few houses. We've made an error in grouping earlier. Return a 'FAIL' answer.
            if right - left + 1 < num:
                return float('inf')
              
             # If there is a mailbox for every house, return 0 (no distance to minimize)
            if num == right - left + 1:
                return 0
              
            if memo[num][left][right] != -1:
                return memo[num][left][right]

            # Base case: if only one mailbox, place it at the median of the houses.
            if num == 1:
                ans = 0
                mid = (left + right) // 2
                for i in range(left, right + 1):
                    ans += abs(houses[i] - houses[mid])
                memo[num][left][right] = ans
                return ans
            
            ans = float('inf')
            
            # "Careful Brute Force" approach
            for i in range(left, right):
                ans = min(ans, helper(left, i, 1) + helper(i + 1, right, num - 1))
            
            # Store the answer in the memoization table
            memo[num][left][right] = ans
            return ans

        return helper(0, len(houses) - 1, k)
