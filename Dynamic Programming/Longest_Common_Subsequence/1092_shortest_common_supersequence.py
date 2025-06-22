# shortest Common Supersequence will contain all the string in order except the lcs(we have to minus lcs to avoid its repitition) i.e every char we have to add only one
# and lcs will be common in both so write lcs only one time 
# will print length of shortest common supersequence
# logic: lcs will be common in both the string for sure 
# so just add the length of given strings and minus
# the length of the lcs to get the 'length of shortest common supersequence'


def shortestCommonSupersequence(x,y,s1,s2):
        lcs_length= lcs(x,y,s1,s2)
        return x+y-lcs_length
def lcs(x,y,s1,s2):
    dp= [[0 for j in range(y+1)] for i in range(x+1)]
    for i in range(1,x+1):
        for j in range(1,y+1):
            if s1[i-1]== s2[j-1]:
                dp[i][j]= 1+ dp[i-1][j-1]
            else:
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])
    return dp[x][y]

# s1= "qpqrr"
# s2= "pqprqrp"
# s1= "abcbdab"
# s2= "bdcaba" 
s1= "abcd"
s2 = "xycd"

x,y= len(s1), len(s2)
print("the length of shortest common supersequence is: ")
print(shortestCommonSupersequence(x,y,s1,s2))

# Java Code 
"""
class Solution {
    public int shortestCommonSupersequence(String s1, String s2) {
        int x = s1.length(), y = s2.length();
        int lcsLength = lcs(x, y, s1, s2);  
        return x + y - lcsLength;  (LCS)
    }

    private int lcs(int x, int y, String s1, String s2) {
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

    public static void main(String[] args) {
        Solution sol = new Solution();
        String s1 = "abcd";
        String s2 = "xycd";
        System.out.println("The length of shortest common supersequence is: ");
        System.out.println(sol.shortestCommonSupersequence(s1, s2));
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
    int shortestCommonSupersequence(string s1, string s2) {
        int x = s1.length(), y = s2.length();
        int lcsLength = lcs(x, y, s1, s2);  
        return x + y - lcsLength; 
    }

private:
    int lcs(int x, int y, const string& s1, const string& s2) {
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

int main() {
    Solution sol;
    string s1 = "abcd";
    string s2 = "xycd";
    cout << "The length of shortest common supersequence is: " << endl;
    cout << sol.shortestCommonSupersequence(s1, s2) << endl;
    return 0;
}
"""

# to print the string 'shortest common supersequence'
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        x,y= len(str1), len(str2)
        i,j, ans= x,y, ""
        dp= self.lcs(x,y,str1,str2)
        print(dp)
        while(i>0 and j>0):
            if str1[i-1]== str2[j-1]:
                ans= str1[i-1] + ans
                i, j= i-1, j-1
            # in equal case only writing one of the string , thw path we had taken to reach the curr cell
            elif dp[i][j-1]> dp[i-1][j]:  
                    ans= str2[j-1] + ans
                    j-= 1
            # and in unequal cases only writing everytime in direction we will move
            else:
                ans= str1[i-1] + ans
                i-= 1
        # now write the remaining string if left any as we have to include all the ele 
        while(i>0):
            ans= str1[i-1] + ans
            i-= 1
        while(j>0):
            ans= str2[j-1] + ans
            j-= 1  
        return ans
            
    def lcs(self,x,y,s1,s2):
        dp= [[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        return dp


# Java Code 
"""
import java.util.*;

class Solution {
    public String shortestCommonSupersequence(String str1, String str2) {
        int x = str1.length(), y = str2.length();
        int i = x, j = y;
        StringBuilder ans = new StringBuilder();
        int[][] dp = lcs(x, y, str1, str2);
        System.out.println(Arrays.deepToString(dp)); // print(dp)

        while (i > 0 && j > 0) {
            if (str1.charAt(i - 1) == str2.charAt(j - 1)) {
                ans.insert(0, str1.charAt(i - 1));
                i--; j--;
            }
            // in equal case only writing one of the string , the path we had taken to reach the curr cell
            else if (dp[i][j - 1] > dp[i - 1][j]) {
                ans.insert(0, str2.charAt(j - 1));
                j--;
            }
            // and in unequal cases only writing everytime in direction we will move
            else {
                ans.insert(0, str1.charAt(i - 1));
                i--;
            }
        }

        // now write the remaining string if left any as we have to include all the ele
        while (i > 0) {
            ans.insert(0, str1.charAt(i - 1));
            i--;
        }
        while (j > 0) {
            ans.insert(0, str2.charAt(j - 1));
            j--;
        }
        return ans.toString();
    }

    private int[][] lcs(int x, int y, String s1, String s2) {
        int[][] dp = new int[x + 1][y + 1];
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1))
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        int x = str1.size(), y = str2.size();
        int i = x, j = y;
        string ans = "";
        vector<vector<int>> dp = lcs(x, y, str1, str2);

        // print(dp)
        for (const auto& row : dp) {
            for (int val : row) cout << val << " ";
            cout << endl;
        }

        while (i > 0 && j > 0) {
            if (str1[i - 1] == str2[j - 1]) {
                ans = str1[i - 1] + ans;
                i--; j--;
            }
            // in equal case only writing one of the string , the path we had taken to reach the curr cell
            else if (dp[i][j - 1] > dp[i - 1][j]) {
                ans = str2[j - 1] + ans;
                j--;
            }
            // and in unequal cases only writing everytime in direction we will move
            else {
                ans = str1[i - 1] + ans;
                i--;
            }
        }

        // now write the remaining string if left any as we have to include all the ele
        while (i > 0) {
            ans = str1[i - 1] + ans;
            i--;
        }
        while (j > 0) {
            ans = str2[j - 1] + ans;
            j--;
        }
        return ans;
    }

private:
    vector<vector<int>> lcs(int x, int y, const string& s1, const string& s2) {
        vector<vector<int>> dp(x + 1, vector<int>(y + 1, 0));
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (s1[i - 1] == s2[j - 1])
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp;
    }
};
"""