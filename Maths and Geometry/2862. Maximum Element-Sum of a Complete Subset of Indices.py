# Index having same remaining no after dividing by perfect square will form a subset.
# E.g: [1,4,9,16, ....], [2, 8, 18, 32,...], [3,12,27,48,....] ...
# for each starting index , multiply by '4','9','16','25',..(with perfect square) to get the next no.

# So in this way: 1, 4,9,16,25,..(perfect square) will have remaining no = 1 after dividing by perfect square, 
# 2, 8, 18, 32,...will have remaining no = 1 after dividing by perfect square and so on.

# Time = O(n * (root(1) + root(2) + root(3) + ..))


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        subsetSum = collections.defaultdict(int)
        n = len(nums)
        ans = 0
        # find the remaining number after perfect square for each index.
        # Index having same remaining part will form the susbet.
        # Our ans will be maximum of those subset sum.
        for i in range(n):
            cur = i + 1   # converting into 1-indexing
            j = 2
            # finding the remaining no after perfect square.
            # we only need to go till square root(j)
            while j *j <= cur:
                # if divisible by perfect sqaure then , continue dividing
                if cur % (j *j) == 0:
                    while cur % (j *j) == 0:
                        cur = cur // (j *j)
                j += 1
            # after this 'cur' will be the remaining no only.
            # and nums[i] will be form subset with ele having same remaining no i.e 'cur'
            subsetSum[cur]+= nums[i]
            ans= max(ans, subsetSum[cur])
        return ans