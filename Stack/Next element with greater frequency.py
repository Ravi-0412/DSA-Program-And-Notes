"""
Just same as find next greater element on right, just check the frequency here ,
Instead of checking the value.

So 1st find the freq of each element and store in hashmap,, after that this question reduces to 'Find next element on right'
having greater frequency.
"""


# Time = space = O(n)
from collections import defaultdict

class Solution:
    def print_next_greater_freq(self,arr,n):
        freq = defaultdict(int)
        for num in arr:
            freq[num] += 1
            
        ans = [-1]* n
        stack = []
        for i in range(n):
            while stack and freq[arr[stack[-1]]] < freq[arr[i]]:
                ans[stack.pop()] = arr[i]
            stack.append(i)
        return ans
