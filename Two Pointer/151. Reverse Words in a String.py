# Time = O(n)
# Space = O(n), excluding answer one.

class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(list(s.strip().split(" "))[::-1])
        # return " ".join(list(s.strip().split())[::-1])
        # return " ".join(s.strip().split()[::-1])
        return " ".join(s.split()[::-1])
        