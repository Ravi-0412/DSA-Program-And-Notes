# method 1: sort the array and apply "Two Sum for sorted array"
# time: O(n*logn)

# method 2: 

# just applied normal two sum.
# but instead of storing 'index' as value, storing frequency since there can be more than same pair.

# when we find any pair then we will incr the ans += 1
# And we will decr the frequency count of 'remainingSum' and in this case we won't incr the count of curr 'n',
# because this pair got used in the ans.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numFrequency= collections.defaultdict(int)
        count= 0
        for n in nums:
            remainingSum = k - n
            if remainingSum in numFrequency:
                count+= 1
                numFrequency[remainingSum]-= 1
                if numFrequency[remainingSum]== 0:
                    del numFrequency[remainingSum]
            else:  # if pair not found then only incr the count.
                numFrequency[n]+= 1
        
        return count


# Note: Whenever you are asked to find pairs then think of 'Two sum' logic and
# Store the 'frequency' as value because pair at different index will also add to ans. 