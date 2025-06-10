# Logic: If you will see the rules properly,
# you can analyse that it is simply asking: " Maximum depth of any ( ".

# Here digits '0-9' and 'operator' won't matter.

# So when you see '(' depth will increase by 1 and when you will see ')' depth will decrease by 1.
# Just take maximum after each character.

# Time : O(n), space : O(14) [0-9, +, -, *, /]

class Solution:
    def maxDepth(self, s: str) -> int:
        skip = {"0", "1", "2","3", "4" ,"5","6","7","8","9", "+", "-", "*", "/"}
        depth = ans = 0
        for c in s:
            if c in skip: 
                continue
            if c == '(':
                depth += 1
            else:
                depth -= 1
            ans = max(ans, depth)
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public int maxDepth(String s) {
        Set<Character> skip = new HashSet<>(Arrays.asList('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/'));
        int depth = 0, ans = 0;

        for (char c : s.toCharArray()) {
            if (skip.contains(c)) {
                continue;
            }
            if (c == '(') {
                depth += 1;
            } else {
                depth -= 1;
            }
            ans = Math.max(ans, depth);
        }
        return ans;
    }
}
"""

# C++ Code
"""
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int maxDepth(string s) {
        unordered_set<char> skip = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/'};
        int depth = 0, ans = 0;

        for (char c : s) {
            if (skip.count(c)) {
                continue;
            }
            if (c == '(') {
                depth += 1;
            } else {
                depth -= 1;
            }
            ans = max(ans, depth);
        }
        return ans;
    }
};
"""
