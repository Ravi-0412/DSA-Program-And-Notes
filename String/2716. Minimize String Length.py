# logic: All duplicate will get discarded, only distinct char will left.
# time: O(n)

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
