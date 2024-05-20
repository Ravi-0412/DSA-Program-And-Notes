# Brute force:
# Just calculate the 'prefix' and 'suffix' multiplication then, 
# ans[i] = prefix[i - 1] * suffix[i + 1]

# Method 2: 
# Optimising space

# we have to do in O(1) space complexity except ans array.
# means we will have to store prefix and suffix into a variable instead of array.

# 1) Traverse from left to right and store the 'prefix' for each ele.
# 2) for 'suffix' traverse right to left.
# time: O(n),space: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans= [1]*(len(nums))
        # first storing the prefix mutliply for each number in 'ans'
        prefix= 1
        for i in range(len(nums)):
            ans[i]= prefix
            prefix= prefix* nums[i]
        # now calculate the postfix and store the final ans in the 'ans'.
        postfix= 1
        for i in range(len(nums) -1, -1, -1):
            ans[i]= ans[i] * postfix   # ans[i] store the prefix for that index and postfix is storing suffix.
            postfix= postfix * nums[i]
        return ans


# observation:
# 1) if count of '0' will be = 1 then all elements will have value= 0 excecpt the '0'th ele.
# 2) if count of '0' >= 2 then value= 0 for all elements.


# Java
# Link: https://leetcode.com/problems/product-of-array-except-self/solutions/1342916/3-minute-read-mimicking-an-interview/
"""
# Method 1:

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int pre[] = new int[n];
        int suff[] = new int[n];
        pre[0] = 1;
        suff[n - 1] = 1;
        
        for(int i = 1; i < n; i++) {
            pre[i] = pre[i - 1] * nums[i - 1];
        }
        for(int i = n - 2; i >= 0; i--) {
            suff[i] = suff[i + 1] * nums[i + 1];
        }
        
        int ans[] = new int[n];
        for(int i = 0; i < n; i++) {
            ans[i] = pre[i] * suff[i];
        }
        return ans;
    }
}

# method 2:

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int ans[] = new int[n];
        Arrays.fill(ans, 1);
        int curr = 1;
        for(int i = 0; i < n; i++) {
            ans[i] *= curr;
            curr *= nums[i];
        }
        curr = 1;
        for(int i = n - 1; i >= 0; i--) {
            ans[i] *= curr;
            curr *= nums[i];
        }
        return ans;
    }
}

"""