# write in notes the logic
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
                # for next starting partition pop the ele that you added i.e backtracking
                part.pop()

