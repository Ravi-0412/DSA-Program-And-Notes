# Brute force: o(n^2)

# greedy: only that triplet can be the ans that will have value at all of its three places <= triplet value.
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

# Method 2:
"""
The idea is to take as much tuples as possible, but keep in mind that some of them are forbidden.
By forbidden I mean, that if we take this tuple, then maximum in one of the 3 places will be greater that what we need to get.
So, algorithm looks like this:

1) Iterate over all triplets once and create forbidden set.
2) Iterate over all triplets once again and update maximums.
3) Check that what we have in the end is equal to what we want.

Complexity
Time complexity is O(n), because we traverse our triplets twice. 
Space complexity is O(n) as well to keep forbidden set.
"""

class Solution:
    def mergeTriplets(self, triplets, T):
        forbidden = set()
        for i, [x, y, z] in enumerate(triplets):
            if x > T[0] or y > T[1] or z > T[2]:
                forbidden.add(i)
        
        a, b, c = 0, 0, 0
        for i, (x, y, z) in enumerate(triplets):
            if i not in forbidden:
                a, b, c = max(a, x), max(b, y), max(c, z)
                
        return [a, b, c] == T
