# This problem can be reduced to : "Find out the minimum 'k' where word is subsequence of "abc" repeated k times."

# Since "abc" is increasing,
# so we can split the original work into k strict increasing subarray.

# How to find k?
# Initial the pre as a big char . Because at least we have to form one subsequence of 'abc'.
# then iterate each char c in word.
# If c <= pre, it means we need to start a new "abc",
# then we increase k++.

# Finally we find k, word is subsequence of "abc" repeated k times.
# We return k * 3 - n.   '3'= len(abc)

# subtracting 'length' because no need to add that much char, they are already given.

# note: agar 'dcba' jaisa form karna hota then strictly decreasing lete.
# pre= smallest char
# if c >= pre, k++.
# last return 4*k - n

# time: O(n), space : O(1)
class Solution:
    def addMinimum(self, word: str) -> int:
        pre= 'z'  # any very large char , it must be greater than the all the char in string.
        k= 0
        for c in word:
            if c <= pre:
               k+= 1
            pre= c
        return 3*k - len(word)
    
# Java Code 
"""
class Solution {
    public int addMinimum(String word) {
        char pre = 'z'; // any very large char, must be greater than all chars in the string
        int k = 0;

        for (char c : word.toCharArray()) {
            if (c <= pre) {
                k++;
            }
            pre = c;
        }

        return 3 * k - word.length();
    }
}
"""

# C++ Code 
"""
#include <string>

using namespace std;

class Solution {
public:
    int addMinimum(string word) {
        char pre = 'z'; // any very large char, must be greater than all chars in the string
        int k = 0;

        for (char c : word) {
            if (c <= pre) {
                k++;
            }
            pre = c;
        }

        return 3 * k - word.length();
    }
};
"""


