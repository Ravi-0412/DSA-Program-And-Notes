

# More will be parts of a number, more we can get product of it's integer.
# For this we need to split in most smaller number as possible avoiding '1'.
# Because 1 + 1+ 1+ ......because in this case ans = 1 which will be minimum only.

# So we can think of spilting into '2' i.e 2 + 2 + 2 +.. but it won't be optimal 
# e.g : e.g: 6 = 2 + 2 + 2 = 3 + 3. But 2 * 2 * 2 < 3 * 3.

# So next smaller number is '3' and it will be most optimal.
# But in case of 'n' not divisible by '3' , we have to use '2' also.
# so the optimal answer will be comprised of only 2s and 3s.

# Also Note: Any number > 1 can be expressed as 'c1*3 + c2*2' where c1,c1 >=0.

# So to get maximum ans, no of '3' should be as big as possible.
# e.g: 6 = 2 + 2 + 2 = 3 + 3. But 2 * 2 * 2 < 3 * 3.
# e.g : 12 = 2 + 2+ 2 + 2+ 2+ 2 (2^6 = 64) = 3 + 3 + 3 + 3 (3^4 = 81) = 6 + 6 (6^2 = 36)
# Just same as "2870. Minimum Number of Operations to Make Array Empty".

# Till n == 4 , we have to handle separately after that logic will work.

# Time : O(1) = space

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
    

# Related Q "2870. Minimum Number of Operations to Make Array Empty".