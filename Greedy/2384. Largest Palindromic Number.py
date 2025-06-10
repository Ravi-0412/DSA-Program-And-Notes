# 1st method
"""
1) We will try to keep middle element as maximum as possible having odd frequency.
2) Now try to form left_part sorting the elements in descending order, each number in left part will get added as: num * (freq //2).
Note: Number will be only from '9' to '0'.
3) Handle the leading zero case.
4) Ans = left_part + Middle + right_part(just reverse of left part).

# Time: O(10 * log10) for sorting, because in map key element will be from '0' to '9' only.
"""
from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        # Count frequency of each digit
        freq = Counter(num)
        
        # Sort digits in descending order and store in variable
        sorted_digits = sorted(freq.keys(), reverse=True)
        
        first_half = ""
        middle_digit = ""
        
        for digit in sorted_digits:
            count = freq[digit]
            
            # Add pairs to first half
            first_half += digit * (count // 2)
            
            # Set middle digit if not already set and count is odd
            if count % 2 == 1 and not middle_digit:
                middle_digit = digit
        
        # Remove leading zeros
        first_half = first_half.lstrip('0')
        
        # Handle edge cases and construct result
        if not first_half:
            return middle_digit if middle_digit else "0"
        
        return first_half + middle_digit + first_half[::-1]

  # in java
  """
  import java.util.*;

class Solution {
    public String largestPalindromic(String num) {
        // Create a frequency map of digits
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : num.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        // Sort the digits in reverse order (from '9' to '0')
        List<Character> sortedDigits = new ArrayList<>(freq.keySet());
        sortedDigits.sort((a, b) -> b - a);

        StringBuilder firstHalf = new StringBuilder();
        String middleDigit = "";

        // Construct the first half and find a potential middle digit
        for (char digit : sortedDigits) {
            int count = freq.get(digit);
            firstHalf.append(String.valueOf(digit).repeat(count / 2)); // Repeat digit count / 2 times
            if (count % 2 == 1 && middleDigit.isEmpty()) {
                middleDigit = String.valueOf(digit);
            }
        }

        // Remove leading zeros
        while (firstHalf.length() > 0 && firstHalf.charAt(0) == '0') {
            firstHalf.deleteCharAt(0);
        }

        // If no valid first half exists, return the middle digit or "0"
        if (firstHalf.length() == 0) {
            return middleDigit.isEmpty() ? "0" : middleDigit;
        }

        // Return the largest palindromic number
        return firstHalf.toString() + middleDigit + firstHalf.reverse().toString();
    }
}


Note: If we want to don't use 'deleteCharAt(0)' to optimise time complexity from O(n^2) to O(1) for each operation then do like this.

int nonZeroIndex = 0;
      while (nonZeroIndex < firstHalf.length() && firstHalf.charAt(nonZeroIndex) == '0') {
            nonZeroIndex++;
        }

        // If the first half is entirely zeros, check if the middle digit exists
        if (nonZeroIndex == firstHalf.length()) {
            // If there was no valid non-zero first half, return the middle digit or "0"
            return middleDigit.isEmpty() ? "0" : middleDigit;
        }

        // Skip leading zeros and update firstHalf
        firstHalf = new StringBuilder(firstHalf.substring(nonZeroIndex));

        // Return the largest palindromic number
        return firstHalf.toString() + middleDigit + firstHalf.reverse().toString();

# Same way we can do in python but not needed.
  """

# C++ Code 
"""
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string largestPalindromic(string num) {
        unordered_map<char, int> freq;
        
        // Count frequency of each digit
        for (char digit : num) {
            freq[digit]++;
        }

        // Sort digits in descending order
        vector<char> sorted_digits;
        for (auto& entry : freq) {
            sorted_digits.push_back(entry.first);
        }
        sort(sorted_digits.rbegin(), sorted_digits.rend());

        string first_half = "", middle_digit = "";
        
        for (char digit : sorted_digits) {
            int count = freq[digit];

            // Add pairs to first half
            first_half += string(count / 2, digit);

            // Set middle digit if not already set and count is odd
            if (count % 2 == 1 && middle_digit.empty()) {
                middle_digit = digit;
            }
        }

        // Remove leading zeros
        first_half.erase(0, first_half.find_first_not_of('0'));

        // Handle edge cases and construct result
        if (first_half.empty()) {
            return middle_digit.empty() ? "0" : middle_digit;
        }

        return first_half + middle_digit + string(first_half.rbegin(), first_half.rend());
    }
};
"""

# 2nd method: Using the fact that number will be from '0' to '9'.
# so instead of sorting, traverse the digit in descending order from '9' to '0' directly.
from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        # Count the frequency of each digit in the input string
        count = Counter(num)

        # Construct the first half of the palindrome
        first_half = ""
        for digit in '9876543210':  # Iterate over digits in reverse order
            count_of_digit = count[digit] // 2  # Take half of the count of each digit
            first_half += digit * count_of_digit  # Add that many digits to the first half

        # Remove leading zeros from the first half
        first_half = first_half.lstrip('0')

        # Find the middle digit (if any) to be placed in the center of the palindrome
        mid = ""
        for digit in count:
            if count[digit] % 2 == 1:  # If the count of the digit is odd
                mid = max(mid, digit)  # Choose the largest such digit as the middle

        # Construct the final palindrome
        # If no first half exists, we check if we have a middle digit and return it or '0'
        if not first_half and not mid:
            return '0'
        
        return first_half + mid + first_half[::-1]

# Java
"""
import java.util.*;

class Solution {
    public String largestPalindromic(String num) {
        Map<Character, Integer> count = new HashMap<>();
        for (char c : num.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }
        
        StringBuilder firstHalf = new StringBuilder();
        for (char digit = '9'; digit >= '0'; digit--) {
            int countOfDigit = count.getOrDefault(digit, 0) / 2;
            for (int i = 0; i < countOfDigit; i++) {
                firstHalf.append(digit);
            }
        }
        
        // Remove leading zeros
        while (firstHalf.length() > 0 && firstHalf.charAt(0) == '0') {
            firstHalf.deleteCharAt(0);
        }

        String mid = "";
        for (char digit : count.keySet()) {
            if (count.get(digit) % 2 == 1) {
                mid = String.valueOf(digit);
            }
        }

        if (firstHalf.length() == 0 && mid.isEmpty()) {
            return "0";
        }

        return firstHalf.toString() + mid + firstHalf.reverse().toString();
    }
}
"""

# C++ Code 
"""
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    string largestPalindromic(string num) {
        unordered_map<char, int> count;

        // Count the frequency of each digit in the input string
        for (char digit : num) {
            count[digit]++;
        }

        string first_half = "";
        string mid = "";

        // Iterate over digits in reverse order
        for (char digit : "9876543210") {
            int count_of_digit = count[digit] / 2; // Take half of the count of each digit
            first_half.append(count_of_digit, digit); // Add that many digits to the first half
        }

        // Remove leading zeros from the first half
        first_half.erase(0, first_half.find_first_not_of('0'));

        // Find the middle digit (if any) to be placed in the center of the palindrome
        for (auto& entry : count) {
            if (entry.second % 2 == 1) { // If the count of the digit is odd
                mid = max(mid, string(1, entry.first)); // Choose the largest such digit as the middle
            }
        }

        // Construct the final palindrome
        if (first_half.empty() && mid.empty()) {
            return "0";
        }

        return first_half + mid + string(first_half.rbegin(), first_half.rend());
    }
};
"""