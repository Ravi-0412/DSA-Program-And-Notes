class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        # negativeCount is used to count the number of negative numbers from zeroPosition to current index 'i' 
        # zeroPosition : index of last seen zero and indexOfFirstNegative : will denote the index of 1st negative number after we have seen last zero 
        indexOfFirstNegative , zeroPosition = -1, -1
        negativeCount , ans = 0, 0
        for i in range(n):
            if nums[i] == 0:
                indexOfFirstNegative , zeroPosition, negativeCount = -1, i, 0
            if nums[i] < 0:
                negativeCount += 1
                # we only need to know index of first negative number
                if indexOfFirstNegative == -1:
                    indexOfFirstNegative = i
            # update ans
            if(negativeCount % 2 == 0):
                # in this case whole subarray after last seen '0' will be our ans
                ans = max(ans, i - zeroPosition)
            else:
                # in this we need to remove the first seen negative number
                ans = max(ans, i - indexOfFirstNegative)
        return ans

# Java
"""
class Solution {
    public int getMaxLen(int[] nums) {
        int n = nums.length;
        // negativeCount is used to count the number of negative numbers from zeroPosition to current index 'i'
        // zeroPosition : index of last seen zero and indexOfFirstNegative : will denote the index of 1st negative number after we have seen last zero
        int indexOfFirstNegative = -1, zeroPosition = -1;
        int negativeCount = 0, ans = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                indexOfFirstNegative = -1;
                zeroPosition = i;
                negativeCount = 0;
            } else {
                if (nums[i] < 0) {
                    negativeCount++;
                    // we only need to know the index of first negative number
                    if (indexOfFirstNegative == -1) {
                        indexOfFirstNegative = i;
                    }
                }
                // update ans
                if (negativeCount % 2 == 0) {
                    // in this case whole subarray after last seen '0' will be our answer
                    ans = Math.max(ans, i - zeroPosition);
                } else {
                    // in this case, we need to remove the first seen negative number
                    ans = Math.max(ans, i - indexOfFirstNegative);
                }
            }
        }

        return ans;
    }
}

"""
