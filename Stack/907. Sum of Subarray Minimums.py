# logic: result[i] the sum of min values of those subarrays having ending at index 'i'.

# No of new subarrays that will form after adding ele at 'i'th index= (i+1).
# Reason: 'i' subarrays to which curr ele will get added at last and one singular subarray of arr[i].

# vvi: if we find any previous ele smaller than A[i] say at index 'j' (j <i) then res[i]= res[j] + (i-j) * arr[i].
# Explanation:
# index 'i' to 'j + 1' tak  ka minimum ele arr[i] . no of such new subarray for which arr[i] will be minimum is
# 'i - j' so total sum from here = (i-j) * arr[i]

# And for remaining 'j + 1' newly formed subarray after adding arr[i], arr[j] will be minimum so adding res[j].

# fianlly total no of subarray at 'i'th index= j +1 + (i-j)= i +1. verified.

# Why stack?
# We have to find the next smaller ele on left for each nums[i].

# time= space= O(n)

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n= len(arr)
        res= [0]*n
        stack= []
        for i in range(n):
            # Find samller ele for nums[i] on left.
            # keep on poping until you find any ele smaller than arr[i].
            while stack and arr[stack[-1]] >= arr[i]:  
                stack.pop()
            if stack: # we have found the smaller ele than 'i'.
                j= stack[-1]
                res[i]= res[j] + (i-j)*arr[i]
            else:  # arr[i] is the smallest ele till now.
                res[i]= (i+1)* arr[i]
            stack.append(i)
        return sum(res) % (10**9 + 7) 

# Note vvvi: Key words

# Subarray + sum -> prefix sum
# Subarray + minimum / maximum-> mono stack