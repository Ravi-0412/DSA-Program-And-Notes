# logic: if in any window if no of characters other than the most frequent char is <=k then that is valid case and we can update our ans
# ans we can replace these char with the most repeating char

# for this there is two approach:
# 1) make a dictionary of 26 letters of alphabet and every time(for each window) find the max frequency of a char from dictioinary
# and do the same thing done in code
# time: O(26*n)

# 2) just keep a varibale 'maxFreq' to count the max freq till now
# but here  keep an eye one thing that if maxfreq ele is at 'i'th index and suppose window is invalid then we will decr the freq of char at 'i'th index
# but there is no need to decr the maxFreq as after any window is invalid then you are decreasing the window size by incr 'i' and 
# if you will decr the max frequency also then your ans will not get updated as valid window is when: wind_size- maxFreq <=k 
#  so when you are incr window size you will want maxfreq to increase for new ans
# you will only get new ans when maxFreq will increase..That's why there is no need to decr teh maxFreq in invalid acse if maxFreq ele at 'i'th index

# Note: keep the above thing in mind, can be helpful in other problems also
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j, FreqCount, maxFreq, maxLength= 0, 0, {}, 0, 0
        while j <len(s):
            FreqCount[s[j]]= 1+ FreqCount.get(s[j],0)
            maxFreq= max(maxFreq, FreqCount[s[j]])
            wind_size= j-i+1
            if wind_size- maxFreq > k:   # if window is not valid then only incr the 'i' as we have to find the longest one. using while loop will give the incorrect ans 
                                        # as may be after decr the freq of one char we can get the valid window
                FreqCount[s[i]]-= 1     # in this no need top pop if freq becomes equal to zero as len(dic) will not matter here, there freq will matter only
                i+= 1
            else:  # valid 
                maxLength= max(maxLength, wind_size)
            j+= 1
        return maxLength

