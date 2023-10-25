class Solution:
    def isFascinating(self, n: int) -> bool:
        ans= ""
        ans += str(n) + str(2*n) + str(3*n)
        hashmap = {}
        for num in ans:
            if num== '0' or num in hashmap:
                return False
            hashmap[num]= True
        return True    # return len(hashmap)== 9


# concise way of writing above
class Solution:
    def isFascinating(self, n: int) -> bool:
        s= str(n) + str(2*n) + str(3*n)
        ans= set(s)
        return len(ans) == len(s) == 9 and '0' not in s


# method 2: Mathematically
# 1) a numbernis fascinating only if 123 <= n <= 329, and
# 2) nmust be cyclic permutations of the digits of 192 or 273. 
# i.e there will only four fascinating number = 192, 219, 273, 327.

# I also don't know how this came.
# have to look on proof later.

# Note: Number >= 500 can't be fascinating because multiplying with '2' or '3' & concatenating them
# will make length >= 10 in which either '0' will come or some number will repeat.

class Solution:
    def isFascinating(self, n: int) -> bool:
        return n in {192, 219, 273, 327}



# method 2: 
# https://leetcode.com/problems/check-if-the-number-is-fascinating/solutions/3625115/C++-oror-O(1)-TC/
# (understand the logic of above solution)
