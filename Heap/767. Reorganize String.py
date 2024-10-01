# Note vvi: In this type of questions, focus on most frequent char first.
# And try to put them one after the other first.

# Here try to put the most frequent char just after other.

# Logic:  store pair of {frequency,char} in a Heap. Then while Heap.size()>1 , 
# at every iteration, take out the top two elements, append them to the ans string, 
# decrease their frequency by 1 and push them again in the Heap.

# When the loop will break, either the Heap became empty or of 1 size.

# If it's empty, return the ans string.
# if it has size == 1, check the remaining frequency of the top/last element, if its 1, append it and return ans.
# Otherwise, return ""

# Note: If there is some character c with freq(c)>(n+1)/2 then it is impossible


# Time: O(n*logn), space: O(n)

import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        frequency = collections.defaultdict(int)
        for i, c in enumerate(s):
            frequency[c] += 1
        
        maxHeap = []
        for key, value in frequency.items():
            maxHeap.append((-1* value, key))  
            # while inserting converting freq into negative to get the char with max freq first

        heapq.heapify(maxHeap)   # to get char with max freq on top
        while len(maxHeap) > 1:
            f1, c1 = heapq.heappop(maxHeap)
            f2, c2 = heapq.heappop(maxHeap)
            ans += c1 + c2
            f1 , f2 = -1*f1 - 1,  -1*f2 - 1   # converting into +ve
            if f1 > 0 :
                heapq.heappush(maxHeap, (-1*f1, c1))  
            if f2 > 0 :
                heapq.heappush(maxHeap, (-1*f2 , c2))
        if len(maxHeap) == 0:
            return ans
        f, c = heapq.heappop(maxHeap)
        if -1*f == 1:
            return ans + c
        return ""


# Method 2: 
# Most optimised

# Note: Keep this Q and logic in mind, it is used in a lot of problems.

# Logic: 
# We construct the resulting string in sequence: at position 0, 2, 4, ... and then 1, 3, 5, ...
# In this way, we can make sure there is always a gap between the same characters

# Consider this example: "aaabbbcdd", we will construct the string in this way:

# a _ a _ a _ _ _ _ // fill in "a" at position 0, 2, 4
# a b a _ a _ b _ b // fill in "b" at position 6, 8, 1
# a b a c a _ b _ b // fill in "c" at position 3
# a b a c a d b d b // fill in "d" at position 5, 7

# Note: 1st put the most frequent element.

# Time: O(n)

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        frequency = collections.defaultdict(int)
        maxLength , letter = 0 , None
        for c in s:
            frequency[c] += 1
            if frequency[c] > maxLength:
                maxLength = frequency[c]
                letter = c

        if maxLength > (n + 1)//2:
            return ""
        # 1st put the char at even index i.e 0, 2, 4, 6,..
        # Then put at odd index i.e 1, 3, 5,...
        ans = [None] * n
        # first put the most frequent char i.e letter
        ind = 0
        while frequency[letter] > 0:
            ans[ind] = letter
            ind += 2   # putting with gap to avoid same char together
            frequency[letter] -= 1
        # Now place remaining char after index 'ind' if got filled till last then start from index 1, 3, 5,...
        for c in s:
            while frequency[c] > 0:
                if ind >= n:
                    ind = 1  # start putting from index '1'.
                ans[ind] = c
                ind += 2
                frequency[c] -= 1
        return "".join(ans)

# Java equivalent of 2nd method: 

# class Solution {
#     public String reorganizeString(String S) {
#         int[] hash = new int[26];
#         for (int i = 0; i < S.length(); i++) {
#             hash[S.charAt(i) - 'a']++;
#         } 
#         int max = 0, letter = 0;
#         for (int i = 0; i < hash.length; i++) {
#             if (hash[i] > max) {
#                 max = hash[i];
#                 letter = i;
#             }
#         }
#         if (max > (S.length() + 1) / 2) {
#             return ""; 
#         }
#         char[] res = new char[S.length()];
#         int idx = 0;
#         while (hash[letter] > 0) {
#             res[idx] = (char) (letter + 'a');
#             idx += 2;
#             hash[letter]--;
#         }
#         for (int i = 0; i < hash.length; i++) {
#             while (hash[i] > 0) {
#                 if (idx >= res.length) {
#                     idx = 1;
#                 }
#                 res[idx] = (char) (i + 'a');
#                 idx += 2;
#                 hash[i]--;
#             }
#         }
#         return String.valueOf(res);
#     }
# }


# Heap solution using Java: 
# https://leetcode.com/problems/reorganize-string/solutions/970413/my-java-solution-using-priorityqueue-and-taking-the-count/
