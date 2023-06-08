# time= space= O(n)
# logic: just keep poping the num into stack when you see curr ele is smaller than the stack_top. else append into stack.
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
        print(stack)
        # return "".join(stack).lstrip('0') if stack else '0' # will give error in case e.g: "10" and k= 1. after removing we will be having "0" 
                                                             # and this will give empty ans after removing '0'.
        # we may left with leading zeroes at the start and for that we used lstrip('0)
        ans= "".join(stack).lstrip('0')
        return ans if ans else '0'   # after removing leading zero if ans is not empty then return  ans else '0'.