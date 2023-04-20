# just same as Two sum.
# note: we can get pair either by adding any staring to last or adding any string to start of a string.
# But 1st here we are storing the count of each then applying "Two sum".
# applying twwo sum and updating freq in same iteration will be diffcult.

# 1st count the freq , then traverse the hashmap.

# here no need to check if we there is any string that we can add at start to get the target.
# checking adding adding at last will work fine since we are told to find the pair.
# if we are finding 'end' staring to add for a given 's' then we are indirectly calculating the result when we can get 'target' by adding at last for other staring as well.

# time: O(n*m) every time checking whether target starts with 's' or not. (n= len(nums), m= len(target))
# space: O(n)
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq= Counter(nums)  # just like we store freq using 'collections.defaultdict(int)' manually. 
        ans= 0
        for s, v in freq.items():
            n= len(s)
            if s== target[:n]:
                suffix= target[n: ]  # remaining string from end we need to form target by adding with 's'.
                ans+= v* freq[suffix]   # including all pairs
                if s== suffix :  # Here pair at same index also got added . so we have to remove the pair with same index that got added above in ans. 
                    ans-= v
        return ans


# method 2: simple and logical
# very nice approach
# we updating the freq at last to avoid duplicates.

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        prefix, suffix= Counter(), Counter()   # [length: count]
        ans= 0
        for s in nums:
            if target.startswith(s):  # then find the suffix freq(ending word freq) of remaining len
                ans+= suffix[len(target) - len(s)]
            if target.endswith(s):    # find the prefix freq (starting word freq) of remaining length.
                ans+= prefix[len(target)- len(s)]
            if target.startswith(s):
                prefix[len(s)]+= 1
            if target.endswith(s):
                suffix[len(s)]+= 1
        return ans
