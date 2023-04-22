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

# since array is already sorted so we can think of binary search but it will go in O(nlogn)
# like for every index just find the remaining sum and try to find that remaining sum in the array
# so time: O(nlogn)
