# Method 1: Merge sort
# just take count while merging and check if it is equal to 'k'.

# Time = O(m + n) = space

# Method 2:
# We can use Two pointer with a 'count' variable.

# Time = O(m + n), space : O(1)


# Method 3:
# Apply binary search.

# Logic: just gfg only.

# We know that the Kth element will lie either in arr1[] or in arr2[], so we can maintain 2 search spaces: [arr1, arr1 + n] 
# and [arr2, arr2 + m] to find the kth element. Find the midpoints of both the search spaces, say mid1 and mid2. 
# mid1 tells that the kth element can lie in the range [arr1, arr1 + mid1] and 
# mid2 tells that kth element can lie in the range [arr2, arr2 + mid2]. Now, we can have 2 cases:

# Case 1: (mid1 + mid2 < k), this means that we have taken less than k elements in our search space and we need to include more elements.
# If (arr1[mid1] > arr2[mid2]), means that there are larger elements in arr1[] so we should include more elements from arr2[].
# If (arr1[mid1] <= arr2[mid2]), means that there are larger elements in arr2[] so we should include more elements from arr1[].

# Case 2: (mid1 + mid2 >= k), this means that we have taken more than or equal to k elements in our search space and 
# we might need to remove extra elements.
# If (arr1[mid1] > arr2[mid2]), means that there are larger elements in arr1[] so we should remove the extra elements from arr1[].
# If (arr1[mid1] <= arr2[mid2]), means that there are larger elements in arr2[] so we should remove the extra elements from arr2[].

# We keep on reducing the search space till we reach the kth element of the merge sorted array.

# Time Complexity: O(log n + log m)
# Auxiliary Space: O(logn + logm)

class Solution:
    
    def kth(self,arr1, arr2, k):
        # If the first array is exhausted, return the k-th element from the second array
        if len(arr1) == 0:
            return arr2[k]
        # If the second array is exhausted, return the k-th element from the first array
        if len(arr2) == 0:
            return arr1[k]
    
        # Calculate midpoints for both arrays
        mid1 = len(arr1) // 2
        mid2 = len(arr2) // 2
    
        if mid1 + mid2 < k:
            # since 'k' < mid1 + mid2,we can include element till 'mid' from that array having smaller 'mid' value before kth ele in virtualy merged array.
            # so in this case decrease 'k' by no of element till mid for respective aray.

            # If the value at mid1 in the first array is greater, discard the left part of the second array
            if arr1[mid1] > arr2[mid2]:
                return self.kth(arr1, arr2[mid2 + 1:], k - mid2 - 1)  # element till 'mid2' from arr2 is included for sure
            # Otherwise, discard the left part of the first array
            else:
                return self.kth(arr1[mid1 + 1:], arr2, k - mid1 - 1) # element till 'mid1' from arr1 is included for sure
        else:
            # since 'k' > mid1 + mid2, we can't how much element we will include from both the arrays so keep 'k' in this case.

            # If the value at mid1 in the first array is greater, discard the right part of the first array
            if arr1[mid1] > arr2[mid2]:
                return self.kth(arr1[:mid1], arr2, k)
            # Otherwise, discard the right part of the second array
            else:
                return self.kth(arr1, arr2[:mid2], k)
        
    
    def kthElement(self,  arr1, arr2, n, m, k):
         return self.kth(arr1, arr2, k - 1)

# my approach:
#  I though to find kth value when we will find the median(after getting virtually sorted array)
# using logic of "4. Median of two sorted Array" but not able to do.

# Try later or ask someone