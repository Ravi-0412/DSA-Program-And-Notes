# logic: 1) Find the square of each number from '1' to 'n'. square= i*i
# 2) we have to check whether we can "partitioned square into contiguous substrings such that 
# the sum of the integer values of these substrings equals i."

# Note: Just we are generating each possible substring one after another and taking their sum.
# for this split from each remainining index using recursion.
# Time= O(n^2), n= len(square)

# why Brute force is getting accepted?
# Reason: Max value of n= 1000, max_value_of_square= 1000000  (7 digit).
# time: O(7^2)

# total time complexity: O(49 * n)


class Solution:
    def punishmentNumber(self, n: int) -> int:

        def partitionPossible(num, i, res):
            if num== '':
                return i== res  # will return True if i==res else False
            # Try to partition into contiguos substring from each index. Just taking sum of all possible substring generated one after another.
            for j in range(1, len(num) + 1):
                if partitionPossible(num[j: ], i, res + int(num[: j])):
                    # If any of the partition return True, then return True
                    return True
            # no such partition possible
            return False

        ans= 0
        for i in range(1, n +1):
            square= i * i
            if partitionPossible(str(square), i, 0):
                ans+= square
        return ans


# Java
"""
class Solution {
    public int punishmentNumber(int n) {
        int ans = 0;
        
        // Loop through numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            int square = i * i;
            // Check if partitioning is possible for the square of the current number
            if (partitionPossible(String.valueOf(square), i, 0)) {
                ans += square;
            }
        }
        
        return ans;
    }
    
    // Helper function to check if partitioning is possible
    private boolean partitionPossible(String num, int i, int res) {
        // If the number is empty, check if the sum of the partitions equals i
        if (num.isEmpty()) {
            return i == res;
        }
        
        // Try to partition into contiguous substrings
        for (int j = 1; j <= num.length(); j++) {
            // Recursively try all partitions
            if (partitionPossible(num.substring(j), i, res + Integer.parseInt(num.substring(0, j)))) {
                return true;  // Return true if a valid partition is found
            }
        }
        
        // Return false if no valid partition is found
        return false;
    }
}

"""

