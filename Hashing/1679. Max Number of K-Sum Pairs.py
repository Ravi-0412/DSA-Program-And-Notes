# method 1: Brute force
# time: O(n^2)
# just check every pair from each index.

# method 2: sort the array and apply "Two Sum for sorted array"
# time: O(n*logn)

# method 3: 

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
            remainingSum= k - n
            if remainingSum in numFrequency:
                count+= 1
                numFrequency[remainingSum]-= 1
                if numFrequency[remainingSum]== 0:
                    del numFrequency[remainingSum]
            else:  # if pair not found then only incr the count.
                numFrequency[n]+= 1
        
        return count
