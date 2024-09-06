# Method 1: Brute force
# Logic: Just try to make every ele = 0 from start.

# More explanation in notes, page: 77

# Time : O(n * k)  , TLE

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue
            if i + k -1 >= n:
                # not suffficient no of ele to inlcude to inlcude to make subarray of size = k starting from index 'i'.
                return False
            operations= nums[i]
            # Reduce the next 'i+k' ele including cur ele by 'num[i]'.
            for j in range(i, i + k):
                nums[j] -= operations
                if nums[j] < 0:
                    # means not possible
                    return False
        return True


# Method 2: PrefixSum + Greedy + Sliding window
# Needs a lot of visualisation.

# More explanation in notes, page: 78

# https://www.youtube.com/watch?v=gGJhgzIHkCY&t=3238s
# https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/solutions/3739101/java-c-python-greedy-sliding-window/


# Time : O(n)
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        impact = 0  # will tell the overall impact of pre 'i-k' ele. will tell minimum no of times, we have to reduce the next ele.
                    # Basically storing:  sum of previous k - 1 element i.e A[i - 1] + A[i - 2] + A[i - k + 1] after each step
        for i in range(n):
            if impact > nums[i] :
                # cur number will become negative after subtracting impact so not possible
                return False
            nums[i] = nums[i] - impact  # After impact cur ele value will equal to this only. 
                                        # This is also the extra impact that it will add to existing impact..
            impact += nums[i]    # Adding the extra impact that it will add to make himself '0' on next numbers.
            # we have to remove the impact of 'i-k' element for next ele . Since ele of that ele will be till this index only.
            if i - (k -1) >= 0:
                impact -= nums[i - (k -1)]
        return impact == 0  # if impact != 0 means for making last ele = 0 , we need to reduce some more ele beyond our array.


# Method 3:
# Just the same logic as above. 
# Try to understand and visualise this properly.

# https://www.youtube.com/watch?v=bL4Fs2NBGxA


# Solve this Q also: "370: Range Addition"  (Lc premium) based on same logic.
# Link: https://www.lintcode.com/problem/903/   (of lintcode)

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        impactPrefix = [0] * (n + 1)  # '+1' because we are subtarcting the impact just '1' ele after the subarray starting from index 'i'.
        impactPrefix[0] += nums[0]  # for making nums[0] = 0 , we need operations = nums[0] only
        impactPrefix[k] -= nums[0]  # since the impact of cur ele i.e indeex 'i' will be till next 'k-1' index only.
                                    # so will subtract the impact of index 'i' after next 'k-1' ele.

        for i in range(1, n):
            impactPrefix[i] += impactPrefix[i -1]
            # impactPrefix[i] : will tell minimum no of operations we need to perform here.

            if impactPrefix[i] == nums[i]:
                continue
            # if performing this much operation if value goes in negative OR if there is no further ele to exist in subarray to make size = 'k'
            if impactPrefix[i] > nums[i] or (i + k - 1) >= n:
                return False
            # if impactPrefix[i] == nums[i]:   # writing this here will give wrong  ans due to '(i + k - 1) >= n'.
            #     continue
            
            # if nums[i] > 'minimum no of operations we need to perform here i.e 'impactPrefix[i]' 
            extraOperations = nums[i] - impactPrefix[i]
            impactPrefix[i] += extraOperations  # overall impact that will be carry forward
            impactPrefix[i + k] -= extraOperations   # will impact till 'i + (k-1)' only.
        print(extraOperations)   # will give the same initial array only in case of 'True'. Have to think why?
        return True


        