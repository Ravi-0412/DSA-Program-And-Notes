# method 1: use the unsorted approach i.e min heap

# since array is sorted, all the closest element will lie i)either left
# ii) either right iii) or some left and some right of given ele
# since ele may not be in the list so we take the diff to handle this case.

# in this we are finding the window of 'k' closest ele starting from 'l'
# mid will always point to the leftmost side of window  and 
# and after updating 'l' and 'r' , we will get the window bw 'l:l+k'.

# no need to find the absolute diff while finding the diff between target ele as array is sorted
# time: O(log(n-k) + k)

# 2nd template only.
# left and right in while loop will denote the starting index of our ans subarray. 
# so think according to this while updating 'left' and 'right'.
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # if x<= arr[0]:  return arr[0:k]
        # if x>= arr[-1]: return arr[-k:]
        left, right= 0, len(arr) - k   # maximum our starting window can start from 'n-k'.
        while left < right:
            mid= left + (right - left)//2
            if arr[mid + k]- x >= x - arr[mid] : # if 'mid+k' is >= then we can't get the ans subarray starting beyond mid.
                right= mid
            else:  # here our starting subarray must start from beyond 'mid' i.e mid+1
                left= mid + 1
        return arr[left: left + k]


