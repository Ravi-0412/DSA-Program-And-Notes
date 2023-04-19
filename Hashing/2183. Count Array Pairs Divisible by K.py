# logic: similar to "Two Sum".
# but here we can't find the other number directly like "Two Sum".

# for finding the other number 'want' first we find the gcd(n, k) then want=  k//gcd.

# we have to find the product which is divisible by k so for example if we need to make a pair which is
# divisible by 10 so by far we have found 12 so the gcd of 12,10 will be 2 now what is the other 
# counter we need to find it is 5 hence if we find 5's multiple or 5 we will add this pair to answer.

# time= (n* sqrt(n)) .
# since max number of divisor any number 'n' can have <= 2 * sqrt(n).

import math
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        frequency= collections.defaultdict(int)
        ans= 0
        for n in nums:
            Gcd= math.gcd(n, k)
            want= k // Gcd  # every num which is multiple of 'want' and what we have already seen will contribute to the ans.
                            # So add frequency of all such num
            for num in frequency:
                if num % want== 0:
                    ans+= frequency[num]

            frequency[Gcd]= 1 + frequency.get(Gcd, 0)
        return ans


# Note vvi: Also do by other Two methods (link in sheet).
