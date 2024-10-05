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

from collections import Counter

class Solution:
    def largestVariance(self, s: str) -> int:
        # Step 1: Calculate frequency of each character
        freq = Counter(s)

        # Step 2: Create a set of unique characters from the string
        charSet = set(s)
        
        ans = 0

        # Step 3: Iterate over pairs of distinct characters
        for c1 in charSet:
            for c2 in charSet:
                if c1 == c2:
                    continue  # We only calculate variance for distinct characters

                # Step 4: Perform Kadane's algorithm twice, one normal and one reversed
                for _ in range(2):
                    count1, count2 = 0, 0  # Track the counts of c1 and c2 in the current substring
                    for c in s:
                        if c == c1:
                            count1 += 1
                        if c == c2:
                            count2 += 1

                        # Step 5: Reset counts if count1 < count2
                        if count1 < count2:
                            count1, count2 = 0, 0

                        # Step 6: Update the answer when both counts are positive
                        if count1 > 0 and count2 > 0:
                            ans = max(ans, count1 - count2)

                    # Step 7: Reverse the string and repeat
                    s = s[::-1]

        return ans

# Java
"""
import java.util.*;

public class Solution {
    public int largestVariance(String s) {
        // Step 1: Calculate frequency of each character
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        // Step 2: Create a set of unique characters from the string
        Set<Character> charSet = new HashSet<>();
        for (char c : s.toCharArray()) {
            charSet.add(c);
        }

        int ans = 0;

        // Step 3: Iterate over pairs of distinct characters
        for (char c1 : charSet) {
            for (char c2 : charSet) {
                if (c1 == c2) {
                    continue; // We only calculate variance for distinct characters
                }

                // Step 4: Perform Kadane's algorithm twice, one normal and one reversed
                for (int k = 0; k < 2; k++) {
                    int count1 = 0, count2 = 0; // Track the counts of c1 and c2 in the current substring
                    for (char c : s.toCharArray()) {
                        if (c == c1) {
                            count1++;
                        }
                        if (c == c2) {
                            count2++;
                        }

                        // Step 5: Reset counts if count1 < count2
                        if (count1 < count2) {
                            count1 = 0;
                            count2 = 0;
                        }

                        // Step 6: Update the answer when both counts are positive
                        if (count1 > 0 && count2 > 0) {
                            ans = Math.max(ans, count1 - count2);
                        }
                    }

                    // Step 7: Reverse the string and repeat
                    s = new StringBuilder(s).reverse().toString();
                }
            }
        }

        return ans;
    }
}
"""



# Try to understand this logic also.
# https://leetcode.com/problems/substring-with-largest-variance/solutions/2579146/%22Weird-Kadane%22-or-Intuition-+-Solution-Explained/


