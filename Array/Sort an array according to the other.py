# count the freq of each ele in Arr1.
# then traverse arr2, and append the cur ele of arr2 in ans no of times= frequency.
# and make freq of these ele= 0

# for remaining ele which is not in arr2, we have to simply add in sorted order.
# for this store all keys in a list, sort the list.
# then traverse the list, and if its freq is != zero, then add that num to ans, no of times= frequency.

# time: O(n + n*logn)= O(nlogn)

from collections import Counter
class Solution:
    
    def relativeSort (self,A1, N, A2, M):
        freq= Counter(A1)
        ans= []
        for n in A2:
            ans.extend([n]*freq[n])  # add manullay 'n' for 'freq[n]' no of times.
            freq[n]= 0
        keysList= list(freq.keys())
        keysList.sort()
        for n in keysList:
            if freq[n]!= 0:
                ans.extend([n]*freq[n])
        return ans
