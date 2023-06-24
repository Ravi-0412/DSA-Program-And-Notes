# Time : O(2*n)

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        visited= set()  # To check the reverse pair and avoid counting same pair again
        count = 0
        for w in words:
            if w not in visited and w[::-1] in visited:
                count += 1
            visited.add(w)
        return count
        