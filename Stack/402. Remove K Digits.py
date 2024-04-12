# Exactly same Q as "1673. Find the Most Competitive Subsequence".

# Required length after removing 'k' number will be 'n-k'.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        k = n - k   # required length after removing 'k' digit.
        stack = []
        for i in range(len(num)):
            while stack and int(stack[-1]) > int(num[i]) and (len(stack) + (n - i)) > k:
                stack.pop()
            if len(stack) < k:
                stack.append(num[i])
        # Now handle the '0' at start.
        ans= "".join(stack).lstrip('0')
        return ans if ans else '0'
    
        # or simply return 
        # return "".join(stack).lstrip("0") or "0"

# time= space= O(n)
# logic: just keep poping the num from stack when you see curr ele is smaller than the stack_top, else append into stack.
# note: we have to make number smaller so we will remove the most significant digit only. 
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack= []
        for n in num:
            while stack and k and stack[-1] > n:   # stack will always contain the ele in ascending order.
                stack.pop()
                k-= 1
            stack.append(n)
        if k : # means we are not able to remove 'k' ele since after a point of time ele were in ascending order.
            stack= stack[:-k]   # removing the last 'k' ele.
        # return "".join(stack).lstrip('0') if stack else '0' # will give error in case e.g: "10" and k= 1. after removing we will be having "0" 
                                                             # and this will give empty ans after removing '0'.
        # we may left with leading zeroes at the start and for that we used lstrip('0)
        ans= "".join(stack).lstrip('0')
        return ans if ans else '0'   # after removing leading zero if ans is not empty then return  ans else '0'.