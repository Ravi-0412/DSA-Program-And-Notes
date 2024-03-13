# logic: just check which substring starting from start is present in 'dict, 
# if it is present in dic then check for remaining string recursively and keep adding that to ans.

# Time Complexity: O(2^n). Because there are 2^n combinations in worst case i.e when every char is present in the dictiionary
# in this case for every char we will have two options either to chose that char or not
# space: O(n) recursive depth + O(n) for storing ans= O(n)

# Cross Q / follow up 
# NOte vvvi: "the same word in the dictionary may be reused multiple times in the segmentation.".
# Due to this only we are able to check if cur substring of 's' matches with any word in 'dict'.
# If same word of dict is not allowed mutiple times then, we will have to take visited set for dict words(index will work)
# to check whether the word at that index is already used or not.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans= []  # will store the final ans
        seg= []  # will store the matching segment
        self.helper(s, wordDict,seg,ans)
        return ans
    
    def helper(self,s,dict,seg, ans):
        if not s:
            # listToStr = reduce(lambda a, b : a+ " " +str(b), seg) # shorter way. 
            # listToStr= " ".join(str(e) for e in seg)   # or do like this
            listToStr = " ".join(seg)   # simpler and best
            ans.append(listToStr)
            return
        for i in range(1,len(s)+1):
            if s[:i] in dict:
                # if present in dict then, search for remaining 's'
                seg.append(s[:i])
                self.helper(s[i:],dict,seg,ans)
                # now backtrack so that it removes the current mapped string and found the new one
                seg.pop()


# Better one
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def helper(s, seg):
            if not s:
                ans.append(seg[: -1])   # removing the extra space at last
                return
            for i in range(1,len(s)+1):
                if s[:i] in wordsSet:
                    # if present in dict then, search for remaining 's'
                    helper(s[i:] , seg + s[: i] + " ")


        ans= []  # will store the final ans
        wordsSet = set(wordDict)
        helper(s, "")
        return ans

# Similar Questions:
# 1) "139. Word Break"
# https://github.com/Ravi-0412/DSA-Program-And-Notes/blob/main/Dynamic%20Programming/Matrix_Chain_Multiplication/Front%20Partitioning/139.%20Word%20Break.py

