# Time: O(10*n)

class Solution(object):
    def wonderfulSubstrings(self, word):
        # we only need to care if number of occurrences of each letter is odd/even
        # so there will be only two states of each character either occuring even no of time or 'odd'
        # We can use bit mask to represent the state of character
        # for example "0101" represents: ("d" even number, "c" - odd, "b" - even, "a" - odd);
        mask = 0 
        mask_count = [0] * (1023)
                    # since only 10 char is allowed i.e from 'a' to 'j' so mask can go maximum till '1024'(2^10).
        mask_count[0] = 1   # base case 
        ans = 0
        for c in word:
            # get the index of this character
            i = ord(c) - ord('a')
            # we need to set bit at this position for marking current character
            mask = mask ^ (1 << i)
            # Now update the ans. Think in similar way as :560. Subarray Sum Equals K" for visualisation of ans.
            # 1) check if all character has even no of occurence
            # for this find if we have seen same mask before and add their count.
            # suppose we are at current index 'j' and we have seen same mask at index 'i' then, 
            # it means all char has occured even no of times from 'i+1' to 'j' && same for all other indices like 'i'.
            ans += mask_count[mask]
            # 2) check if any one of the letter has odd no of occurence
            # for this try to switch the bit of each char and see if we have seen that before & add their count
            for i in range(10):
                ans += mask_count[mask ^ (1 << i)]  # from this 'index + 1' only one char has odd number of count.
            mask_count[mask] += 1
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public long wonderfulSubstrings(String word) {
        int mask = 0;
        int[] maskCount = new int[1024]; // Since only 10 characters are allowed ('a' to 'j')
        maskCount[0] = 1; // Base case
        long ans = 0;

        for (char c : word.toCharArray()) {
            // Get the index of the character
            int i = c - 'a';
            // Set bit at this position to mark current character
            mask ^= (1 << i);

            // Case 1: Check if all characters have even occurrences
            ans += maskCount[mask];

            // Case 2: Check if any one letter has an odd occurrence
            for (int j = 0; j < 10; j++) {
                ans += maskCount[mask ^ (1 << j)];
            }

            maskCount[mask]++;
        }

        return ans;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    long long wonderfulSubstrings(string word) {
        int mask = 0;
        vector<int> mask_count(1024, 0); // Since only 10 characters are allowed ('a' to 'j')
        mask_count[0] = 1; // Base case
        long long ans = 0;

        for (char c : word) {
            // Get the index of the character
            int i = c - 'a';
            // Set bit at this position to mark current character
            mask ^= (1 << i);

            // Case 1: Check if all characters have even occurrences
            ans += mask_count[mask];

            // Case 2: Check if any one letter has an odd occurrence
            for (int j = 0; j < 10; j++) {
                ans += mask_count[mask ^ (1 << j)];
            }

            mask_count[mask]++;
        }

        return ans;
    }
};
"""