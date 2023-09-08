# Logic: Find the minimum and maximum and store the indices of minimum and maximum in a list.
# Note: Minimum swap will be equal to: 
# ans = bring the last maximum ele at 'n-1'th index + bring the 1st minimum ele at '0'th index

# VVI: But while bringing the 1st minimum ele at '0'th index last maximum ele may also get swapped
# so to bring the last maximum ele at 'n-1'th index , we will need '1' less swap.

# Therefore in this case, we will subtract '1' from ans.

class Solution:
    def minimumSwaps(self, nums):
        n  = len(nums)
        minEle , maxEle = min(nums) , max(nums)
        minEleIndices , maxEleIndices = [] , []
        for i, num in enumerate(nums):
            if num == minEle:
                minEleIndices.append(i)
            if num == maxEle:
                maxEleIndices.append(i)
        swaps = 0
        swaps += (n - 1) - maxEleIndices[-1]  # to bring the last maximum ele at 'n-1'th index
        swaps += minEleIndices[0]             # to bring the 1st minimum ele at '0'th index
        # Now check if last maximum ele get swapped automatically while bringing the 1st minimum ele at '0'th index
        if maxEleIndices[-1] < minEleIndices[0]:  
            swaps -= 1
        return swaps

s= Solution()
arr = [3,4,5,5,3,1]
arr = [9]
arr = [1,3,5,2,8]
arr = [10, 8, 6, 2, 2, 12, 9, 12]
print("minimum no of swaps needed is : ", s.minimumSwaps(arr))