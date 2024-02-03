# logic:
# Straight forward way to solve the problem in 3 steps:

# find the length of the number where the nth digit is from
# find the actual number where the nth digit is from
# find the nth digit and return

# time:O(logn)

class Solution:
    def findNthDigit(self, n: int) -> int:
        length= 1   # will give the number of digits in the target number
        start= 1    # will give the first number in which 'n' lies
        count= 9    # no of '1' length no = 9, '2' length = 90 , '3' length = 900 and so on 
        # 1st find the length of digit in target number i.e range in which our target number lies.
        while n > length *count:
            n-= length * count
            count*= 10     # 9, 90, 900, 9000
            start*= 10     # 1, 10, 100, 1000,....
            length+= 1     #1, 2, 3,....
        # Now find the target number. Target number is 'n' digit aheead from the start i.e 1st number in range.
        number= start + ((n-1) //length)   # '0' indexing in digit (0-9)
        # find the index that we have to get in final number
        index= ((n-1) % length)
        # find the required digit.
        return int(str(number)[index])

