# logic: result[i] the sum of min values of those subarrays (ending with i-th element).
# No of subarrays ending with ele at 'i'th index= (i+1).
# Reason: 'i' subarray to which curr ele will get added at last and one singular subarray of arr[i].
# vvi: if we find any previous ele smaller say at index 'j' than A[i] (j <i) then res[i]= res[j] + (i-j) * arr[i].
# => res[j]= sum of ans till 'j'(j+1 subarray) index and (i-j)* arr[i]= because for this much subarray(j-i) ,arr[i] is minimum so doing multiplication.
# fianlly total no of subarray at 'i'th index= j +1 + (i-j)= i +1. verified.
# since we are using the last pre calculated value again and again so stack should come into mind. 

# time= space= O(n)
# https://leetcode.com/problems/sum-of-subarray-minimums/solutions/257811/python-o-n-slightly-easier-to-grasp-solution-explained/
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n= len(arr)
        res= [0]*n
        stack= []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:  # keep on poping until you find any ele smaller than arr[i].
                stack.pop()
            if stack: # we have found the smaller ele than 'i'.
                j= stack[-1]
                res[i]= res[j] + (i-j)*arr[i]
            else:  # arr[i] is the smallest ele till now.
                res[i]= (i+1)* arr[i]
            stack.append(i)
        return sum(res) % (10**9 + 7)     #  return sum(res) % (10**9 + 7): giving incorrect ans

# Note vvvi: Key words

# Subarray + sum -> prefix sum
# Subarray + minimum -> mono stack