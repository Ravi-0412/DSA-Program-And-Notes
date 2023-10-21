
# ans = bring the last maximum ele at 'n-1'th index + bring the 1st minimum ele at '0'th index

# VVI: But while bringing the 1st minimum ele(say at index 'i') at '0'th index last maximum ele may also get swapped
# so to bring the last maximum ele(say at inex 'j') at 'n-1'th index , we will need '1' less swap 
# when i > j

# Therefore in this case, we will subtract '1' from ans.

class Solution:
    def minimumSwaps(self, nums):
        n  = len(nums)
        minEle , maxEle = min(nums) , max(nums)
        first_index_min , last_index_max = n-1, 0
        for i, num in enumerate(nums):
            if num == minEle:
                first_index_min = min(first_index_min, i)
            if num == maxEle:
                last_index_max = max(last_index_max, i)
        swaps = 0
        swaps += (n - 1) - last_index_max  # to bring the last maximum ele at 'n-1'th index
        swaps += first_index_min             # to bring the 1st minimum ele at '0'th index
        # Now check if last maximum ele get swapped automatically while bringing the 1st minimum ele at '0'th index
        if last_index_max < first_index_min:  
            swaps -= 1
        return swaps

s= Solution()
arr = [3,4,5,5,3,1]
arr = [9]
arr = [1,3,5,2,8]
arr = [10, 8, 6, 2, 2, 12, 9, 12]
print("minimum no of swaps needed is : ", s.minimumSwaps(arr))