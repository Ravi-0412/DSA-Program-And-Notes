# we will try to keep the max freq of any ele to minimise the deletion.
# FOr this we need to sort the string according to their freq in ascending order.

# After that traverse the sorted list from index '1'.
# upcoming index must have freq less than the preFreq  otherwise we need to delete some char from cur one.

# Note: At every step 'preFreq' will must decrease by '1' to avoid same freq char.

# Time : O(c*logc). max c = 26 as we are sorting freq of char and char possible is '26'(a to z).
# space= O(26)

class Solution:
    def minDeletions(self, s: str) -> int:
        charFreq = Counter(s)
        # print(charFreq)
        charFreqValues = sorted(charFreq.values(), reverse = True)  # we only need to care about freq.
        # print(charFreqValues)
        preFreq = charFreqValues[0]  
        # preFreq i.e next ele must have smaller freq than preFreq otherwise we need to delete some char from that.
        ans = 0
        for i in range(1, len(charFreqValues)):
            if charFreqValues[i] >= preFreq:
                # taking max with '0' to handle the case when 'preFreq=0'.
                # In this case we need to delete all occurence of char with cur freq.
                # Allowed 'preFreq -1' ho sakta h. extra sb delete karna hoga.
                ans += (charFreqValues[i] - max((preFreq -1), 0))  
            preFreq = min(preFreq - 1, charFreqValues[i])  # can't be more than this for next upcoming char.
        return ans


# Method 2: Very better and concise
# Same logic as above.
# Optimisation: Same freq can't be used again.
# So when we will see any used freq , we need to delete char till we find any used freq.

# Time: O(n), in total we need to traverse + delete = n(given constraint) space= O(26)

class Solution:
    def minDeletions(self, s: str) -> int:
        charFreq = Counter(s)
        seen = set()  # will store the freq we seen till now
        ans = 0
        for freq in charFreq.values():
            while freq > 0 and freq in seen:
                freq -= 1
                ans += 1
            seen.add(freq) # this added freq can't be freq of any char
        return ans