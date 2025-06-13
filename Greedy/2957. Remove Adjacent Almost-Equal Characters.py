# Logic: Just count the number of consecutive almost-equal char using ascii value difference.
# We will need to perform minimum of (count//2) operation to remove almost-equal char from these.
# (We can change the middle char for minimum operation).

# Time : O(n), space : O(1)

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        ans = 0
        i = 0
        while i < n:
            cnt = 1
            # Finding the number of consecutive almost-equal starting from 'i'.
            while i + 1 < n and abs(ord(word[i]) - ord(word[i + 1])) <= 1:
                i += 1
                cnt += 1
            ans += (cnt // 2)
            i += 1
        return ans
    
# Java
"""
class Solution {
    public int removeAlmostEqualCharacters(String word) {
        int n = word.length();
        int ans = 0;
        int i = 0;

        while (i < n) {
            int cnt = 1;

            // Finding the number of consecutive almost-equal starting from 'i'.
            while (i + 1 < n && Math.abs(word.charAt(i) - word.charAt(i + 1)) <= 1) {
                i++;
                cnt++;
            }

            ans += (cnt / 2);
            i++;
        }

        return ans;
    }
}
"""

# C++
"""
#include <string>
#include <cmath>
using namespace std;

class Solution {
public:
    int removeAlmostEqualCharacters(string word) {
        int n = word.size();
        int ans = 0;
        int i = 0;

        while (i < n) {
            int cnt = 1;

            // Finding the number of consecutive almost-equal starting from 'i'.
            while (i + 1 < n && abs(word[i] - word[i + 1]) <= 1) {
                i++;
                cnt++;
            }

            ans += (cnt / 2);
            i++;
        }

        return ans;
    }
};
"""

# method 2:
# Steps: 
# 1) Iterate from i = 1 to the string end.
# 2) For each i check if its prev char is almost equal aplohabet or not => 
# where abs diff of current char and prev char is less than equal to 1.
# 3) If almost equal found then we have to change the curr index char to a char diff 
# from prev as well as diff from the next. So we increment the change count. 
# We don't hv to care about the what the new char will be as we will replace by that char for which 'i-1' and 'i+1' is not almost-equal.
# 4) Also if we change the char to a new one that means we are sure that the next char should not be checked 
# so iterate one more to skip check for the immidiate next char.

# Time : O(n), space : O(1)

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        ans = 0
        i = 1
        while i < n:
            if abs(ord(word[i]) - ord(word[i -1])) <= 1:
                ans += 1
                i += 1   # No need to check next char
            i += 1
        return ans

# Java
"""
class Solution {
    public int removeAlmostEqualCharacters(String word) {
        int n = word.length();
        int ans = 0;
        int i = 1;

        while (i < n) {
            if (Math.abs(word.charAt(i) - word.charAt(i - 1)) <= 1) {
                ans += 1;
                i += 1; // No need to check next char
            }
            i += 1;
        }

        return ans;
    }
}
"""

# C++
"""
#include <string>
#include <cmath>
using namespace std;

class Solution {
public:
    int removeAlmostEqualCharacters(string word) {
        int n = word.length();
        int ans = 0;
        int i = 1;

        while (i < n) {
            if (abs(word[i] - word[i - 1]) <= 1) {
                ans += 1;
                i += 1; // No need to check next char
            }
            i += 1;
        }

        return ans;
    }
}
"""