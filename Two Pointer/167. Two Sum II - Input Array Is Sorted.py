# 1st method: using hashmap like as usual for all probelms of this type.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap= {}
        for i in range(len(numbers)):
            rem_sum= target- numbers[i]
            if rem_sum in hashmap:
                return hashmap[rem_sum] +1, i+1
            else:
                hashmap[numbers[i]]= i


# 2nd method : using two pointer (this q was mainly given because of this)
# vvi basic logic: hmko pointer ko aisa jagah rakhna h jisse hm sure dekh paye ki kis side move karna h.
# Aisa Q like closest pair, minDiff of pairs etc  sbka yhi logic h.

# isliye phle pointer sochna h.
# simpler way to find index of pointers: just keep one pointer at index where you can get the min number 
# and one at index where you can get the maximum number.
# time: O(n), space: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n= len(numbers)
        start, end= 0, n-1
        while start< end:  #  start can't be equal to end as we can't use the same ele twice
            
            # in this case our ans will lie before end since array is sorted so incr start will incr the more 
            if numbers[start] + numbers[end] > target:
                    end-= 1
            # in this case our ans will lie after start since array is sorted
            elif numbers[start]+ numbers[end] < target:
                start+= 1
            else:  # we found the target
                return start+1, end+1

# Note: where to use "Two pointer"?
# 1) where you see array is sorted then once must think about "Two Pointer" or "Binary Search".
# 2) when you have to solve in-place , then think if we can do by "Two Pointer".
# vvi: For in-place, mostly a) Think about swapping elements b) Think of "Two Pointer". 
# these two method work in most of the cases where we are asked to do in-place.


