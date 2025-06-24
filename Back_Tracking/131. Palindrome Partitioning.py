# Method 1: 
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

# Java Code 
"""
import java.util.*;

public class Solution {

    public List<List<String>> partition(String s) {
        List<List<String>> ans = new ArrayList<>();
        List<String> part = new ArrayList<>();
        PAlindromePartition(s, part, ans); // starting from index '0'
        return ans;
    }

    public void PAlindromePartition(String s, List<String> part, List<List<String>> ans) {
        if (s.isEmpty()) {
            ans.add(new ArrayList<>(part));
            return;
        }

        for (int i = 0; i < s.length(); i++) {
            String s1 = s.substring(0, i + 1);  // or if s[:i] == s[:i][::-1]:
            if (isPalindrome(s1)) {
                part.add(s1);
                PAlindromePartition(s.substring(i + 1), part, ans);
                // for next starting partition pop the ele that you added so that it add the fresh new palindrome i.e do backtracking
                part.remove(part.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String s) {
        return s.equals(new StringBuilder(s).reverse().toString());
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
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        vector<string> part;
        PAlindromePartition(s, part, ans); // starting from index '0'
        return ans;
    }

    void PAlindromePartition(string s, vector<string>& part, vector<vector<string>>& ans) {
        if (s.empty()) {
            ans.push_back(part);
            return;
        }

        for (int i = 0; i < s.size(); ++i) {
            string s1 = s.substr(0, i + 1);  // or if s[:i] == s[:i][::-1]:
            if (isPalindrome(s1)) {
                part.push_back(s1);
                PAlindromePartition(s.substr(i + 1), part, ans);
                // for next starting partition pop the ele that you added so that it add the fresh new palindrome i.e do backtracking
                part.pop_back();
            }
        }
    }

    bool isPalindrome(const string& s) {
        return equal(s.begin(), s.begin() + s.size() / 2, s.rbegin());
    }
};
"""

# Method 2: 
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

public class Solution {
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
            String substring = s.substring(i, j + 1);
            if (isPalindrome(substring)) {
                partition.add(substring);
                solve(j + 1, s, partition, ans);
                partition.remove(partition.size() - 1); 
            }
        }
    }

    private boolean isPalindrome(String s) {
        return s.equals(new StringBuilder(s).reverse().toString());
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
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        vector<string> partition;
        solve(0, s, partition, ans);
        return ans;
    }

private:
    void solve(int i, const string& s, vector<string>& partition, vector<vector<string>>& ans) {
        if (i == s.size()) {
            ans.push_back(partition);
            return;
        }
        for (int j = i; j < s.size(); ++j) {
            string sub = s.substr(i, j - i + 1);
            if (isPalindrome(sub)) {
                partition.push_back(sub);
                solve(j + 1, s, partition, ans);
                partition.pop_back();
            }
        }
    }

    bool isPalindrome(const string& str) {
        return equal(str.begin(), str.begin() + str.size() / 2, str.rbegin());
    }
};
"""