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

# Java Code 
"""
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        List<Integer> merged = new ArrayList<>();
        int i = 0, j = 0;
        int n = nums1.length, m = nums2.length;

        // Merge the two arrays
        while (i < n && j < m) {
            if (nums1[i] < nums2[j]) {
                merged.add(nums1[i]);
                i++;
            } else {
                merged.add(nums2[j]);
                j++;
            }
        }

        // If any elements left in nums1
        while (i < n) {
            merged.add(nums1[i]);
            i++;
        }

        // If any elements left in nums2
        while (j < m) {
            merged.add(nums2[j]);
            j++;
        }

        // Find median
        int total = n + m;
        if (total % 2 == 1) {
            return (double) merged.get(total / 2);
        } else {
            int mid1 = merged.get(total / 2 - 1);
            int mid2 = merged.get(total / 2);
            return (mid1 + mid2) / 2.0;
        }
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merged;
        int i = 0, j = 0;
        int n = nums1.size(), m = nums2.size();

        // Merge the two arrays
        while (i < n && j < m) {
            if (nums1[i] < nums2[j]) {
                merged.push_back(nums1[i]);
                i++;
            } else {
                merged.push_back(nums2[j]);
                j++;
            }
        }

        // If any elements left in nums1
        while (i < n) {
            merged.push_back(nums1[i]);
            i++;
        }

        // If any elements left in nums2
        while (j < m) {
            merged.push_back(nums2[j]);
            j++;
        }

        // Find median
        int total = n + m;
        if (total % 2 == 1) {
            return (double) merged[total / 2];
        } else {
            int mid1 = merged[total / 2 - 1];
            int mid2 = merged[total / 2];
            return (mid1 + mid2) / 2.0;
        }
    }
};
"""

# method 2: 
"""
Using Binary Search
most optimised . Q is asking this Algorithm only.

just we are making left and right partition virtually for both the arrays.
And if partition is correct then we can get the 'median'.

i.e , The Core Intuition: Virtual Partitioning
1. We aren't merging arrays; we are looking for a cutting point in both arrays such that:
The total number of elements on the left side of the cuts equals the total number of elements on the right (or +1 for odd).
2. Every element on the left side is <= every element on the right side.
Just trying to make the correct partition.

Q) Why Binary Search on the Smaller Array?
We swapped A and B to ensure A is smaller. 
1. Efficiency: It ensures the time complexity is O(log(min(m, n))).

Time Complexity:  O(log(min(m, n))) , We perform a binary search only on the smaller array.
Even though we are solving a problem involving m+n elements, we never "search" the larger array. 
We simply calculate the index j for the larger array in O(1) time using the result of our search in the smaller array.

Space Complexity: O(1). We only use a few pointer variables.

To see the case of '+infinity' or '-infinity', try example:
A = [10, 11] and B = [1, 2, 3, 4, 5] or 
A = [1, 2] and B = [10, 11, 12, 13, 14]

for these case: you need an example where the two arrays are "disjoint" in terms of their values—meaning one array 
is entirely smaller or larger than the other. This forces the partition to the absolute edges.
"""

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

# Java Code 
"""
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A = nums1, B = nums2;
        int total = nums1.length + nums2.length;   // total length of both array
        int half = total / 2;
        
        // finding the smaller size array and storing the smaller size array in "A" only.
        if (B.length < A.length) {  // then swap
            int[] temp = A;
            A = B;
            B = temp;
        }

        int l = 0, r = A.length - 1;  // traversing by finding the mid in smaller length array 'A'

        // we have to move mid of 'A' in case we don't find the correct partition.
        while (true) {
            int i = l + (r - l) / 2;  // mid of smaller array. last ele in left partition of 'A'.
            int j = half - i - 2;     // point to the last index in array 'B' in the left partition.

            double Aleft = (i >= 0) ? A[i] : Double.NEGATIVE_INFINITY;  // handling the corner case when all ele in left partition get included to form a single array i.e array 'B' only.
            double Aright = (i + 1 < A.length) ? A[i + 1] : Double.POSITIVE_INFINITY;  // First ele from array 'A' in right partition.
            double Bleft = (j >= 0) ? B[j] : Double.NEGATIVE_INFINITY;  // left most ele from B in left partition
            double Bright = (j + 1 < B.length) ? B[j + 1] : Double.POSITIVE_INFINITY;  // first ele from B in right partition.

            // if partition is correct, means we have done the left and right partitiion correctly.
            if (Aleft <= Bright && Bleft <= Aright) {
                // if total number of ele is odd
                if (total % 2 == 1) {
                    return Math.min(Aright, Bright);  // since one ele will more in right partition, so we have to return min from that.
                } else {
                    // return max(from left partition) + min(Right Partition) //2
                    return (Math.max(Aleft, Bleft) + Math.min(Aright, Bright)) / 2.0;
                }
            } else if (Aleft > Bright) {  // we have to go left in "A" to decrease the no of ele from "A" in left partition
                r = i - 1;
            } else {  // Bleft > Aright
                l = i + 1;  // we have to move right in 'A', to decrease the index 'j'(to deacrease the no of ele from B in left partition)
            }
        }
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> A = nums1, B = nums2;
        int total = nums1.size() + nums2.size();   // total length of both array
        int half = total / 2;

        // finding the smaller size array and storing the smaller size array in "A" only.
        if (B.size() < A.size()) {  // then swap
            swap(A, B);
        }

        int l = 0, r = A.size() - 1;  // traversing by finding the mid in smaller length array 'A'
        
        // we have to move mid of 'A' in case we don't find the correct partition.
        while (true) {
            int i = l + (r - l) / 2;  // mid of smaller array. last ele in left partition of 'A'.
            int j = half - i - 2;     // point to the last index in array 'B' in the left partition.

            double Aleft = (i >= 0) ? A[i] : -INFINITY;  // handling the corner case when all ele in left partition get included to form a single array i.e array 'B' only.
            double Aright = (i + 1 < A.size()) ? A[i + 1] : INFINITY;  // First ele from array 'A' in right partition.
            double Bleft = (j >= 0) ? B[j] : -INFINITY;  // left most ele from B in left partition
            double Bright = (j + 1 < B.size()) ? B[j + 1] : INFINITY;  // first ele from B in right partition.

            // if partition is correct, means we have done the left and right partitiion correctly.
            if (Aleft <= Bright && Bleft <= Aright) {
                // if total number of ele is odd
                if (total % 2 == 1) {
                    return min(Aright, Bright);  // since one ele will more in right partition, so we have to return min from that.
                } else {
                    // return max(from left partition) + min(Right Partition) //2
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0;
                }
            } else if (Aleft > Bright) {  // we have to go left in "A" to decrease the no of ele from "A" in left partition
                r = i - 1;
            } else {  // Bleft > Aright
                l = i + 1;  // we have to move right in 'A', to decrease the index 'j'(to deacrease the no of ele from B in left partition)
            }
        }

# Follow ups:
"""
https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
Code link : https://github.com/Ravi-0412/DSA-Program-And-Notes/blob/main/Binary_Search/K-th%20Element%20of%20Two%20Sorted%20Arrays.py
"""


