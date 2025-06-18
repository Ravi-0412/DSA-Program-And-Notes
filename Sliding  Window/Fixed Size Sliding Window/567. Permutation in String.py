# Method 1: 
# fully 100% same as "438. Find All Anagrams in a String" only
# here if you find any anargam then return true else return False instead of adding them into ans

# Time = space: O(n)

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        count_s1 = Counter(s1)
        window = Counter(s2[:len1])

        if count_s1 == window:
            return True

        for i in range(len1, len2):
            start_char = s2[i - len1]
            end_char = s2[i]

            # Slide the window: remove start_char, add end_char
            window[end_char] += 1
            window[start_char] -= 1

            if window[start_char] == 0:
                del window[start_char]

            if window == count_s1:
                return True

        return False
