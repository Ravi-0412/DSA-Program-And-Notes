# Note: Here diff 'd' can be between multiple element and all will counted individually.
# 'k-th smallest' after we sort all the difference not kth- distinct.


# just same as "Q no: 668. Kth Smallest Number in Multiplication Table".
# Differenec in both: Here we need to sort the array to find no of  absolute difference in less than a given 'num' in  O(n) 
# rather than o(n^2) in unsorted array.

# learnt way to find the absolute diff between pairs in array in O(n*logn) i.e
# if given array is unsorted then just sort and apply this method.

# logic to find the absolute difference between pairs(here count function):
# Both pointers go from leftmost end. If the current pair pointed at has a distance less than or equal to distance,
# all pairs between these pointers are valid (since the array is already sorted), we move forward the fast pointer. 
# Otherwise, we move forward the slow pointer. By the time both pointers reach the rightmost end, we finish our scan and see if total counts exceed k.

# time: O(n*log(A)). A= max(nums)- min(nums)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # to calculate the no of  pairs having absolute difference easily
        n= len(nums)

        # uses the two pointer approach.
        def count(num):   # kitna pair ka abs diff 'num' se chota h ya equal h(<=)
            i, j, cnt= 0, 1, 0  # start with j = 1 
            while i < n :
                while j < n and nums[j] - nums[i] <= num: 
                    j+= 1
                # add all the pair for this 'i' with j= i+1 to curr 'j-1'. . '-1' for absolute diff between same index (i,i).
                cnt+= j- i - 1
                i+= 1   # incr 'i' as we can get more ans since after incr 'i' for same 'j' absolute diff will become smaller.
            return cnt

        # template 2 only
        start= 0  # min Absolute difference we can have = 0
        end=   nums[-1] - nums[0]   # max Absolute difference we can have
        while start < end:
            mid= start + (end- start)//2
            if count(mid) >= k:
                end= mid
            else:
                start= mid + 1
        return start


# my mistakes:
        # start= nums[1]- nums[0]   # wrong because there can be other pair where also which can have abs diff less than this . 
        # like [1,5,6,...]. (5,6) has min diff . e.g: [1,6,6]. '0' here.

# Note vvi: So better generalise the case of range like min and max in which our ans will lie. Guessing exact one is very difficult.
# This is the main reason i used to get wrong ans in most of the Q only because of trying to guess the range exactly.

# If you are sure then take that range otherwise just take min and max possible.
# Here we are sure that end= nums[-1]- nums[0] . end more than this is not possible.



# my mistake in solution
# changed the first while loop like this.
# vvi Reason for wrong ans: suppose even j is out of bound i.e = n for any given 'i'.
# means all pair fron that 'i' to 'j-1' will be part of our ans.
# Since we have to find the pair with smaller abs diff then , if we incraese 'i' then for same 'j', 
# all pair for new 'i' till 'j-1' will be our ans.
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
    



# Method 2: We can do by sorting also if k <= n -1. n= len(nums)

# Note vvi: We will get minimum difference when we will subtract adjacent ele if array is sorted.
# So just sort the array , store diff in another array say 'diff'.
# Then for ans sort 'diff' array and return diff[k -1].

# But this will only work if k <= n -1.
# Because if we will store the difference of adjacent ele then there will be only 'k-1' ele in 'diff' array.

# Also it is taking extra spac: O(n-1)


# Note: If we will store all possible diff then time: O(n^2) i.e comb(n, 2)

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = []
        for i in range(1, len(nums)):
            d = nums[i] - nums[i- 1]
            diff.append(d)
        diff.sort()
        return diff[k-1]
    

# Related Q:
# https://leetcode.com/discuss/interview-question/2408607/Amazon-2023-New-GRAD-OA

# In this we have to print all 'k' smallest pair also.
# Look at this later properly.


def getSmallestInefficiencies(nums, k) :
    n = len(nums)
    
    def count(num):   
        i, j, cnt= 0, 1, 0  # start j= 1.
        while i < n or j < n:
            while j < n and nums[j]- nums[i] <= num:  
                j+= 1
            # add all the pair for this 'i' with j= i+1 to curr 'j-1'. . '-1' for absolute diff between same index (i,i).
            cnt+= j- i - 1
            i+= 1  
        return cnt


    start= 0  # min Absolute difference we can have = 0
    end=   nums[-1]- nums[0]   # max Absolute difference we can have
    while start < end:
        mid= start + (end- start)//2
        if count(mid) >= k:
            end= mid
        else:
            start= mid + 1

    def getAns(kth) :
        # Get k pairs with distance <= kth
        ans = []
        i, j, cnt= 0, 1, 0  # start j= 1.
        while i < n or j < n:
            while j < n and nums[j]- nums[i] <= kth:  
                j+= 1
            
            if i == j:
                continue
            else:
                l = i
                while l < j:
                    ans.append(nums[] - nums[l])
                    l += 1
        return sorted(ans[:k])

    return getAns(start)

def main():
    e = getSmallestInefficiencies([6, 9, 1], 2)
    print(e)
    e = getSmallestInefficiencies([6, 9, 1, 2, 4, 7, 9, 10], 4)
    print(e)
    e = getSmallestInefficiencies([9, 10, 7, 10, 6, 1, 5, 4, 9, 8], 18)
    print(e)

if __name__ == "__main__":
    main()