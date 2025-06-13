# Method 1 :
# Using Dynamic Programming, just using exact code of 'Longest common Subsequence'

# if s is a subsequence of 't' then lcs of 's' and 't'
# must be equal to the 's' itself as lcs of two strings is
# always less than or equal to the length of min(length of either string)
# time = space = O(n*m)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x,y= len(s), len(t)
        lcs_length= self.lcs(x,y,s,t)
        if lcs_length== x:  # check if length of lcs= len(substring)
            return True
        return False
    def lcs(self,x,y,s1,s2):
        dp= [[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        return dp[x][y]


# Java
"""
class Solution {
    public boolean isSubsequence(String s, String t) {
        int x = s.length(), y = t.length();
        int lcs_length = lcs(x, y, s, t);
        if (lcs_length == x)  // check if length of lcs = len(substring)
            return true;
        return false;
    }

    public int lcs(int x, int y, String s1, String s2) {
        int[][] dp = new int[x + 1][y + 1];
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1))
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[x][y];
    }
}
"""

# C++
"""
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int x = s.length(), y = t.length();
        int lcs_length = lcs(x, y, s, t);
        if (lcs_length == x)  // check if length of lcs = len(substring)
            return true;
        return false;
    }

    int lcs(int x, int y, string& s1, string& s2) {
        vector<vector<int>> dp(x + 1, vector<int>(y + 1, 0));
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (s1[i - 1] == s2[j - 1])
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[x][y];
    }
};
"""

# method 2:
"""
Using Two pointer : Best way
logic: traverse both simultaneoulsy and when both char is same incr both pointer else incr pointer of 't' only(say 'j').

'i' will tell the no of char of 's' that we seen in 't' at any point of time.

At last if value of 'i' >= len(s) means we have got all char of 's' in 't'.

apporach : 
1) start 2 variables i and j,both are initializes to 0 , which points s and t respectively
2)in this while loop both the points runs upto the lenth of the strings ,
in this loop if s[i] == t[j], move both forward (i++, j++).
If characters don’t match, move only j++ to keep looking for a match for s[i] in t.
after the loop , If all characters of s were matched (i == len(s)), return True.
Otherwise, return False (some characters in s weren’t found in order in t).
time: O(m + n)
space :O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j= 0, 0  # will point to 's' and 't' respectively
        while i < len(s) and j < len(t):
            if s[i]== t[j] :
                i+= 1
                j+= 1
            else:
                j+= 1 
        return i== len(s)  # means we have got all char of 's' in 't'.
    
# java
"""
class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0, j = 0;  // will point to 's' and 't' respectively
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
                j++;
            } else {
                j++;
            }
        }
        return i == s.length();  // means we have got all char of 's' in 't'.
    }
}
"""

# C++
"""
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;  // will point to 's' and 't' respectively
        while (i < s.length() && j < t.length()) {
            if (s[i] == t[j]) {
                i++;
                j++;
            } else {
                j++;
            }
        }
        return i == s.length();  // means we have got all char of 's' in 't'.
    }
};
"""
    
# method 3: 
# using stack
# We treat subsequence string as stack and travel from end of base string.
# When the top() of stack matches current element in base string we pop().
# We continue till we reach end of base string or till stick becomes empty.

# time: O(n)= O(10000) , only for 't'
# space= O(100), only for 's'
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = list(s)
        for i in range(len(t) -1, -1, -1):
            if not stack:
                return True
            if t[i] == stack[-1]:
                stack.pop()
        return stack == []
    

# Java
"""
import java.util.Stack;

class Solution {
    public boolean isSubsequence(String s, String t) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            stack.push(c);
        }

        for (int i = t.length() - 1; i >= 0; i--) {
            if (stack.isEmpty())
                return true;
            if (t.charAt(i) == stack.peek())
                stack.pop();
        }

        return stack.isEmpty();
    }
}
"""

# C++
"""
import java.util.Stack;

class Solution {
    public boolean isSubsequence(String s, String t) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            stack.push(c);
        }

        for (int i = t.length() - 1; i >= 0; i--) {
            if (stack.isEmpty())
                return true;
            if (t.charAt(i) == stack.peek())
                stack.pop();
        }

        return stack.isEmpty();
    }
}
"""