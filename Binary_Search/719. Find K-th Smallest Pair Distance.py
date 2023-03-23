# just same as "Q no: 668".
# Differenec in both: Here we need to sort the array to find no of  absolute difference in less than a given 'num' in  O(n) rather than o(n^2) in unsorted array.

# learnt way to find the absolute diff between pairs in array in O(n*logn).

# logic to find the absolute difference between pairs(here count function):
# Both pointers go from leftmost end. If the current pair pointed at has a distance less than or equal to distance,
# all pairs between these pointers are valid (since the array is already sorted), we move forward the fast pointer. 
# Otherwise, we move forward the slow pointer. By the time both pointers reach the rightmost end, we finish our scan and see if total counts exceed k.

# time: O(n*log(A)). A= max(nums)- min(nums)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # to calculate the no of  pairs having absolute difference  less than a given 'num' in  O(n) rather than o(n^2) in unsorted array.
        n= len(nums)

        # uses the two pointer approach.
        def count(num):   # kitna pair ka abs diff 'num' se chota h ya equal h(<=)
            i, j, cnt= 0, 1, 0  # start j= 1.
            while i < n or j < n:
                while j < n and nums[j]- nums[i] <= num:  # incr for "="  also so equal to diff equal to 'num' will also get included in ans.
                    j+= 1
                # add all the pair for this 'i' with j= i+1 to curr 'j-1'. . '-1' for absolute diff between same index (i,i).
                cnt+= j- i - 1
                i+= 1   # incr 'i' as we can get more ans since after incr 'i' absolute diff will become smaller.
            return cnt


        start= 0  # min Absolute difference we can have = 0
        end=   nums[-1]- nums[0]   # max Absolute difference we can have
        while start < end:
            mid= start + (end- start)//2
            if count(mid) >= k:
                end= mid
            else:
                start= mid + 1
        return start


# my mistakes:
        # start= nums[1]- nums[0]   # wrong because there can be other where also which can have abs diff less than this . 
        # like [1,5,6,...]. (5,6) has min diff . e.g: [1,6,6]. '0' here. 
# Note vvi: So better generalise the case of range like min and max in which our ans will lie. Guessing exact one is very difficult.
# This is the main reason i used to get wrong ans in most of the Q only because of trying to guess the range exactly.

# If you are sure then take that range otherwise just take min and max possible.
# Here we are sure that end= nums[-1]- nums[0] . end more than this is not possible.



# my mistake in solution
# changed the first while loop like this.
# vvi Reason for wrong ans: suppose even j is out of bound i.e = n for any given 'i'.
# means all pair fron that 'i' to 'j-1' will be part of our ans.
# Since we have to find the pair with smaller abs diff then , if we incraese 'i' then for same 'j', all pair for new 'i' till 'j-1' will be our ans.
# so we will do till our 'i' becomes equal to 'j' i.e 'n'.

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # to calculate the no of  pairs having absolute difference  less than a given 'num' in  O(n) rather than o(n^2) in unsorted array.
        n= len(nums)

        # uses the two pointer approach.
        def count(num):   # will give the count for which absolute difference between between pairs is <= num.
            i, j, cnt= 0, 0, 0
            while j < n:
                while j < n and nums[j]- nums[i] <= num:
                    j+= 1
                # add all the indices from 'i' to 'j'. '-1' for absolute diff between same index.
                cnt+= j- i - 1
                i+= 1   # incr 'i' as we can get more ans since after incr 'i' absolute diff will become smaller.
            return cnt


        start= 0  # min Absolute difference we can have = 0
        end=   nums[-1]- nums[0]   # max Absolute difference we can have
        while start < end:
            mid= start + (end- start)//2
            if count(mid) >= k:
                end= mid
            else:
                start= mid + 1
        return start
    

# other mistake:
# chnaged the first while loop and condition in 2nd while loop.
# even '=' condition i included.
# vvi Reason for wrong ans: we are taking equal to also when all ans when 'i==j' will also got included and our count will increase giving wrong ans.
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # to calculate the no of  pairs having absolute difference  less than a given 'num' in  O(n) rather than o(n^2) in unsorted array.
        n= len(nums)

        # uses the two pointer approach.
        def count(num):   # will give the count for which absolute difference between between pairs is <= num.
            i, j, cnt= 0, 1, 0
            print(num)
            while i < j:
                print(i, j, cnt)
                while j < n and num > nums[j]- nums[i]:
                    j+= 1
                # all the pair taht will form with this 'i' to 'j-1' will have abs diff smaller than 'num'.
                cnt+= j- i
                i+= 1   # incr 'i' as we can get more ans since after incr 'i' absolute diff will become smaller.
            return cnt + 1

        start= 0  # min Absolute difference we can have = 0
        end=   nums[-1]- nums[0]   # max Absolute difference we can have
        while start < end:
            mid= start + (end- start)//2
            if count(mid) >= k:
                end= mid
            else:
                start= mid + 1
        return start
    
