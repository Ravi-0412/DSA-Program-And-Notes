# Brute force: o(n^2)

# greedy: only that triplet can be the ans that can will have value at all of its three places <= triplet value.
# time: O(n)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # ans= [] # this won't work in case of more than one possible ans since it can't eliminate duplicates.
        ans= set()
        for t in triplets:
            # if any of the three value is greater than the target then that triplet can't be the part of ans
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            # now check triplet that can be the ans, can lead to target triplet or not.
            # if any of the triplet can form the value at each of the three position means possible else not
            for i, v in enumerate(t):  # for comparing the value of triplet and target at same time. 
                            # since 't' is an array so each val in 't' will get assigned to index
                if v== target[i]:
                    ans.add(i)  # adding the index to ans
        return len(ans)== 3
