# time; O(logn)
class Solution:
    def guessNumber(self, n: int) -> int:
        start, end= 1, n
        while start <= end:
            mid= start + (end- start)//2
            if guess(mid)== 0:    # for calling predefined api no need to call with 'self'.
                return mid
            elif guess(mid)== -1:
                end= mid -1
            else:
                start= mid + 1

# Alternate way:
# template 2
class Solution:
    def guessNumber(self, n: int) -> int:
        start, end= 1, n
        while start < end:
            mid= start + (end- start)//2
            if guess(mid) <=0:    #if num >= picked. search for even more smaller
                end= mid
            else:
                start= mid + 1
        return start