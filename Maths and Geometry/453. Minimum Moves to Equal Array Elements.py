# Method 1:
# Logic: 
"""
Every move means select #n-1 numbers plus 1, which equals to select #1 number minus 1 relatively.
hence, just every number reduce to the minimum number.
i.e 
The problem description tells you that you should count how much moves (or sums) to make all values equal,
 always excluding one. So, we can think reversely i.e you can decrement only one element at a time relatively to other.

 Note: So just make all element equal to minimum_number.

i.e instead of 
[1,2,3] -> [2,3,3] -> [3,3,4] -> [4,4,4] = 3 moves

We do:
[1,2,3] -> [1,2,2] -> [1,1,2] -> [1,1,1] = 3 moves

    3 - 1 = 2
    2 - 1 = 1
    1 - 1 = 0
"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minNo = min(nums)
        ans = 0
        for num in nums:
            ans += num - minNo
        return ans
    
# Method 2: 
# logic: 
"""
sum: sum of all the numbers, before any moves; 
minNum : min number in the list; 
n: length of the list;

After, say m moves, we get all the numbers as x , and we will get the following equation

 sum + m * (n - 1) = x * n     ---> (i)

and actually,

  x = minNum + m
How 'x = minNum + m' ?
it comes from two observations:
i) the minNum number will always be minimum until it reachs the final number, 
because every move, other numbers (besides the max) will be increamented too.
ii) from above, we can get, the minum number will be incremented in every move. 
So, if the final number is x, it would be minNum + moves;

Now replace 'x' -> minNum + moves in '(i)' and simplify , you will get
  sum - minNum * n = m 
"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(nums) - min(nums) * n