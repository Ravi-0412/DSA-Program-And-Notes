# method 1: 
# Brute force
# just merge both the array in sorted order using the logic "merge two sorted array into one sorted array".
# After that find the median.
# time: O(n+ m)

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i = j = 0
        n, m = len(nums1), len(nums2)
        
        # Merge the two arrays
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # If any elements left in nums1
        while i < n:
            merged.append(nums1[i])
            i += 1
        
        # If any elements left in nums2
        while j < m:
            merged.append(nums2[j])
            j += 1
        
        # Find median
        total = n + m
        if total % 2 == 1:
            return float(merged[total // 2])
        else:
            mid1 = merged[total // 2 - 1]
            mid2 = merged[total // 2]
            return (mid1 + mid2) / 2.0


# method 2: 
# Using Binary Search
# most optimised . Q is asking this Algorithm only.
# time: O(log(m+ n))

# just we are making left and right partition virtually for both the arrays.
# And if partition is correct then we can get the 'median'.

# Just trying to make the correct partition.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B= nums1, nums2
        total= len(nums1) + len(nums2)   # total length of both array
        half= total//2
        # finding the smaller size array and storing the smaller size array in "A" only.
        if len(B) < len(A):  # then swap
            A, B= B, A
        # traversing by finding the mid in smaller length array 'A' 
        # Also we have to move mid of 'A' in case we don't find the correct partition.   
        l, r= 0, len(A) -1

        # If we write 'while l <= r' then, it won't work because here with the help of 
        while True:
            i = l+ (r-l) //2   # mid of smaller array. last ele in left partition of 'A'.
            j= half- i- 2     # point to the last index in array 'B' in the left partition.  '-2' since indexing are from '0'.
                            # we must include this much ele from 'B' to get 'half' no of ele in cumulative array.
                            # j = half - (i + 1) - 1
            
            Aleft=  A[i] if i>=0 else float('-inf')  # handling the corner case when all ele in left partition get 
                      # included to form a single array i.e array 'B' only.
        
            Aright= A[i+1] if (i+1) < len(A) else float('inf')  # if all ele get included from single array.
                                                    # First ele from array 'A' in right partition. 
            Bleft=  B[j]   if j>=0 else float('-inf')   # left most ele from B in left partition
            Bright= B[j+1] if (j+1) < len(B) else float('inf')  # first ele from B in right partition.

            # if partition is correct, means we have done the left and right partitiion correctly.

            # No need to check with same i.e Aleft <= Aright. Because this will be always true. 
            # So check with opposite one with opposite paramter i.e left with right of other.
            # Agar leftmost , 1st ele of right partition se chota h then yahan se partition kar sakte h left and right me.

            if Aleft <= Bright and Bleft <= Aright:
                # if total number of ele is odd
                if total % 2:  
                    return min(Aright, Bright)  # since one ele will more in right partition, so we have to return min from that.
                # if total number of ele is even.
                else: # return max(from left partition) + min(Right Partition) //2
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:  # we have to go left in "A" to decrease the no of ele from "A" in left partition
                r= i-1
            else:   # Bleft > Aright
                l= i+1  # we have to move right in 'A', to decrease the index 'j'(to deacrease the no of ele from B in left partition)


