# logic: https://leetcode.com/problems/power-of-heroes/solutions/3520202/c-java-python3-explanation-and-stepping-through-the-code/?orderBy=most_votes

# Only max and min matter , arrangement won't matter.
# So we can sort.

# For each element in the array, we will calculate the contribution of that element to the final answer. 
# The contribution will be the sum of two parts:

# a) The first part is the product of the square of the maximum element and the minimum element 
# when the current element is the only element in the subsequence.
# b) The second part is the sum of the product of the square of the maximum element and the minimum
# element when the minimum element is one of the elements from the prefix array.

# To calculate the first part(a), we can simply compute max*max*min where max and min are both equal to the current element.

# To calculate the second part(b), we need to use the variable pre. 
# We can iterate over all the previous elements and add the product of max*max (which is equal to the square of the current element)
# and the current minimum element. Since the minimum element can be one of the elements from the prefix array, 
# we can multiply this product by the number of times the minimum element appears in the prefix array.

# After calculating the contribution of the current element, we can update pre by setting it to pre*2 + current_element 
# and add the current contribution to res.

# Note: pre will keep track of the minimum elements of all the previous subsequences i.e
# All possible minimum elements * their possibility as minimum ele for next upcoming ele.


# In short: 
# Cur ele will be max till now and if we can keep track of all possible minimum ele with possibilty(count) as minimum ele
# then we can add the total contribution when we will include cur ele say nums[i].

# Note: say cur index is 'j' then any ele of previous indexes say 'i' will contribute as minimum ele
# 'j-i' no of times.

# But no need to compute 'pre' one by one , we can directly calculate pre = pre*2 + nums[i] using observation.
# i.e contribution of each pre ele is doubled and cur ele nums[i] will act as previous of one time for next upcoming element.

# Why multiplying 'pre' two times?
# suppose cur index is 'j' then till now max ele = nums[j]
# and we can consider any ele before index 'j' as minimum for cur max ele nums[j].
# for subarray till 'j' [i, j] , length of subarray = j -i + 1 say 'length'
# Now let we consider nums[k] as minimum (i <= k < j) then total number of choices when nums[j] is maximum
# will be equal to : "2^(length -2 )" i.e include / don't include any ele from remaining one.

# If any more ele will come , contribution will increase in same way i.e 2*pre for each ele.
# so directly multiplying pre by '2.

# time: O(n*logn)
# space = O(1)

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        n, mod = len(nums), 10**9 + 7
        nums.sort()
        pre = ans = 0
        # pre will keep track of the minimum elements of all the previous subsequences
        for i in range(n):
            ans = (ans + nums[i]**3 + nums[i]*nums[i]*pre) % mod
            pre = (pre*2 + nums[i]) % mod
        return ans

