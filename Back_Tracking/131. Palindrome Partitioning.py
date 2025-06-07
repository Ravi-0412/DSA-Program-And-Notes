# write in notes the logic
# Time: O(2^n * n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, part= [], []
        self.PAlindromePartition(s,part,ans) # starting from index '0'
        return ans
    
    def PAlindromePartition(self,s,part, ans):
        if not s:
            ans.append(part.copy())
            return 
        for i in range(len(s)):
            s1= s[:i+1]           # or if s[:i] == s[:i][::-1]:
            if s1==s1[::-1]:
                part.append(s1)
                self.PAlindromePartition(s[i+1:],part,ans)
                # for next starting partition pop the ele that you added so that it add the fresh new palindrome i.e do backtracking
                part.pop()

# Better one:
# No need to 'pop' while returning time if we modify the partition in function call only
# instead of 1st appending and then adding.
# This we can do in every Q.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def solve(i, partition):
            if i == len(s):
                ans.append(partition)
                return
            for j in range(i, n):
                if s[i : j + 1] == s[i : j + 1][::-1]:
                    solve(j + 1, partition + [s[i : j + 1]])

        ans = []
        solve(0, [])
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> ans = new ArrayList<>();
        solve(0, s, new ArrayList<>(), ans);
        return ans;
    }

    private void solve(int i, String s, List<String> partition, List<List<String>> ans) {
        if (i == s.length()) {
            ans.add(new ArrayList<>(partition));
            return;
        }
        for (int j = i; j < s.length(); j++) {
            String sub = s.substring(i, j + 1);
            if (isPalindrome(sub)) {
                partition.add(sub);
                solve(j + 1, s, partition, ans);
                partition.remove(partition.size() - 1); // Backtracking
            }
        }
    }

    private boolean isPalindrome(String s) {
        return new StringBuilder(s).reverse().toString().equals(s);
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
    void palindromePartition(string s, vector<string> &part, vector<vector<string>> &ans) {
        if (s.empty()) {
            ans.push_back(part);
            return;
        }
        for (int i = 0; i < s.size(); i++) {
            string s1 = s.substr(0, i + 1); // Extract substring
            if (s1 == string(s1.rbegin(), s1.rend())) { // Check if palindrome
                part.push_back(s1);
                palindromePartition(s.substr(i + 1), part, ans);
                part.pop_back(); // Backtracking
            }
        }
    }

    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        vector<string> part;
        palindromePartition(s, part, ans);
        return ans;
    }
};
"""
# Related Q:
# 1) 93. Restore IP Addresses
# 2) 282. Expression Add Operators
# 3) 140. Word Break II
