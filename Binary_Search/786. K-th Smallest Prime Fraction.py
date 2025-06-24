# method 1: 

# used the similar 'heap' logic as :"378. Kth Smallest Element in a Sorted Matrix" .
# first put all the elements from where we can get all the minimum i.e starting indexes.

# time: O(n*logn) + O(k*logn)
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n= len(arr)
        minHeap = []
        # first add all pair of index from which we can get all minimum fraction possible by poping those numbers.
        # smallest fraction we will get arr[i]/arr[n-1] since array is sorted. 
        # numerator index should from the start of the arr and denominator index should be from the last of the array for minimum fraction.
        for i in range(n-1):   
            heapq.heappush(minHeap, (arr[i]/ arr[n-1], i, n-1))
        # now pop first 'k' elements. 
        for _ in range(k):
            _, i, j= heapq.heappop(minHeap)
            # next smaller may be arr[i]/ arr[j-1] or will be already in the heap. 
            # e.g: [1,2,3,5]  2nd min= (2,5) not (1,3) that's why we put all arr[i]/arr[n-1] at first.
            if j-1 >= 0:  
                heapq.heappush(minHeap, (arr[i]/ arr[j-1], i, j-1))  # not pushed (i+1, j) since this we get pushed automatically when 'i+1, j' will be poped.
        return [arr[i], arr[j]]   # last poped index will be our ans.

# Java Code 
"""
import java.util.*;

public class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        int n = arr.length;
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            Comparator.comparingDouble(a -> (double) arr[a[0]] / arr[a[1]])
        );

        // first add all pair of index from which we can get all minimum fraction possible by popping those numbers.
        // smallest fraction we will get arr[i]/arr[n-1] since array is sorted. 
        // numerator index should be from the start of the arr and denominator index from the end for minimum fraction.
        for (int i = 0; i < n - 1; i++) {
            minHeap.offer(new int[]{i, n - 1});
        }

        // now pop first 'k' elements.
        for (int step = 0; step < k - 1; step++) {
            int[] top = minHeap.poll();
            int i = top[0], j = top[1];

            // next smaller may be arr[i]/ arr[j-1] or will be already in the heap.
            // e.g: [1,2,3,5]  2nd min = (2,5) not (1,3), that's why we put all arr[i]/arr[n-1] initially.
            if (j - 1 > i) {
                minHeap.offer(new int[]{i, j - 1});
            }
        }

        int[] result = minHeap.poll();
        return new int[]{arr[result[0]], arr[result[1]]};  // last popped index will be our ans.
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        int n = arr.size();

        // minHeap will store pairs {i, j} based on the value of arr[i]/arr[j]
        auto comp = [&](const pair<int, int>& a, const pair<int, int>& b) {
            return (double) arr[a.first] / arr[a.second] > (double) arr[b.first] / arr[b.second];
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)> minHeap(comp);

        // first add all pair of index from which we can get all minimum fraction possible by popping those numbers.
        // smallest fraction we will get arr[i]/arr[n-1] since array is sorted. 
        // numerator index should be from the start of the arr and denominator index from the end for minimum fraction.
        for (int i = 0; i < n - 1; i++) {
            minHeap.emplace(i, n - 1);
        }

        // now pop first 'k' elements.
        for (int step = 0; step < k - 1; step++) {
            auto [i, j] = minHeap.top(); minHeap.pop();

            // next smaller may be arr[i]/ arr[j-1] or will be already in the heap.
            // e.g: [1,2,3,5]  2nd min = (2,5) not (1,3), that's why we put all arr[i]/arr[n-1] initially.
            if (j - 1 > i) {
                minHeap.emplace(i, j - 1);
            }
        }

        auto [i, j] = minHeap.top();
        return {arr[i], arr[j]};  // last popped index will be our ans.
    }
};
"""

# Method 2: 

# Note: Inserting both (i, j- 1) and (i+ 1, j) will give ans because (i + 1, j) may already in heap before
# when we are adding 1st and last i.e (i , j - 1)
# e.g: say n = 5 . in heap = [(0, 4) , (1, 4) ....]
# suppose 1st (0, 4) i.e i = 0, j = 4 get poped and if we insert (i + 1, j) i.e (1, 4) then this will be duplication.

# So insert only (i , j- 1).
    

