# Logic: Find the length of 'longest valid substring' from each index from right side.

# Time complexity: O(n * max_length_of_forbidden_words ^ 2) = 10^7.

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        forbidden_set = set(forbidden)
        ans = 0
        right = n - 1   # will keep track of where valid substring end. beyond this no need to check
        for left in range(n -1, -1, -1):
            # we only need to check only next 10 char from this index or till 'right' because '1 <= forbidden[i].length <= 10'.
            for k in range(left , min(left + 10 , right + 1)):
                if word[left : k + 1] in forbidden_set:
                    right = k - 1  # last valid substting will end at here only as including 'k' is leading to invalid substring.
                    break   # no need to check further from index 'left'
            ans = max(ans, right - left  + 1)  # max valid length of substring that we can get when we will start from 'left'.
        return ans
    
# Note: if 'k' grows then it is better to use 'Trie'.

# Trie vs Set

# Suppose that,

# 1 <= forbidden[i].length <= k
# In this problem, k = 10.

# When we use a set of forbidden words, to check if a substring beginning at 'i' is in forbidden_set, 
# we need to perform a slicing on the provided word.
# That is, for 1 <= j <= k, we need to perform word[i:j]. As you can see, this runs in O(k^2) time.

# If we use a Trie, we can keep track of the node in the trie as we move through the substring. 
# This means, we can store the node cb before we move on to cba, as node cba will be a child of node cb. That is O(k) time complexity.

# In this problem, k is small enough that a set will do just fine. As k grows, the runtime will start to favour using a trie.


# Note: Try by tries also.
# Easy only
# https://leetcode.com/problems/length-of-the-longest-valid-substring/solutions/3774799/python-sliding-window-trie/
# https://leetcode.com/problems/length-of-the-longest-valid-substring/solutions/3771520/python-hashmap-and-trie-solutions/