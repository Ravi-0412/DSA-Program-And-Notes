# Logic: what if nums[0] = 0 ?
# If nums[0] is 0, then the only way to change it to 1 is by doing an operation on the first 3 elements of the array.

# so just do the same for every element.
# if you see any element = 0 then flip next 2 elements.

class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length;
        int ans = 0;
        for(int i = 0 ; i < n; i ++) {
            if(nums[i] == 0) {
                if(i + 2 >= n)
                // No sufficient elements to flip to make value at this index = 1
                    return -1 ;
                nums[i] = 1;   # No need of this
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
                ans += 1 ;
            }
        }
        return ans;
    }
}
