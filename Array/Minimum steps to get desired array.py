# steps:
# 1) if all number is even , divide all ele by '2'. Incr ans by '1' for overall.
# 2) Make all odd number even. Incr ans by '1' for each step.

# whenever you find all ele= 0, return the ans.

class Solution:
    def countMinOperations(self, arr, n):
        # find the position of first odd ele
        ans= 0
        while True:
            zeroCount= 0
            i= 0 
            while i < n:
                if arr[i] & 1:
                    break
                if arr[i]== 0:
                    zeroCount+= 1
                i+= 1
            # check if all number has become zero
            if zeroCount== n:
                return ans
            # check if all number is even
            if i== n:  # i== n when we will not find any odd number means all are even
                # divide all number by '2'
                for j in range(n):
                    arr[j]= arr[j]//2
                ans+= 1
            
            # make all number even if it is odd
            for j in range(n):
                if arr[j] & 1:
                    arr[j]-= 1
                    ans+= 1


# i was trying to do opposite but it was getting complicated.
