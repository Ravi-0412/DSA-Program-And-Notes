# 1st method: using hashmap like as usual for all problems of this type.

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
        while start < end:  #  start can't be equal to end as we can't use the same ele twice
            
            # in this case our ans will lie before end since array is sorted so incr start will incr the more 
            if numbers[start] + numbers[end] > target:
                    end-= 1
            # in this case our ans will lie after start since array is sorted
            elif numbers[start]+ numbers[end] < target:
                start+= 1
            else:  # we found the target
                return start+1, end+1


# If asked to find the no of such pairs then:
# a) No duplicate element

def count_pairs_with_sum(arr, target):
    left = 0
    right = len(arr) - 1
    count = 0
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            count += 1
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return count

# b) Duplicate allowed

def count_pairs_with_sum(arr, target):
    left = 0
    right = len(arr) - 1
    count = 0
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            if arr[left] == arr[right]:
                # If both pointers are at the same element, count combinations
                num_elements = right - left + 1
                count += (num_elements * (num_elements - 1)) // 2   # comb(n, 2)
                break
            else:
                # Count occurrences of arr[left] and arr[right]
                left_count = 1
                right_count = 1
                
                while left + 1 < right and arr[left] == arr[left + 1]:
                    left += 1
                    left_count += 1
                    
                while right - 1 > left and arr[right] == arr[right - 1]:
                    right -= 1
                    right_count += 1
                
                count += left_count * right_count   # (m*n)
                left += 1
                right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return count

# c) Given two strictly sorted arrays in ascending order and a target.
# count no of pairs whose sum = target such that one ele is taken from arr1 and other is from arr2.
# Note: strictly sorted => no duplicates

def count_pairs_with_sum(arr1, arr2, target):
    left = 0
    right = len(arr2) - 1
    count = 0
    
    while left < len(arr1) and right >= 0:
        current_sum = arr1[left] + arr2[right]
        
        if current_sum == target:
            count += 1
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return count

# d) If arrays are sorted but not strictly means duplicate are allowed
def count_pairs_with_sum(arr1, arr2, target):
    left = 0
    right = len(arr2) - 1
    count = 0
    
    while left < len(arr1) and right >= 0:
        current_sum = arr1[left] + arr2[right]
        
        if current_sum == target:
            left_val = arr1[left]
            right_val = arr2[right]
            
            left_count = 0
            right_count = 0
            
            # Count occurrences of the current element in arr1
            while left < len(arr1) and arr1[left] == left_val:
                left_count += 1
                left += 1
            
            # Count occurrences of the current element in arr2
            while right >= 0 and arr2[right] == right_val:
                right_count += 1
                right -= 1
            
            count += left_count * right_count
        
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return count

# Note vvi: whenever you get this type of Q then try to fix one ele somehow 
# and find the other two ele using "Two sum" for sorted/unsorted array.
# Just try to reduce into "two sum" problem.
# e.g: "15. 3Sum", "18. 4Sum", "Count Triplets"


# Note: where to use "Two pointer"?
# 1) where you see array is sorted then once must think about "Two Pointer" or "Binary Search".
# 2) when you have to solve in-place , then think if we can do by "Two Pointer".
# vvi: For in-place, mostly a) Think about swapping elements b) Think of "Two Pointer". 
# these two method work in most of the cases where we are asked to do in-place.


