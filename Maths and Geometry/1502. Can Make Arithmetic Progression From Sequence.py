# method 1: Brute force
# logic: just sort and check if diff between each adjacent pair is same.

# time: O(n*logn), space: O(1)

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff= arr[1] - arr[0]
        pre= arr[1]
        for i in range(2, len(arr)):
            if arr[i] - pre != diff:
                return False
            pre= arr[i]
        return True
    

# method 2: 
# logic: find the diff first.
# we get the max_number in AP using 'min_number + (n-1)*diff' . From this we can get the difference.
# diff= (max(nums) - min(nums)) / (n-1).

# then we have starting ele of AP and diff so we can check if next ele of sequence is present or not.
# next= min(nums) +  i * diff, i= 1, 2, 3,....n-1

# time= space= O(n)

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n= len(arr)
        s= set(arr)   # storing all unique ele in a set 's'.
        minimum= min(arr) # finding min ele of arr
        maximum= max(arr) # Finding max ele of arr
        diff= (maximum - minimum) /(n-1)  # finding the diff between ele
        for i in range(1, len(arr)):
            next= minimum + i * diff
            if next not in s:
                return False
        return True

# method 3: Try Later.
# optimising space to (1).
# time: O(n), space O(1)
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/solutions/720152/o-n-time-o-1-space/
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/solutions/721352/c-counting-sort-solution-with-o-n-and-o-1-complexity/