# Or take a visited set and insert both pair if not already visited.

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n= len(arr)
        minHeap = []
        visited = set()
        # first add all pair of index from which we can get all minimum fraction possible by poping those numbers.
        # smallest fraction we will get arr[i]/arr[n-1] since array is sorted. 
        # numerator index should from the start of the arr and denominator index should be from the last of the array for minimum fraction.
        for i in range(n-1):   
            heapq.heappush(minHeap, (arr[i]/ arr[n-1], i, n-1))
            visited.add((i , n -1))
        # now pop first 'k' elements. 
        for _ in range(k):
            _, i, j= heapq.heappop(minHeap)
            # next smaller may be arr[i]/ arr[j-1] or will be already in the heap. 
            # e.g: [1,2,3,5]  2nd min= (2,5) not (1,3) that's why we put all arr[i]/arr[n-1] at first.
            if j-1 >= 0 and (i, j -1) not in visited:  
                heapq.heappush(minHeap, (arr[i]/ arr[j-1], i, j-1))  # not pushed (i+1, j) since this we get pushed automatically when 'i+1, j' will be poped.
                visited.add((i, j -1))
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(minHeap, (arr[i + 1]/ arr[j], i + 1, j))
                visited.add((i + 1, j))
        return [arr[i], arr[j]]   # last poped index will be our ans.


# Java Code 
"""
import java.util.*;

public class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        int n = arr.length;

        // minHeap will store [value, i, j] based on the value of arr[i]/arr[j]
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            Comparator.comparingDouble(a -> (double) arr[a[0]] / arr[a[1]])
        );

        Set<String> visited = new HashSet<>();

        // first add all pair of index from which we can get all minimum fraction possible by popping those numbers.
        // smallest fraction we will get arr[i]/arr[n-1] since array is sorted.
        // numerator index should from the start and denominator index from the end for min fractions
        for (int i = 0; i < n - 1; i++) {
            minHeap.offer(new int[]{i, n - 1});
            visited.add(i + "," + (n - 1));
        }

        // now pop first 'k' elements
        for (int step = 0; step < k - 1; step++) {
            int[] top = minHeap.poll();
            int i = top[0], j = top[1];

            // next smaller may be arr[i]/arr[j-1] or will already be in the heap
            if (j - 1 >= 0 && !visited.contains(i + "," + (j - 1))) {
                minHeap.offer(new int[]{i, j - 1});
                visited.add(i + "," + (j - 1));
            }

            // also explore the next row (i+1)
            if (i + 1 < n && !visited.contains((i + 1) + "," + j)) {
                minHeap.offer(new int[]{i + 1, j});
                visited.add((i + 1) + "," + j);
            }
        }

        int[] result = minHeap.poll();
        return new int[]{arr[result[0]], arr[result[1]]};  // last popped index will be our ans
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <queue>
#include <set>
#include <string>
#include <tuple>

using namespace std;

class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        int n = arr.size();

        auto cmp = [&](const tuple<double, int, int>& a, const tuple<double, int, int>& b) {
            return get<0>(a) > get<0>(b);
        };

        priority_queue<tuple<double, int, int>, vector<tuple<double, int, int>>, decltype(cmp)> minHeap(cmp);
        set<pair<int, int>> visited;

        // first add all pair of index from which we can get all minimum fraction possible
        for (int i = 0; i < n - 1; i++) {
            minHeap.emplace((double)arr[i] / arr[n - 1], i, n - 1);
            visited.insert({i, n - 1});
        }

        // pop 'k-1' elements
        for (int step = 0; step < k - 1; step++) {
            auto [val, i, j] = minHeap.top(); minHeap.pop();

            if (j - 1 >= 0 && !visited.count({i, j - 1})) {
                minHeap.emplace((double)arr[i] / arr[j - 1], i, j - 1);
                visited.insert({i, j - 1});
            }

            if (i + 1 < n && !visited.count({i + 1, j})) {
                minHeap.emplace((double)arr[i + 1] / arr[j], i + 1, j);
                visited.insert({i + 1, j});
            }
        }

        auto [_, i, j] = minHeap.top();
        return {arr[i], arr[j]};  // last popped index will be our answer
    }
};
"""
# Method 3: 
# using binary search.
# used the similar concept of "719. Find K-th Smallest Pair Distance".
# logic: first find the range in which our fraction can lie. 
# for possible fraction calculate the no of pair smaller than that and keep storing the largest fraction pair smaller than mid. 
# And if count of any 'mid' value== k: return that pair .
    
# vvi: Here we need to return simply when we will find the ans.So in while loop we will use 'start<=end'.
# note: while updating start and end , here we will make both equal to mid only because we are deaing in fraction and 
# max possible value is '1' only so we can't update start like 'mid+1' and end like 'mid -1'.

