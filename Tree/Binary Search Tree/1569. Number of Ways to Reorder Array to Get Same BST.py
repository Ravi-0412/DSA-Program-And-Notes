# logic: 1) we have to reorder elements in such a way that we get the same BST,
# when we add the elements in given order to an empty tree.

# 2) so first ele must be root.val then only you can get the same BST.

# And for above conditions we have to keep the relative order same of both left and right subtree respectively.
# (If you will not maintain the relative order in both then you won't get the same BST).


# How we get that formula?
# Suppose we have two finite, ordered sequences x=(x1,…,xm)
# and y=(y1,…,yn).
# How many ways can we create a new sequence of length m+n from x and y
# such that the relative order of the digits from the same sequence(array) remain preserved?

# Ans:
# This is the same as taking m+n places, and deciding which of them get the xi or yi
# , i.e., com(m + n , m) or comb(m + n, n) = (n + m)! //(m! * n!)

# There are m + n total positions. If we put m elements from left(smaller value than root) in randomly chosen m positions (but, in order), 
# we can put the rest(right) in other remaining positions. (right: greater values than root)
# (Equivalently, we could also have chosen to fill n arbitrary positions from right and fill remaining from whatever positions are left.)

# TIME: o(n^2)

class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        def dfs(nums):
            if len(nums) <= 2:
                return 1
            left = [v for v in nums if v <  nums[0]]   # left subtree ele if nums[0] is root
            right = [v for v in nums if v > nums[0]]   # right subtree ele if nums[0] is root
            return comb(len(left) + len(right), len(right)) * dfs(left) * dfs(right)   # just maths
        
        return (dfs(nums) -1) % (10**9 + 7)   # '-1' for given initial array

