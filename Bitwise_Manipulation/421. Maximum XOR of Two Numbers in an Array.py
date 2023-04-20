# for finding the max value, if we can get bit set at rightmost sides then that will be our ans.
# so we are taking the help of masking to extract those number by 100....00, 1100...00, 11100..000  etc for leftmost bit.
# till every bit we have traversed, we are putting the 'mask&num' in a set.(we want '1' so doing '&')
# now we will fix our target to get the max ans and that will be acc to the ans we have got till now.

# later we will take num one by one from set and do will xor with 'target' and will check if it's xor is present in set then,
# we can get our target . so update ans= target in this case and break otherwise leave ans as it is(it means we can't set the ans bit at bit position)

# Reason behind working of above one.
# if (a^b= target) then (target ^ a= b) and (target ^ b= a).   

# time:O(32*n), space: O(n)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans, mask= 0, 0
        for i in range(31, -1, -1):
            mask= mask | (1<< i)
            found= set()
            for num in nums:
                found.add(mask & num)
            target= ans | (1<< i)
            # now do xor of num in 'found ' with target and check if 'target^num' is in found.
            # if it is in found then we can get our desired target. so update the ans and break
            for prefix in found:
                if target ^ prefix in found:
                    ans= target
                    break
        return ans


