# method 1: 
# Note: thought to do by same method as 'printing lcs' but was becoming very tough and not getting how to do.
# Try all substring
# Time: O(n^3)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        result = ""

        # Try all substrings
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if self.isPalindrome(sub):
                    if (j - i + 1) > max_len:
                        max_len = j - i + 1
                        result = sub
        return result

    def isPalindrome(self, sub: str) -> bool:
        return sub == sub[::-1]

# Java Code 
"""
class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        int max_len = 0;
        String result = "";

        // Try all substrings
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                String sub = s.substring(i, j + 1);
                if (isPalindrome(sub)) {
                    if ((j - i + 1) > max_len) {
                        max_len = j - i + 1;
                        result = sub;
                    }
                }
            }
        }
        return result;
    }

    public boolean isPalindrome(String sub) {
        return new StringBuilder(sub).reverse().toString().equals(sub);
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        int max_len = 0;
        string result = "";

        // Try all substrings
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                string sub = s.substr(i, j - i + 1);
                if (isPalindrome(sub)) {
                    if ((j - i + 1) > max_len) {
                        max_len = j - i + 1;
                        result = sub;
                    }
                }
            }
        }
        return result;
    }

    bool isPalindrome(const string& sub) {
        return sub == string(sub.rbegin(), sub.rend());
    }
};
"""

# Method 2: 
"""
this one is very easy and logical.
just the another way to check whether a string is palindrome or not.
normally we used to check by taking two pointer, one at the start and one at the end and we go till 'mid'.

another way VVI: start checking from mid and move the pointer to it left and right 
and check whether they are equal or not.
using same logic: take each ele as mid and take two pointer left and right
(initailisation will depend on what we are checking i.e even or odd len palindrome) 
and move left pointer one position to left and right pointer one position to right.

logic: we are just calculating the max len of odd and even length palindrome from each index.
just treat each index as mid and move left and right from that.

 time: O(n*n)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans= ""
        ansLen= 0
        for i in range(len(s)):
            # check for odd length palindrome
            l, r= i, i
            while l>= 0 and r < len(s) and s[l]== s[r]:
                if r-l+1 > ansLen:
                    ans=    s[l: r+1]
                    ansLen= r-l +1
                l-= 1
                r+= 1
            
            # now check for even length palindrome
            l, r= i, i+1
            while l>= 0 and r < len(s) and s[l]== s[r]:
                if r-l+1 > ansLen:
                    ans=    s[l: r+1]
                    ansLen= r-l +1
                l-= 1
                r+= 1
        return ans
# Java Code 
"""
class Solution {
    public String longestPalindrome(String s) {
        String ans = "";
        int ansLen = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            // check for odd length palindrome
            int l = i, r = i;
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > ansLen) {
                    ans = s.substring(l, r + 1);
                    ansLen = r - l + 1;
                }
                l--;
                r++;
            }

            // now check for even length palindrome
            l = i;
            r = i + 1;
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > ansLen) {
                    ans = s.substring(l, r + 1);
                    ansLen = r - l + 1;
                }
                l--;
                r++;
            }
        }

        return ans;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    string longestPalindrome(string s) {
        string ans = "";
        int ansLen = 0;
        int n = s.length();

        for (int i = 0; i < n; ++i) {
            // check for odd length palindrome
            int l = i, r = i;
            while (l >= 0 && r < n && s[l] == s[r]) {
                if (r - l + 1 > ansLen) {
                    ans = s.substr(l, r - l + 1);
                    ansLen = r - l + 1;
                }
                l--;
                r++;
            }

            // now check for even length palindrome
            l = i;
            r = i + 1;
            while (l >= 0 && r < n && s[l] == s[r]) {
                if (r - l + 1 > ansLen) {
                    ans = s.substr(l, r - l + 1);
                    ansLen = r - l + 1;
                }
                l--;
                r++;
            }
        }

        return ans;
    }
};
"""

# Method 3:
# Better to write above code
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def longestPal(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        ans = ""
        for i in range(len(s)):
            # Check for odd-length palindrome
            odd_pal = longestPal(i, i)
            # Check for even-length palindrome
            even_pal = longestPal(i, i + 1)

            # Update the answer if the found palindrome is longer
            if len(odd_pal) > len(ans):
                ans = odd_pal
            if len(even_pal) > len(ans):
                ans = even_pal

        return ans


# Java Code 
"""
class Solution {
    public String longestPalindrome(String s) {
        String ans = "";

        for (int i = 0; i < s.length(); i++) {
            // Check for odd-length palindrome
            String odd_pal = longestPal(s, i, i);
            // Check for even-length palindrome
            String even_pal = longestPal(s, i, i + 1);

            // Update the answer if the found palindrome is longer
            if (odd_pal.length() > ans.length()) {
                ans = odd_pal;
            }
            if (even_pal.length() > ans.length()) {
                ans = even_pal;
            }
        }

        return ans;
    }

