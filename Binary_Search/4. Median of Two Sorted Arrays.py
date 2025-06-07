# method 1: Brute force
# just merge both the array in sorted order using the logic "merge two sorted array into one sorted array".
# After that find the median.
# time: O(n+ m)


# method 2: Using Binary Search
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

# Do by other approaches in the sheet.


# Java Code 
"""
import java.util.*;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A = nums1, B = nums2;
        int total = nums1.length + nums2.length;
        int half = total / 2;

        if (B.length < A.length) {
            int[] temp = A;
            A = B;
            B = temp;  // Ensure A is the smaller array
        }

        int l = 0, r = A.length - 1;

        while (true) {
            int i = l + (r - l) / 2;  // Mid index in A (last element of left partition)
            int j = half - i - 2;     // Last index in B's left partition

            int Aleft = (i >= 0) ? A[i] : Integer.MIN_VALUE;
            int Aright = (i + 1 < A.length) ? A[i + 1] : Integer.MAX_VALUE;
            int Bleft = (j >= 0) ? B[j] : Integer.MIN_VALUE;
            int Bright = (j + 1 < B.length) ? B[j + 1] : Integer.MAX_VALUE;

            if (Aleft <= Bright && Bleft <= Aright) {
                if (total % 2 == 1) {
                    return Math.min(Aright, Bright);
                } else {
                    return (Math.max(Aleft, Bleft) + Math.min(Aright, Bright)) / 2.0;
                }
            } else if (Aleft > Bright) {
                r = i - 1;
            } else {
                l = i + 1;
            }
        }
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>& A = nums1;
        vector<int>& B = nums2;
        int total = nums1.size() + nums2.size();
        int half = total / 2;

        if (B.size() < A.size()) swap(A, B); // Ensure A is the smaller array

        int l = 0, r = A.size() - 1;

        while (true) {
            int i = l + (r - l) / 2;  // Mid index in A (last element of left partition)
            int j = half - i - 2;     // Last index in B's left partition

            int Aleft = (i >= 0) ? A[i] : INT_MIN;
            int Aright = (i + 1 < A.size()) ? A[i + 1] : INT_MAX;
            int Bleft = (j >= 0) ? B[j] : INT_MIN;
            int Bright = (j + 1 < B.size()) ? B[j + 1] : INT_MAX;

            if (Aleft <= Bright && Bleft <= Aright) {
                if (total % 2) {
                    return min(Aright, Bright);
                } else {
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0;
                }
            } else if (Aleft > Bright) {
                r = i - 1;
            } else {
                l = i + 1;
            }
        }
    }
};
"""






        