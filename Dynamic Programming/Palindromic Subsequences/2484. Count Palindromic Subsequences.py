# simplest one
# Logic: we have '6' choice for each character.
# i) Don't take it    && In take in case we have '5' possibility i.e take it as :
# i) first_char   ii) 2nd char  iii) 3rd_char  iv) 4th char   v) 5th char  

# To create a 5 digit palindrome we do not need to care about the middle element. 
# We just need to find subsequence of pattern XY_YX. 

# But giving tle in python. Same code getting accepted in java.

# Time: O(10001 * 11 * 11 * 6) = space 
class Solution:
    def __init__(self):
        self.mod = int(1e9 + 7)
        self.dp = [[[[None for _ in range(6)] for _ in range(11)] for _ in range(11)] for _ in range(10001)]

    def dfs(self, ind, first_char, second_char, cnt, s):
        if cnt == 5:
            return 1  # found a subsequence
        if ind == len(s):
            return 0
        if self.dp[ind][first_char][second_char][cnt] is not None:
            return self.dp[ind][first_char][second_char][cnt]

        # option of not choosing current digit
        res = self.dfs(ind + 1, first_char, second_char, cnt, s)

        if cnt == 0:
            # option of choosing the first digit of the subsequence
            res += self.dfs(ind + 1, int(s[ind]), second_char, cnt + 1, s)
            res %= self.mod
        elif cnt == 1:
            # option of choosing the second digit of the subsequence
            res += self.dfs(ind + 1, first_char, int(s[ind]), cnt + 1, s)
            res %= self.mod
        elif cnt == 2:
            # option of choosing the third digit of the subsequence
            res += self.dfs(ind + 1, first_char, second_char, cnt + 1, s)
            res %= self.mod
        elif cnt == 3:
            # option of choosing the fourth digit of the subsequence if it matches with the second_char digit
            if int(s[ind]) == second_char:
                res += self.dfs(ind + 1, first_char, second_char, cnt + 1, s)
                res %= self.mod
        elif cnt == 4:
            # option of choosing the fifth digit of the subsequence if it matches with the first_char digit
            if int(s[ind]) == first_char:
                res += self.dfs(ind + 1, first_char, second_char, cnt + 1, s)
                res %= self.mod

        self.dp[ind][first_char][second_char][cnt] = res
        return res

    def countPalindromes(self, s: str) -> int:
        self.dp = [[[[None for _ in range(6)] for _ in range(11)] for _ in range(11)] for _ in range(10001)]
        return self.dfs(0, 10, 10, 0, s)    # we are passing '10' as first_char & second_char. just any unvalid char


# java
"""
public class Solution {
    private long[][][][] dp;
    private final long MOD = 1_000_000_007L;

    private long dfs(int ind, int first_char, int second_char, int cnt, String s) {
        if (cnt == 5) {
            return 1; // found a subsequence
        }
        if (ind == s.length()) {
            return 0;
        }
        if (dp[ind][first_char][second_char][cnt] != -1) {
            return dp[ind][first_char][second_char][cnt];
        }

        long res = dfs(ind + 1, first_char, second_char, cnt, s); // option of not choosing current digit

        if (cnt == 0) {
            res += dfs(ind + 1, s.charAt(ind) - '0', second_char, cnt + 1, s); // choosing the first digit
            res %= MOD;
        } else if (cnt == 1) {
            res += dfs(ind + 1, first_char, s.charAt(ind) - '0', cnt + 1, s); // choosing the second digit
            res %= MOD;
        } else if (cnt == 2) {
            res += dfs(ind + 1, first_char, second_char, cnt + 1, s); // choosing the third digit
            res %= MOD;
        } else if (cnt == 3) {
            if (s.charAt(ind) - '0' == second_char) {
                res += dfs(ind + 1, first_char, second_char, cnt + 1, s); // choosing the fourth digit if it matches the second
                res %= MOD;
            }
        } else if (cnt == 4) {
            if (s.charAt(ind) - '0' == first_char) {
                res += dfs(ind + 1, first_char, second_char, cnt + 1, s); // choosing the fifth digit if it matches the first
                res %= MOD;
            }
        }

        return dp[ind][first_char][second_char][cnt] = res;
    }

    public int countPalindromes(String s) {
        dp = new long[s.length()][11][11][6];
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < 11; j++) {
                for (int k = 0; k < 11; k++) {
                    for (int l = 0; l < 6; l++) {
                        dp[i][j][k][l] = -1;
                    }
                }
            }
        }
        return (int) dfs(0, 10, 10, 0, s);
    }
}

"""


# Later try in O(n). Solutions in sheet

# Related q to try later:
# 1) 730. Count Different Palindromic Subsequences