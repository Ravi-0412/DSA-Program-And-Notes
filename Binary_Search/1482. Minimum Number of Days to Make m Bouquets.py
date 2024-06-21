# just same logic as "alllocate minimum no of pages".
# Difference between both Q: Here we can excatly allocate 'k' no of adjacent books to each student,
# instead of allocating any no of books if no of pages in that book is <= max_page_allowed.(i.e mid) .

# And we must allocate to at least 'm' students.

# our ans will lie in range [min(bloomDay), max(bloomDay)]. 
# At least we will have to wait till min(bloomDay) and max can go upto max(bloomDay)

# Note: one of element of array will be ans.

# time: O(n*log(max(bloomDay)))
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):  # not possible 
            return -1
        start, end= min(bloomDay), max(bloomDay) 
        while start < end:
            mid= start + (end- start)//2
            if self.isPossible(bloomDay, mid, m , k):
                end= mid 
            else:
                start= mid + 1
        return start 

    def isPossible(self, arr, mid, m , k):
        bouquet, count= 0, 0
        for i in range(len(arr)):
            if arr[i] > mid:
                count= 0   # we have start searching from '0' only
            else:
                count+= 1
            if count== k:  # means we have found 'k' adjacent flower so we can make one bouquet.
                bouquet+= 1
                count= 0  # to chekc for next possible bouquet.
        return bouquet >= m


# other way we can do is: 
# 1) just sort the array 
# 2) apply binary search on range ' [min(bloomDay), max(bloomDay)]' .
# 3) Check the last insertion point of mid in sorted array
# if insertion_point >= m * k then means for this 'mid' , it is possible to get all 'm' boquet.
# Reason: it means that we can get >= m * k flowers at days == mid.

# why this will work?
# because: one of element of array will be ans.


# Java
"""
// 'm*n' can overflow so we need to handle it. so handled it using 'division' instead of multiplication for not possible case.

import java.util.Arrays;

class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        int n = bloomDay.length;
        // Handle potential overflow by using division instead of multiplication
        if (m > n / k) // not possible
            return -1;

        // Determine the initial binary search bounds
        int start = Arrays.stream(bloomDay).min().getAsInt();
        int end = Arrays.stream(bloomDay).max().getAsInt();

        // Binary search to find the minimum number of days
        while (start < end) {
            int mid = start + (end - start) / 2; // Calculate midpoint (integer division)
            if (isPossible(bloomDay, mid, m, k))
                end = mid;
            else
                start = mid + 1;
        }
        return start;
    }

    // Helper method to check if it's possible to form m bouquets in mid days
    private boolean isPossible(int[] arr, int mid, int m, int k) {
        int bouquet = 0, count = 0;
        for (int day : arr) {
            if (day > mid) {
                count = 0; // reset count if current day is greater than mid
            } else {
                count += 1; // increment count if current day is less than or equal to mid
            }
            if (count == k) { // we found k adjacent flowers
                bouquet += 1; // one bouquet is made
                count = 0; // reset count for the next bouquet
            }
        }
        return bouquet >= m; // check if we can make at least m bouquets
    }
}

"""