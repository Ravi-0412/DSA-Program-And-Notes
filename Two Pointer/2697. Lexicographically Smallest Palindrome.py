# logic: we have to make char same from start and end where char_at_start <= char_at_end.

# so, just check char  from left and right like we do in case of palindrome.
# if equal simply skip else make char same where char_at_start <=char_at_end

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        lst= list(s)
        n= len(s)
        l, r= 0, n-1
        while l < r:
            if lst[l]== lst[r]:
                # skip
                l,r= l+1, r-1               
                continue
            if lst[l] > lst[r]:
                # bring smaller one at start and both equal
                lst[l]= lst[r]
            else:
                # make end= start because we have to find the samllest alphabetical.
                lst[r]= lst[l]
            l,r= l+1, r-1
        return "".join(lst)


