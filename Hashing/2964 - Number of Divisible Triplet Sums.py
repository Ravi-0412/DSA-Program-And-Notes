# Logic: 
"""
1) (a + b) % d = 0
2) a % d = -b % d
3) a = nums[i] + num[j], b = nums[k]

By fixing each index one by one, try to find the no of pair.
"""

# Time: O(n^2)

class Solution:
    def divisibleTripletCount(self, A: List[int], d: int) -> int:
        ans = 0
        for i in range(len(A)):
            seen = Counter()
            for j in range(i+1, len(A)):
                # -A[j] % d gives the remainder that we need to find among previously seen pairs for the triplet sum to be divisible by d
                ans += seen[-A[j]%d]
                seen[(A[i]+A[j])%d] += 1
        return ans

# Java
# Note: Here we need to convert the remainder to actual needed one.
# Python automatically give that so no needed in python.

"""
import java.util.HashMap;

class Solution {
    public int divisibleTripletCount(int[] nums, int d) {
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            // HashMap to store the frequency of remainders for pairs (nums[i], nums[j])
            HashMap<Integer, Integer> seen = new HashMap<>();
            
            // Inner loop for the second element in the triplet
            for (int j = i + 1; j < nums.length; j++) {
                // Calculate the needed remainder for a triplet to be divisible by d
                int remainder = (-nums[j] % d + d) % d; // Ensuring the remainder is non-negative
                
                // Add to the result the number of pairs with the matching remainder
                ans += seen.getOrDefault(remainder, 0);
                
                // Store the remainder of the current pair (nums[i] + nums[j]) % d
                int pairRemainder = (nums[i] + nums[j]) % d;
                pairRemainder = (pairRemainder + d) % d; // Ensure positive remainder
                
                // Update the frequency of this remainder
                seen.put(pairRemainder, seen.getOrDefault(pairRemainder, 0) + 1);
            }
        }

        return ans;
    }
}

"""