# time: O(NlogW), where N is array size, and W is the range size between the smallest and the largest fraction, in float number space.

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n= len(arr)

        def countLess(mid):
            cnt= 0
            j= 1  # will work as denominator
            p, q= 0, 1   # will store the largest fraction pair <= mid
            for i in range(n-1):  # 'i' will work as nominator and will go till 'n-2' 
                # move 'j' till you start getting fraction value <= mid.
                # after finding such 'j' then all number from 'n-j' will have fraction <= mid for curr 'i'.
                while j < n and arr[i]/arr[j] > mid:  # move 'j' till you start getting fraction value<= mid 
                    j+= 1
                # update p, q
                if j < n and p/q < arr[i]/ arr[j]:   # since we have to find the largest fraction <= mid so we are updating the value first time while loop break for any 'i'. 
                    p, q= arr[i], arr[j]                                                           # after this 'j' all will be smaller tahn current 'i'.
                cnt+= n- j   # all ele after 'j' will have fraction less than mid.
            return cnt, p, q

        # start, end= arr[0]/arr[n-1], 1  # can do like this also since we are sure that min can be this much only. And for max it will nearly equal to 1 but eaxctly '1'.
        start, end= 0, 1
        while start <= end:  # end -start>=0
            mid= start + (end- start)/2
            cnt, p, q= countLess(mid)
            if cnt== k:
                return [p, q]
            elif cnt > k:
                end= mid
            elif cnt < k:
                start= mid

# Java Code 
"""
public class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        int n = arr.length;
        double start = 0, end = 1;

        int p = 0, q = 1;

        while (end - start > 1e-9) {  // end - start >= 0
            double mid = start + (end - start) / 2;

            int[] res = countLess(arr, n, mid);  // cnt, p, q
            int cnt = res[0];
            p = res[1];
            q = res[2];

            if (cnt == k) {
                return new int[]{p, q};
            } else if (cnt > k) {
                end = mid;
            } else {
                start = mid;
            }
        }
        return new int[]{p, q};
    }

    // countLess(mid)
    private int[] countLess(int[] arr, int n, double mid) {
        int cnt = 0;
        int j = 1;  // will work as denominator
        int p = 0, q = 1;  // will store the largest fraction pair <= mid

        for (int i = 0; i < n - 1; i++) {  // 'i' will work as nominator and will go till 'n-2'
            // move 'j' till you start getting fraction value <= mid.
            // after finding such 'j' then all numbers from 'n-j' will have fraction <= mid for curr 'i'.
            while (j < n && (double) arr[i] / arr[j] > mid) {
                j++;
            }
            // update p, q
            if (j < n && (long) p * arr[j] < (long) q * arr[i]) {
                p = arr[i];
                q = arr[j];  // after this 'j', all will be smaller than current 'i'
            }
            cnt += n - j;  // all ele after 'j' will have fraction less than mid
        }
        return new int[]{cnt, p, q};
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        int n = arr.size();
        double start = 0, end = 1;

        int p = 0, q = 1;

        while (end - start > 1e-9) {  // end - start >= 0
            double mid = start + (end - start) / 2;
            auto [cnt, p1, q1] = countLess(arr, n, mid);  // cnt, p, q
            p = p1;
            q = q1;

            if (cnt == k) {
                return {p, q};
            } else if (cnt > k) {
                end = mid;
            } else {
                start = mid;
            }
        }
        return {p, q};
    }

private:
    // countLess(mid)
    tuple<int, int, int> countLess(const vector<int>& arr, int n, double mid) {
        int cnt = 0;
        int j = 1;  // will work as denominator
        int p = 0, q = 1;  // will store the largest fraction pair <= mid

        for (int i = 0; i < n - 1; i++) {  // 'i' will work as nominator and will go till 'n-2'
            // move 'j' till you start getting fraction value <= mid.
            // after finding such 'j' then all numbers from 'n-j' will have fraction <= mid for curr 'i'.
            while (j < n && (double) arr[i] / arr[j] > mid) {
                j++;
            }
            // update p, q
            if (j < n && (long long) p * arr[j] < (long long) q * arr[i]) {
                p = arr[i];
                q = arr[j];  // after this 'j', all will be smaller than current 'i'
            }
            cnt += n - j;  // all ele after 'j' will have fraction less than mid
        }

        return {cnt, p, q};
    }
};
"""