# method 1: use hashmap to store count.
# now traverse the number from 1 to n and check if it presentor not and if present what is its count.
# time= space: O(n)


# method 2: using maths
# time= O(n)
# space: O(1)
# Note: This may give overflow in other language.
def missingAndRepeating(arr, n):
    s= (n *(n+1))//2   # sum of number from 1 to n
    s2= (n * (n + 1) * (2 * n + 1)) // 6  # sum of squares of number from 1 to n.
    for num in arr:
        s-=  num
        s2-= num * num
    # now 's' will be left with 'missing- repeating'.   (1)
    # now 's' will be left with 'missing^2- repeating^2'.  (2)
    missing=    (s2//s + s)//2   # uing 1and 2
    repeating=  missing - s      # from 1
    return [missing, repeating]


# method 3(Best): Bitwise 
# submitted on interview Bit
# time: O(n), space: O(1)
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n= len(A)
        x1= 0
        for num in A:
            x1= x1^ num
        x2= 0
        for i in range(1, n+1):
            x2= x2^ i
        xor_result= x1^x2
        # now we have to find our ans from the above xor.
        rightmost_set_bit= xor_result & (-xor_result)
        # separate the arr number into two buckets having bit set at rightmost bit of 'xor_result'.
        set, not_set= 0, 0
        for num in A:
            if rightmost_set_bit & num:
                set= set ^ num
            else:
                not_set= not_set ^ num
        # now add separate the number from '1' to 'n' in these two buckets.
        for num in range(1, n+1):
            if rightmost_set_bit & num:
                set= set ^ num
            else:
                not_set= not_set ^ num
        # our number will get stored in set and not_set
        # now to return the repeating number first then missing.
        if set in A:  # means repeating
            return [set, not_set]
        else:  # means not_set is repeating one
            return [not_set, set]


# Note: How it is different from 'Q: 260. single number 3'.
# in that Q every ele is occuring two times except two. And no of ele that will have bit set at rightmost bit set of xor_result will be odd only 
# and no of ele for whcih bit is not set will be also odd only so we can directly get the ans on one separation.

# But here one is missing and one is repeating and no of ele having bit set and not set can be anything like odd or even.
# so in this we can't get ans directly.

# logic: 
# so when we do xor two times then in one part every number will occur two times except the missing one(will occur one time), 
# so from here we will get the missing one when we will take xor of all in this part and we did the same only in solution.
# And in 2nd part every number will occur two times except the repeating one(it will occur three times).
# so from here we will get the repeating one when we will take xor of all in this part and we did the same only in solution.

# and to know which one is repeating and which one is missing, just check whether that is present in the array or not.