    private String longestPal(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        return s.substring(l + 1, r);
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    string longestPalindrome(string s) {
        string ans = "";

        for (int i = 0; i < s.length(); ++i) {
            // Check for odd-length palindrome
            string odd_pal = longestPal(s, i, i);
            // Check for even-length palindrome
            string even_pal = longestPal(s, i, i + 1);

            // Update the answer if the found palindrome is longer
            if (odd_pal.length() > ans.length()) {
                ans = odd_pal;
            }
            if (even_pal.length() > ans.length()) {
                ans = even_pal;
            }
        }

        return ans;
    }

private:
    string longestPal(const string& s, int l, int r) {
        while (l >= 0 && r < s.length() && s[l] == s[r]) {
            l--;
            r++;
        }
        return s.substr(l + 1, r - l - 1);
    }
};
"""

# Method 4: 
# Using DP
# logic: 
"""
Observation: how we can avoid unnecessary re-computation while validating palindromes.
 Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious 
 that "ababa" must be a palindrome since the two left and right end letters are the same.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] 
        # dp[j][i] : whether string from 'j to i' is palindrome or not.
        # j: starting index , i: last index
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str

# Java Code 
"""
class Solution {
    public String longestPalindrome(String s) {
        if (s.length() <= 1)
            return s;

        int Max_Len = 1;
        String Max_Str = s.substring(0, 1);
        boolean[][] dp = new boolean[s.length()][s.length()];
        // dp[j][i] : whether string from 'j to i' is palindrome or not.
        // j: starting index , i: last index

        for (int i = 0; i < s.length(); i++) {
            dp[i][i] = true;
            for (int j = 0; j < i; j++) {
                if (s.charAt(j) == s.charAt(i) && (i - j <= 2 || dp[j + 1][i - 1])) {
                    dp[j][i] = true;
                    if (i - j + 1 > Max_Len) {
                        Max_Len = i - j + 1;
                        Max_Str = s.substring(j, i + 1);
                    }
                }
            }
        }

        return Max_Str;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.length() <= 1)
            return s;

        int Max_Len = 1;
        string Max_Str = s.substr(0, 1);
        int n = s.length();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        // dp[j][i] : whether string from 'j to i' is palindrome or not.
        // j: starting index , i: last index

        for (int i = 0; i < n; ++i) {
            dp[i][i] = true;
            for (int j = 0; j < i; ++j) {
                if (s[j] == s[i] && (i - j <= 2 || dp[j + 1][i - 1])) {
                    dp[j][i] = true;
                    if (i - j + 1 > Max_Len) {
                        Max_Len = i - j + 1;
                        Max_Str = s.substr(j, Max_Len);
                    }
                }
            }
        }

        return Max_Str;
    }
};
"""

"""
Related question:
1) 647. Palindromic Substrings
2) 1062. Longest Repeating Substring
"""
