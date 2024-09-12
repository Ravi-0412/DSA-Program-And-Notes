# lOgic: 
"""
Given array A, we can compute an array diff where diff[i] = (A[0] + .. + A[i-1]) - (A[i] + .. + A[N-1]) (1 <= i < N),
i.e. sum of left part minus sum of right part.

If we don't do any replacement, the answer is the number of 0s in the diff array.

If we replace A[i] with k, then diff[1] to diff[i] decrease by d, and diff[i+1] to diff[N-1] increase by d, 
where d = k - A[i]. Again, the answer is the number of 0s in this new diff array.

Instead of changing the diff array (taking O(N) time), we can simply count the number of d in diff[1..i] 
and number of -d in diff[(i+1)..(N-1)] (taking O(1) time).

So, we can use two frequency maps L(initial_freq_sum_diff) and R(after_update_freq_sum_diff)
which are the frequency maps of diff[1..i] and diff[(i+1)..(N-1)] respectively.

We scan from left to right. For each A[i], we try to update ans with L[d] + R[-d] where d = k - A[i], 
and update the frequency maps.

Link: https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/solutions/1499365/c-frequency-map-o-n/
Go through example in above to understand more properly.
"""
# Time = Space = O(n)

class Solution:
    def waysToPartition(self, A, k):
        N = len(A)
        total_sum = sum(A)
        initial_freq_sum_diff = defaultdict(int)
        
        left_sum = 0
        for i in range(N - 1):
            left_sum += A[i]
            right_sum = total_sum - left_sum
            initial_freq_sum_diff[left_sum - right_sum] += 1

        after_update_freq_sum_diff = defaultdict(int)
        ans = initial_freq_sum_diff[0]  # If no replacement is done, answer is the number of `0`s in the frequency map
        
        left_sum = 0
        for i in range(N):
            left_sum += A[i]
            right_sum = total_sum - left_sum
            d = k - A[i]  # Difference if we replace A[i] with k
            ans = max(ans, after_update_freq_sum_diff[d] + initial_freq_sum_diff[-d])  # Get max of current result or new pivot count after replacement
            initial_freq_sum_diff[left_sum - right_sum] -= 1  # Transfer frequency from initial_freq_sum_diff to after_update_freq_sum_diff
            after_update_freq_sum_diff[left_sum - right_sum] += 1
         
        return ans
