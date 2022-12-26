# logic: think of binary form of given 'power'
# and whenever  its bit is equal to 1, update the ans
# as presence of 1 in binary represents 2^0,2^1,2^2.....
# and update the base each time(base=base*base) till you traverse the whole digit of power.


# just we are spliting the powers into sum of powers of 2 
# like: 6(110)= 2+4, 5(101)= 4+1
# only valid if power is a natural no
# time complexity= O(logn)
# def power(x,n):
#     ans= 1
#     base= x
#     while(n>0):
#         if n&1==1:     # to get the last bit
#             ans*= base  # update the ans 
#         base*= base     # update the base for each iteration(1,2,4,...) # so multiplying base with base rather than 'base= base*x' as we only updating ans when we get '1' .
#         n>>= 1         # shift power right by 1 to get the next last bit for next iteration
#     return ans
# print(power(3,4))
# print(power(3,5))



# if power is negative same approach but we have to initialise base with '1/x' this time
# beacuse if any '1' comes then it must get start reducing  immediately like incr in case of +ve powers

# very concise will work for both +ve and negative powers
# in case power is '-ve' make it positive and after that eevrything will be same
# time: o(logn)
def power(x,n):
    if n<0:
        x= 1/x
        n= -n
    ans=1.0
    base= x
    i= n
    while i:
        if i % 2==1:   # to check the last bit 
            ans*= base
        base*= base
        i = int(i/2)          # right shift means dividing by 2 only 
    return ans

print(power(3,4))
print(power(3,5))
print(power(2,-5))
print(power(2,-4))


# METHOD 3: By Recursion
# time: O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x= 1/x
            n= -n
        if n== 0:
            return 1
        elif n %2==0:
            return self.myPow(x, n//2) * self.myPow(x, n//2) 
        else:
            return x * self.myPow(x, n//2) * self.myPow(x, n//2)

