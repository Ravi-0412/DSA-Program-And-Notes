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


# method 2: most efficient one
# https://leetcode.com/problems/check-if-the-number-is-fascinating/solutions/3625115/C++-oror-O(1)-TC/
# (understand the logic of above solution)
