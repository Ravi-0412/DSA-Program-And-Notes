
# time: ~ O(logn)
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num==0:
            return 0
        if num%2== 0:  # if even
            return 1+ self.numberOfSteps(num//2)
        # if odd
        return 1+ self.numberOfSteps(num-1)


# method 2 :
# logic: 
# For the binary representation from right to left(until we find the leftmost 1)
# if we meet 0, result += 1 because we are doing divide;
# if we meet 1, result += 2 because we first do "-1" then do a divide;
# ony exception is the leftmost 1, we just do a "-1" and it becomse 0 already.


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num==0:
            return 0
        ans= 0
        while num:
            if num & 1:  # if odd
                ans += 2
            else:
                ans += 1
            num = num >> 1
        return ans - 1