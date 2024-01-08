# time: O(n) = space = O(n)

# Logic: we should include common element only one time.
# for first find the common ele.

# Then find the maximum unique ele we can include from both set of ararys without common one.
# and then add common one to get the final ans.

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1 = set(nums1)
        s2 = set(nums2)
        inter = s1.intersection(s2)
        # find out the element we can include from both excluding common one
        eleFromS1 = min((len(s1) - len(inter)), n //2)  # we can't include more than half
        eleFromS2 = min((len(s2) - len(inter)), n //2)
        return min(eleFromS1 + eleFromS2 + len(inter), n)
