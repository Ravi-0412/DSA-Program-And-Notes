"""
1st sort the array for better traversing and checking.

if the sum of three numbers is less than the target, then any number smaller than our current "right" pointer will also result in a sum less than the target.
    Sort the array.
    Iterate through the array with index i, treating nums[i] as the first element of our triplet.
    Set two pointers for the remaining portion of the array: left = i + 1 and right = n - 1.
    Check the sum: * If nums[i] + nums[left] + nums[right] < target:
    * Since the array is sorted, every element between left and right would also satisfy the condition when paired with nums[i] and nums[left].
    * We add right - left to our total count.
    * Move the left pointer forward to try a larger sum.
        Otherwise, the sum is too large:
            Move the right pointer backward to decrease the sum.

Time : O(n^2), space : O(1)
"""

class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < target:
                    # If nums[i] + nums[left] + nums[right] < target,
                    # then all elements between left and right also work
                    # as the third element.
                    count += (right - left)
                    left += 1
                else:
                    # Sum is too high, need a smaller value from the right
                    right -= 1
                    
        return count


# Follow ups:
"""
In the standard "3Sum Smaller" problem, we are looking for index triplets (i,j,k), so duplicates in the values don't matter—the indices make them unique. 

However, if the question asked for unique value combinations that sum to less than a target, the logic shifts.
To find unique triplets, you must skip over duplicate values during the iteration to ensure you aren't counting the same combination of numbers twice.

i) Skip i duplicates: Prevents us from starting a triplet with the same number twice.
ii) Handle left and right carefully: Unlike the "equals" version, when we find a valid sum, we can't just jump. We need to collect the unique combinations between left and right.
"""


def threeSumSmallerUnique(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # 1. Skip duplicate starting numbers
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < target:
                # 2. We found a valid range. 
                # Since we want UNIQUE values, we can't just do (right - left).
                # We need to iterate from left to right and pick unique pairs.
                temp_right = right
                while temp_right > left:
                    result.append([nums[i], nums[left], nums[temp_right]])
                    
                    # Skip duplicate values for the 'right' element
                    while temp_right > left and nums[temp_right] == nums[temp_right - 1]:
                        temp_right -= 1
                    temp_right -= 1
                
                # 3. Skip duplicate values for the 'left' element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                left += 1
            else:
                # Sum too big, move the right pointer down
                right -= 1
                
    return result
