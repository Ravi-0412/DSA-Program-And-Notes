# Exactly same as "1004. Max Consecutive Ones III".

# Only diff is: we can get our ans as "consecutive T" or "consecutive F".
# so we will have to check for both.

# Time : O(n)

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        # Helper function to find the max length of a window containing 
        # at most 'k' characters that are NOT the 'target' character.
        def getMaxWindow(target: str) -> int:
            left = 0
            other_count = 0  # Counts how many characters we've "flipped"
            max_len = 0
            
            for right in range(len(answerKey)):
                # If current char is NOT our target, it costs us 1 flip
                if answerKey[right] != target:
                    other_count += 1
                
                # If we've exceeded k flips, shrink the window from the left
                while other_count > k:
                    if answerKey[left] != target:
                        other_count -= 1
                    left += 1
                
                # Update the maximum window size found so far
                max_len = max(max_len, right - left + 1)
                
            return max_len

        # The answer is the best we can do by either 
        # trying to make a long string of 'T's or a long string of 'F's.
        return max(getMaxWindow('T'), getMaxWindow('F'))


# Method 2: In one pass

# How to reduce?
# Logic: window can't have both i.e 'T' & 'F' count > k to get the optimal one.
# So in any window if count of both is > k then, we will remove from left side.

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        i, j= 0, 0
        countT , countF = 0, 0
        ans = 0
        while j < n:
            if answerKey[j] == 'T':
                countT += 1
            else:
                countF += 1
            while countT > k and countF > k:
                if answerKey[i] == 'T':
                    countT -= 1
                else:
                    countF -= 1
                i += 1
            ans = max(ans , j - i + 1)
            j += 1
        return ans
