# correct only but GFg getting error don't know why
# Time Complexity: O(2^n). Because there are 2^n combinations in worst case i.e when every char is present in the dictiionary
# in this case for every char we will have two options either to chose that char or not
# space: O(n) recursive depth + O(n) for storing ans= O(n)
class Solution:
    def wordBreak(self, dict, s):
        ans= []   # not storing in string because string is immutable thats why it will be add the matched sequence in  the already found sequnence only
        return self.helper(s,dict,ans)
    
    def helper(self,s,dict,ans):
        if not s:
            print(" ".join(ans))
            return
        for i in range(1,len(s)+1):
            if s[:i] in dict:
                ans.append(s[:i])
                self.helper(s[i:],dict,ans)
                # now backtrack so that it removes the current mapped string and found the new one
                ans.pop()

w= Solution()
# s = "catsanddog"
# # s= "catsandog"
# dict = {"cats", "cat", "and", "sand", "dog"}

# test case 2
dict= { "i", "like", "sam", "sung", "samsung", "mobile", "ice", "and", "cream", "icecream", "man", "go", "mango"}
# s= "ilikesamsungmobile"
s= "ilikeicecreamandmango"
w.wordBreak(dict,s)
