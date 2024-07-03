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


# Related Q:
# 1) 93. Restore IP Addresses
# 2) 282. Expression Add Operators
# 3) 140. Word Break II


# Java
"""
class Solution {
    private int n;
    private List<List<String>> ans;

    public List<List<String>> partition(String s) {
        n = s.length() ;
        ans = new ArrayList<>();
        backtrack(0, s, new ArrayList<String>());
        return ans;   
    }
    public void backtrack(int ind, String s, List<String> par) {
        if(ind == n){
            // directly adding will give wrong ans because in java list are passed by referene.
            ans.add(new ArrayList<>(par));
            return ;
        }
        for(int j = ind ; j < n; j ++){
            String substr = s.substring(ind, j + 1);
            // checking palindrome
            if(substr.equals(new StringBuilder(substr).reverse().toString())) {
                par.add(substr);
                backtrack(j + 1, s, par) ;
                par.remove(par.size() - 1) ;
            }
        }
    }
}

"""