# logic: if in any window if no of characters other than the most frequent char is <=k then that is valid case 
# and we can update our ans, we can replace these char with the most repeating char.

# Time = Space = O(n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        FreqCount = {}  # will count the freq count in cur window
        maxFreq = 0   # will store the maximum frequency of any char in cur window.
        maxLength= 0  # will store the ans
        while j < len(s):
            FreqCount[s[j]]= 1+ FreqCount.get(s[j],0)
            maxFreq= max(maxFreq, FreqCount[s[j]])
            # We can only make 'k' char equal to char having maxFreq , so remove the extra char from starting of window.
            # If char having maxFreq is at start then, also it won;t affect the ans. Take exmaple and see.
            while (j -i + 1) - maxFreq > k:   
                FreqCount[s[i]]-= 1     
                i+= 1
            maxLength= max(maxLength, j - i + 1)
            j+= 1
        return maxLength

