# here talking about sequence, so we can pick from anyone like subset
# so first sort the  given array according to the length 
# logic: just like LIS , just change the condition
# nect word can only form a chain if they differ by pre char by only one position 
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sorted_words= sorted(words, key= len)   # it will sort the each word in array according to their length
        LSC= [1]* len(words)   # LSC[i] indicates that 'Longest String Chain' that ends at index 'i'
        for curr in range(len(words)):  # calculating for each index one by one
            for pre in range(curr):     # take the values from all the pre index till now
                # if curr differ by pre by one position it means they are forming a chain. so include
                if len(sorted_words[curr])== len(sorted_words[pre]) + 1 and self.Compare(sorted_words[curr], sorted_words[pre])== True and LSC[curr] < 1+ LSC[pre]:         
                        LSC[curr]= 1+ LSC[pre]    
        return max(LSC)
    
    def Compare(self,curr,pre):
        i,j= 0,0
        count= 0
        while i <len(curr) and j < len(pre):
            if curr[i]== pre[j]:
                i,j= i+1, j+1
            else: # only move 'i' ahead as we have to count the position differences from pre word
                count+= 1  # just incr the count when they differ
                i+= 1
        if count>1 :  # differ at more than one position
            return False
        return True