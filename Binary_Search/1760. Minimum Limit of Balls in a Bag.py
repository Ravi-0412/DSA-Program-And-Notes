"""
In Koko Eating Bananas, you search for the minimum speed K to finish in H hours.
In Minimum Limit of Balls, you search for the minimum penalty P to finish within maxOperations.

If the Penalty (P) is large: 
  You need fewer operations (easy to satisfy).
  If the Penalty (P) is small: You need more operations (hard to satisfy).

  This is the trickiest part. If a bag has $9$ balls and your target penalty is $3$:You need the bags to be $[3, 3, 3]$.
  How many cuts/operations? 2 operations.
  The Formula: To split a bag of size N into pieces no larger than P, you need:
            Operations = [N / P] - 1 
            Or in integer division: (N - 1) // P

The relationship is:
Number of Pieces= ⌈n / penalty​⌉
Number of Operations=Number of Pieces−1
Number of Operations= ⌈n / penalty​⌉

Q) why (n−1)//penalty ?
In programming, we prefer avoiding math.ceil because it uses floating-point numbers, 
which can lead to precision errors with very large integers (like 10^9 in the constraints).
The integer division trick (n - 1) // penalty is exactly equivalent to ceil(n / penalty) - 1.
e.g: n=9, penalty = 3

Ceil logic,    ⌈9/3⌉−1=3−1 =   2
Integer trick, (9−1)//3=8//3 = 2

Time: O(N * log M), where N is the number of bags and M is the maximum value in nums.
Space : O(1)
"""

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Range: Penalty can be at minimum 1, at maximum the largest bag size
        low, up = 1, max(nums)
        ans = up
        
        while low <= up:
            mid = low + (up - low) // 2
            
            if self.isPossible(nums, mid, maxOperations):
                ans = mid      # This penalty is possible, try to find a smaller one
                up = mid - 1
            else:
                low = mid + 1  # This penalty is too small, need more operations than allowed
                
        return ans

    def isPossible(self, nums, penalty, maxOps):
        total_ops = 0
        for n in nums:
            # Calculate operations needed for this bag
            # Example: bag =9, penalty = 3 -> (9-1)//3 = 2 operations
            total_ops += (n - 1) // penalty
            
            if total_ops > maxOps:
                return False
        return True
