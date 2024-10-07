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
