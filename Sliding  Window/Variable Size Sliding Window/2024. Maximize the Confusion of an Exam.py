# Exactly same as "1004. Max Consecutive Ones III".

# Only diff is: we can get our ans as "consecutive T" or "consecutive F".
# so we will have to check for both.

# Time : O(n)

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n= len(answerKey)
        i, j= 0, 0
        count = 0
        ans = 0
        while j < n:
            if answerKey[j] == 'F':
                count += 1
            while i <= j and count > k:
                if answerKey[i] == 'F':
                    count -= 1
                i += 1
            ans = max(ans, j- i + 1)
            j += 1
        
        i, j= 0, 0
        count = 0
        while j < n:
            if answerKey[j] == 'T':
                count += 1
            while i <= j and count > k:
                if answerKey[i] == 'T':
                    count -= 1
                i += 1
            ans = max(ans, j- i + 1)
            j += 1
        return ans


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
