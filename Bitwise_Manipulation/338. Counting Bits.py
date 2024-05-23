# method 1: apply the logic of counting set bits with "n= n & n-1".

# method 2:
# write down in notebook you will get this pattern for even and odd number.

# Reason: Agar kisi number ko double kare to binary me bs ek '0' first me badhega baki sb same rhega.
# isliye no of one increase nhi karega agar kisi number ka multiple le binary me.
# e.g: 2 -> 10, 4 -> 100  ;   3 -> 11 , 6 -> 110  ; 5 -> 101 , 10 -> 1010 
# For add number 'num' we need to add '1' to ans of 'num//2'.

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans= [0]*(n+1)
        for num in range(1, n+1):
            if num %2 == 0:
                ans[num]= ans[num//2]
            else: 
                ans[num]= ans[num -1] + 1   # or ans[num]= ans[num//2] +1
        return ans
