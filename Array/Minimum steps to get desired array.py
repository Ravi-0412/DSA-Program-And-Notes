# Note: Here we are trying to reduce the target array 'arr' to array ahving all zero.
# So we will have to do reverse operation i.e 
# a) Decremental operations:Choose 1 element from the array and decrease its value by 1.
# b) Reducing operation: Half the values of all the elements of array.

# it will be better to apply operation 'b' only when all elements are odd.

# steps:
# 1) if all number is even , divide all ele by '2'. Incr ans by '1' .
# 2) Make all odd number even. Incr ans by '1' for each step. and then apply step '1' and so on.

# whenever you find all ele= 0, return the ans.

# Note : check for all even 1st rather than making all odd elements to even otherwise it will give TLE.
# Reason: In case all are even then, it will unnecessarily check to make them even.

class Solution:
    def countMinOperations(self, arr, n):
        # find the position of first odd ele
        ans= 0
        while True:
            zeroCount= 0
            i= 0 
            while i < n:
                if arr[i] & 1:
                    # if any ele is odd 1st make all element even 
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
            
            # make all number even if it is odd by subtracting '-1'.
            for j in range(n):
                if arr[j] & 1:
                    arr[j]-= 1
                    ans+= 1


# i was trying to do opposite but it was getting complicated.
