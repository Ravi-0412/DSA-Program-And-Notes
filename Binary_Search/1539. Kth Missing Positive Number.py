# logic: our ans may like betweeen [1, n + k]  (max range: when there is no missing number and num is starting from '1'.)
# store the given arr into set so that we can check in O(1).

# search number in our range i.e if they are present or not.
# if not present then decr k by '1'. and when k reaches '0' 'n' will give the ans.

# time: O(n)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num_set= set(arr)
        for n in range(1, len(arr) +k +1):
            if n not in num_set:
                k-= 1
            if k== 0:
                return n

# method 2:
# Note that the array is in strictly increasing order and hence there is no repetition.
# Think of this case, if every element in the array > k , the answer would be k.
# So, for every element <= k , you need to increment k. (i.e. when you iterate from left to right).
# And since the array is in increasing order, you can break out of the loop on the first instance this condition fails.

# time: O(n)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for n in arr:
            if n <= k:  # abhi tak ka sara ele 'k' se chota h then ans or bda hoga. so incr 'k'.
                k+= 1
            else:  # means all element from now onwards is greater than k.
                break
        return k

# method 3: using Binary Search.
# conversion of method 2 only but have to think in very deep.
# logic: we are mainating another array say 'B' where
# B[i]= arr[i] - i- 1   # which denotes how many missing positives so far at index i that is smaller than K. (i=> mid)
# So the question becomes: finding the largest index of array B so that B[j] is smaller than K.
# It is the same as finding first/last occurrence

# vvi(analyse this properly) here index can lie from '0' to 'n' (n when last ele is smaller than k).

# Reason: After while loop is stopped, l - 1 is our target index because, 
# B[l - 1] represents how many positive is missing at index l - 1 that is smaller than K, so result is A[l -1]
# (the largest number in A that is less than result) + K - B[l - 1](offset, how far from result) = (A[l - 1]) + (k - (A[l - 1] - l)) = l + k.

# https://leetcode.com/problems/kth-missing-positive-number/solutions/779999/java-c-python-o-logn/
# read comment by 'ryz' in above link for more clarity.
# analyse this very properly and try to bring in the format i solve the Q.
# time: O(logn)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n= len(arr)
        start, end= 0, n    # here is the doubt i used to take 'n-1' always(i.e last possible ans) but here when i took 'n-1' then gave incorrect ans.
        while start < end:
            mid= start + (end- start)//2
            if arr[mid] - mid -1 < k:    # checking in virtual array 'B'
                start= mid + 1
            else:
                end= mid
        return start + k