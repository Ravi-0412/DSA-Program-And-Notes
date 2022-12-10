# correct only but GFg getting error don't know why
# Time Complexity: O(2^n). Because there are 2^n combinations in worst case i.e when every char is present in the dictiionary
# in this case for every char we will have two options either to chose that char or not
# space: O(n) recursive depth + O(n) for storing ans= O(n)
class Solution:
    def wordBreak(self, dict, s):
        ans= []   # not storing in string because string is immutable
        #  thats why we won't be able to add the current matched word by deleting the last added matched word 
        return self.helper(s,dict,ans)
    
    def helper(self,s,dict,ans):
        if not s:  # reached beyond lenth of string , so you will get one of the possibel ans
            print(" ".join(ans))
            return
        for i in range(1,len(s)+1):
            if s[:i] in dict:
                ans.append(s[:i])
                self.helper(s[i:],dict,ans)
                # now backtrack so that it removes the current mapped string and found the new one
                ans.pop()

w= Solution()
s = "catsanddog"
# # s= "catsandog"
dict = {"cats", "cat", "and", "sand", "dog"}

# test case 2
# dict= { "i", "like", "sam", "sung", "samsung", "mobile", "ice", "and", "cream", "icecream", "man", "go", "mango"}
# s= "ilikesamsungmobile"
# s= "ilikeicecreamandmango"

# test case 3
# s = "leetcode"
# dict = {"leet","code"}
w.wordBreak(dict,s)


# this submitted on leetcode, same approach
# just printing into above case just we have to store in a list ans we got one by one.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans= []  # will store the final ans
        seg= []  # will store the matching segment
        self.helper(s, wordDict,seg,ans)
        return ans
    
    def helper(self,s,dict,seg, ans):
        if not s:
            # listToStr = reduce(lambda a, b : a+ " " +str(b), seg) # shorter way. 
                        # was not able to do by join so used this otherwise iterate and store
            listToStr= " ".join(str(e) for e in seg)   # or do like this
            ans.append(listToStr)
            return
        for i in range(1,len(s)+1):
            if s[:i] in dict:
                seg.append(s[:i])
                self.helper(s[i:],dict,seg,ans)
                # now backtrack so that it removes the current mapped string and found the new one
                seg.pop()

