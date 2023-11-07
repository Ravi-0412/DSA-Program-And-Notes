# just same as Two sum.

# note: we can get pair either by adding any string to last or adding any string to start of a string.
# i.e any current string can be added at 'last' or at 'start' to get 'target'.

# so 1st count the freq , then traverse the hashmap.

# here no need to check if we there is any string that we can add at start to get the target separately.
# It will give duplicate pair.

# time: O(n*m) every time checking whether target starts with 's' or not. (n= len(nums), m= len(target))
# space: O(n)
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq= Counter(nums)  # just like we store freq using 'collections.defaultdict(int)' manually. 
        ans= 0
        for s, v in freq.items():
            n= len(s)
            if s== target[:n]:
                # if target starts with 's'
                suffix= target[n: ]  # remaining string from end we need to form target by adding with 's'.
                ans+= v* freq[suffix]   # including all pairs
                if s== suffix :  # Here pair at same index also got added . so we have to remove the pair with same index that got added above in ans. 
                    ans-= v
        return ans
    


# Method 2:
# To avoid duplicates separately in method 1

# note: we can get pair either by adding any string to last or adding any string to start of a string.
# i.e any current string can be added at 'last' or at 'start' to get 'target'.

# So here we will need two hashamp , one to check from last(Suffix) and one to check from start(Prefix).

# Here we can store the [length : count] instead of [word: count] for easier one.
# only store if either word starts or end with cur word.

# time: O(n*m) every time checking whether target starts with 's' or not. (n= len(nums), m= len(target))
# space: O(n)

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        prefix, suffix= Counter(), Counter()   # [length: count]
        ans= 0
        for s in nums:
            if target.startswith(s):  # then find the suffix freq(ending word freq) of remaining len
                ans+= suffix[len(target) - len(s)]
            if target.endswith(s):
                # find the prefix freq (starting word freq) of remaining length.    
                ans+= prefix[len(target)- len(s)]
            # Now add length of this word to both 'prefix' and 'suffix'
            # if target starts and end with 's'.
            if target.startswith(s):
                prefix[len(s)]+= 1
            if target.endswith(s):
                suffix[len(s)]+= 1
        return ans


# Method 3:
# More simpler and logical

# Logic: store the freq first since any word can come at start or end.
# Then, check for every index in 'target' for prefix and suffix.


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq= Counter(nums)  # just like we store freq using 'collections.defaultdict(int)' manually. 
        ans= 0
        for i in range(1, len(target)):
            s1 = target[: i]
            s2 = target[i : ]
            if s1 == s2:
                ans += freq[s1] *(freq[s2] -1)  
                # '-1' to avoid duplicates as word at same index will get counted also in both prefix and suffix.
            else:
                ans += freq[s1] * freq[s2]
        return ans
