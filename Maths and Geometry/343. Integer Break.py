# Same logic as : "2870. Minimum Number of Operations to Make Array Empty".

# More will be parts of a number, more we can get product of it's integer.
# But we can't divide like 1 + 1+ 1+ ......because in this case ans = 1 which will be minimum only.

# Note: we know any number > 1 can be expressed as 'c1*3 + c2*2' where c1,c1 >=0.

# And to get maximum ans no of '3' should be as big as possible.
# e.g: 6 = 2 + 2 + 2 = 3 + 3. But 2 * 2 * 2 < 3 * 3.
# e.g : 12 = 2 + 2+ 2 + 2+ 2+ 2 (2^6 = 64) = 3 + 3 + 3 + 3 (3^4 = 81) = 6 + 6 (6^2 = 36)
# Just same as "2870. Minimum Number of Operations to Make Array Empty".

# Till n == 4 , we have to handle separately after that logic will work.

# Concise explanation:
# Hint 1
# For all x, y >1, product(x,y) ≥ sum(x,y)

# Hint 2
# It follows that it always makes sense to try to split the sum into the most components > 1 possible, as product > sum

# Hint 3
# 2 and 3 sum up to any number ≥ 2*, so it always makes sense to break it down into 2s and 3s.
# The optimal answer will be comprised of only 2s and 3s
# *(you can trivially prove this because 1 and 2 sum up to every number, and 3 is 2+1)

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        if n <= 3:   
            return 2
        if n == 4:
            return 4
        q, r = divmod(n , 3)
        if r == 0:
            return 3**q
        if r == 1:
            return (3 ** (q - 1)) * (2*2)
        return (3**q) * (2) 