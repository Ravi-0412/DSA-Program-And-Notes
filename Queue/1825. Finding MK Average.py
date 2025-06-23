# Brute force
class MKAverage:

    def __init__(self, m: int, k: int):
        self.n = m
        self.k = k
        self.q = deque()

    def addElement(self, num: int) -> None:
        if len(self.q)==self.n:
            self.q.popleft()
        self.q.append(num)

    def calculateMKAverage(self) -> int:
        if len(self.q)<self.n:
            return -1
        arr = sorted(list(self.q))
        l = len(arr) - 2*self.k
        s = sum(arr[self.k:self.n-self.k])
        return s//l

# Java Code 
"""
import java.util.*;

class MKAverage {
    private int n, k;
    private Deque<Integer> q;

    public MKAverage(int m, int k) {
        this.n = m;
        this.k = k;
        this.q = new ArrayDeque<>();
    }

    public void addElement(int num) {
        if (q.size() == n) {
            q.pollFirst();
        }
        q.addLast(num);
    }

    public int calculateMKAverage() {
        if (q.size() < n) {
            return -1;
        }
        List<Integer> arr = new ArrayList<>(q);
        Collections.sort(arr);
        int l = n - 2 * k;
        int sum = 0;
        for (int i = k; i < n - k; i++) {
            sum += arr.get(i);
        }
        return sum / l;
    }
}
"""

# C++ Code
"""
#include <deque>
#include <vector>
#include <algorithm>

class MKAverage {
    int n, k;
    std::deque<int> q;

public:
    MKAverage(int m, int k) {
        this->n = m;
        this->k = k;
    }

    void addElement(int num) {
        if (q.size() == n) {
            q.pop_front();
        }
        q.push_back(num);
    }

    int calculateMKAverage() {
        if (q.size() < n) {
            return -1;
        }
        std::vector<int> arr(q.begin(), q.end());
        std::sort(arr.begin(), arr.end());
        int l = n - 2 * k;
        long long sum = 0;
        for (int i = k; i < n - k; ++i) {
            sum += arr[i];
        }
        return sum / l;
    }
};
"""
# Method 2: 
# Logic: Just focus on how we will get sum of those remaining ele for which we have to find the average.

# Intutition: We need to remove the ele from start if len(data_structure) > m.
# so 'deque' comes into mind.

# But for calculatiing the average , we need to sort each time and remove 'first_k' and 'last_k' 
# so deque alone is not enough.

# So we need somthing that stores all 'm' element in sorted order always.
# for this 'sortedList' comes into mind.

# So finally we will store all upcoming element into sorted list and will check if it's length is > m
# then we will remove the possible ele and make decision accordingly.

# explanation:
"""
use both a deque and a SortedList to keep track of the last m numbers, FIFO. It's trivial to maintain the total sum of them. 
To maintain the sum of the smallest/largest k numbers, we examine the index at which the new number will be inserted
into the SortedList and the index at which the oldest number will be removed from the SortedList. 
If the new number to be inserted will become one of the smallest/largest k numbers,
we add it to self.first_k/self.last_k and subtract out the current kth smallest/largest number. 
"""

# Note: Using 'SortedList' interviewer won't accept that.
# So try to solve using segment tree.

from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m , self.k = m , k
        self.sorted_list = SortedList()
        self.dq = deque()
        self.total = 0
        self.sum_first_k = self.sum_last_k = 0
    
    # Time: O(logn)
    def addElement(self, num: int) -> None:
        self.total += num
        # Before adding check if will come under 'k' smallest or 'k' largest.
        # for this find the insertion index in sorted_list
        ind = self.sorted_list.bisect_left(num)
        # 1) checking if it will come under 'k' smallest
        # for this 'ind' must be < 'k'
        if ind < self.k:
            self.sum_first_k += num
            # we need to subtract the current ele at index 'k-1' from 'sum_first_k'.
            if len(self.sorted_list) >= self.k:
                self.sum_first_k -= self.sorted_list[self.k -1]
        # 2) checking if it will come under last 'k' largest
        # for this 'ind' must >= len(sorted_list) + k -1
        if ind >= len(self.sorted_list) - self.k + 1:
            self.sum_last_k += num
            # we need to subtract the current ele at index 'k' from last from 'sum_last_k'.
            if len(self.sorted_list) >= self.k:
                self.sum_last_k -= self.sorted_list[-self.k]
        # Now add this to sorted_list and deque
        self.sorted_list.add(num)
        self.dq.append(num)
        # Since 'dq' only store 'm' elements so check if len(dq) > m
        if len(self.dq) > self.m:
            # we need to remove 1st ele from start of deque and sorted_list
            # Because it is not going to matter in sum calculation later
            # 1) 
            no = self.dq.popleft()
            self.total -= no
            ind1 = self.sorted_list.bisect_left(no)
            # Now check if this removed ele was contributing to 'first' or 'last' sum.
            # a) checking for 'first_k'.
            ind1 = self.sorted_list.index(no)
            if ind1 < self.k:
                self.sum_first_k -= no
                # after removal of this, ele at index 'k' will contribute to 'first_k' sum.
                self.sum_first_k += self.sorted_list[self.k]
            # b) checking for 'last_k'.
            elif ind1 >= len(self.sorted_list) - self.k:
                self.sum_last_k -= no
                # after removal of this, ele at index 'k- 1' from last will contribute to 'last_k' sum.
                self.sum_last_k += self.sorted_list[-(self.k + 1)]
            # 2) now remove from sorted_list as well
            self.sorted_list.remove(no)

    # time : O(1)
    def calculateMKAverage(self) -> int:
        if len(self.sorted_list) < self.m:
            return -1
        return (self.total - self.sum_first_k - self.sum_last_k) // (self.m - 2 * self.k)

# Java Code 
"""
import java.util.*;

public class MKAverage {
    int m, k;
    long total;
    long sumFirstK, sumLastK;
    Deque<Integer> dq;
    TreeMap<Integer, Integer> sortedMap;

    public MKAverage(int m, int k) {
        this.m = m;
        this.k = k;
        this.total = 0;
        this.sumFirstK = 0;
        this.sumLastK = 0;
        this.dq = new LinkedList<>();
        this.sortedMap = new TreeMap<>();
    }

    public void addElement(int num) {
        total += num;

        // Before adding check if will come under 'k' smallest or 'k' largest.
        // for this find the insertion index in sortedMap
        insert(num);
        dq.addLast(num);

        // Since 'dq' only stores 'm' elements so check if len(dq) > m
        if (dq.size() > m) {
            // we need to remove 1st ele from start of deque and sortedMap
            int no = dq.removeFirst();
            total -= no;
            erase(no);
        }
    }

    public int calculateMKAverage() {
        if (dq.size() < m) return -1;
        return (int) ((total - sumFirstK - sumLastK) / (m - 2 * k));
    }

    private void insert(int num) {
        sortedMap.put(num, sortedMap.getOrDefault(num, 0) + 1);
        updateSumK();
    }

    private void erase(int num) {
        if (sortedMap.get(num) == 1) sortedMap.remove(num);
        else sortedMap.put(num, sortedMap.get(num) - 1);
        updateSumK();
    }

    private void updateSumK() {
        sumFirstK = 0;
        sumLastK = 0;

        // Count first k smallest
        int cnt = 0;
        for (Map.Entry<Integer, Integer> entry : sortedMap.entrySet()) {
            int val = entry.getKey();
            int freq = entry.getValue();
            for (int i = 0; i < freq && cnt < k; i++, cnt++) {
                sumFirstK += val;
            }
            if (cnt >= k) break;
        }

        // Count last k largest
        cnt = 0;
        for (Map.Entry<Integer, Integer> entry : sortedMap.descendingMap().entrySet()) {
            int val = entry.getKey();
            int freq = entry.getValue();
            for (int i = 0; i < freq && cnt < k; i++, cnt++) {
                sumLastK += val;
            }
            if (cnt >= k) break;
        }
    }
}

"""
# C++ Code 
"""
#include <bits/stdc++.h>
using namespace std;

class MKAverage {
    int m, k;
    long long total = 0;
    long long sumFirstK = 0, sumLastK = 0;
    deque<int> dq;
    multiset<int> sorted;

public:
    MKAverage(int m, int k) {
        this->m = m;
        this->k = k;
    }

    void addElement(int num) {
        total += num;

        // add this to sorted and deque
        sorted.insert(num);
        dq.push_back(num);

        // Since 'dq' only store 'm' elements so check if len(dq) > m
        if (dq.size() > m) {
            // we need to remove 1st ele from start of deque and sorted
            int no = dq.front(); dq.pop_front();
            total -= no;
            sorted.erase(sorted.find(no));
        }

        if (dq.size() == m) {
            updateSumK();
        }
    }

    int calculateMKAverage() {
        if (dq.size() < m) return -1;
        return (total - sumFirstK - sumLastK) / (m - 2 * k);
    }

private:
    void updateSumK() {
        sumFirstK = 0;
        sumLastK = 0;

        // Count first k smallest
        int cnt = 0;
        for (auto it = sorted.begin(); it != sorted.end() && cnt < k; ++it, ++cnt)
            sumFirstK += *it;

        // Count last k largest
        cnt = 0;
        for (auto it = sorted.rbegin(); it != sorted.rend() && cnt < k; ++it, ++cnt)
            sumLastK += *it;
    }
};

"""

# Method 3: 
# Using segment tree
# Link: https://leetcode.com/problems/finding-mk-average/solutions/1152438/python3-fenwick-tree/

class Fenwick: 

    def __init__(self, n: int):
        # Initialize a Fenwick Tree with size n
        self.tree = [0] * (n + 1)

    def prefix_sum(self, index: int) -> int: 
        # Calculate prefix sum from 0 to index
        index += 1
        result = 0
        while index:
            result += self.tree[index]
            # Move to the previous segment
            index &= index - 1  # Unset the last set bit to move backwards
        return result

    def update(self, index: int, delta: int) -> None: 
        # Update the Fenwick Tree by adding delta to index
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            # Move to the next segment
            index += index & -index  # Add the last set bit to move forwards


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m  # Total number of elements to consider in the sliding window
        self.k = k  # The number of smallest and largest elements to ignore
        self.window = deque()  # Stores the most recent 'm' elements
        self.sum_tree = Fenwick(10**5 + 1)  # tree[i] : sum of number till number 'i'.
        self.count_tree = Fenwick(10**5 + 1)  # tree[i] : Count of number <= 'i'.

    def addElement(self, num: int) -> None:
        # Add an element to the sliding window
        self.window.append(num)
        self.sum_tree.update(num, num)  # Add the value to the sum tree
        self.count_tree.update(num, 1)  # Increment the count for the number

        # If the window exceeds size 'm', remove the oldest element
        if len(self.window) > self.m:
            oldest = self.window.popleft()
            self.sum_tree.update(oldest, -oldest)  # Remove the value from the sum tree
            self.count_tree.update(oldest, -1)  # Decrement the count for the number

    def _find_kth_smallest(self, k: int) -> int:
        # Binary search to find the k-th smallest element using count_tree
        low, high = 0, 10**5 + 1
        while low < high:
            mid = (low + high) // 2
            if self.count_tree.prefix_sum(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low

    def calculateMKAverage(self) -> int:
        # If the window is not yet full, return -1
        if len(self.window) < self.m:
            return -1
        
        # Find the k-th smallest and m-k-th smallest elements
        lower_bound = self._find_kth_smallest(self.k)  # k-th smallest element
        upper_bound = self._find_kth_smallest(self.m - self.k)  # m-k-th smallest element
        
        # Calculate the sum of the elements between lower_bound and upper_bound
        total_sum = self.sum_tree.prefix_sum(upper_bound) - self.sum_tree.prefix_sum(lower_bound)
        
        # Adjust for elements that fall on the boundary
        total_sum += (self.count_tree.prefix_sum(lower_bound) - self.k) * lower_bound
        total_sum -= (self.count_tree.prefix_sum(upper_bound) - (self.m - self.k)) * upper_bound
        
        # Return the MK average
        return total_sum // (self.m - 2 * self.k)

# Java Code 
"""
import java.util.*;

class Fenwick {
    int[] tree;

    // Initialize a Fenwick Tree with size n
    public Fenwick(int n) {
        tree = new int[n + 1];
    }

    // Calculate prefix sum from 0 to index
    public int prefixSum(int index) {
        index += 1;
        int result = 0;
        while (index > 0) {
            result += tree[index];
            // Move to the previous segment
            index &= index - 1; // Unset the last set bit to move backwards
        }
        return result;
    }

    // Update the Fenwick Tree by adding delta to index
    public void update(int index, int delta) {
        index += 1;
        while (index < tree.length) {
            tree[index] += delta;
            // Move to the next segment
            index += index & -index; // Add the last set bit to move forwards
        }
    }
}

class MKAverage {
    private int m, k;
    private Deque<Integer> window;
    private Fenwick sumTree;
    private Fenwick countTree;

    public MKAverage(int m, int k) {
        this.m = m; // Total number of elements to consider in the sliding window
        this.k = k; // The number of smallest and largest elements to ignore
        this.window = new ArrayDeque<>();
        this.sumTree = new Fenwick(100001); // tree[i] : sum of number till number 'i'.
        this.countTree = new Fenwick(100001); // tree[i] : Count of number <= 'i'.
    }

    // Add an element to the sliding window
    public void addElement(int num) {
        window.addLast(num);
        sumTree.update(num, num); // Add the value to the sum tree
        countTree.update(num, 1); // Increment the count for the number

        // If the window exceeds size 'm', remove the oldest element
        if (window.size() > m) {
            int oldest = window.pollFirst();
            sumTree.update(oldest, -oldest); // Remove the value from the sum tree
            countTree.update(oldest, -1); // Decrement the count for the number
        }
    }

    // Binary search to find the k-th smallest element using count_tree
    private int findKthSmallest(int k) {
        int low = 0, high = 100001;
        while (low < high) {
            int mid = (low + high) / 2;
            if (countTree.prefixSum(mid) < k) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

    // Return the MK average
    public int calculateMKAverage() {
        // If the window is not yet full, return -1
        if (window.size() < m) {
            return -1;
        }

        // Find the k-th smallest and m-k-th smallest elements
        int lowerBound = findKthSmallest(k); // k-th smallest element
        int upperBound = findKthSmallest(m - k); // m-k-th smallest element

        // Calculate the sum of the elements between lower_bound and upper_bound
        int totalSum = sumTree.prefixSum(upperBound) - sumTree.prefixSum(lowerBound);

        // Adjust for elements that fall on the boundary
        totalSum += (countTree.prefixSum(lowerBound) - k) * lowerBound;
        totalSum -= (countTree.prefixSum(upperBound) - (m - k)) * upperBound;

        return totalSum / (m - 2 * k);
    }
}

"""
# C++ Code 
"""
#include <bits/stdc++.h>
using namespace std;

class Fenwick {
    vector<int> tree;

public:
    // Initialize a Fenwick Tree with size n
    Fenwick(int n) {
        tree.resize(n + 1, 0);
    }

    // Calculate prefix sum from 0 to index
    int prefix_sum(int index) {
        index += 1;
        int result = 0;
        while (index > 0) {
            result += tree[index];
            // Move to the previous segment
            index &= index - 1; // Unset the last set bit to move backwards
        }
        return result;
    }

    // Update the Fenwick Tree by adding delta to index
    void update(int index, int delta) {
        index += 1;
        while (index < tree.size()) {
            tree[index] += delta;
            // Move to the next segment
            index += index & -index; // Add the last set bit to move forwards
        }
    }
};

class MKAverage {
    int m, k;
    deque<int> window;
    Fenwick sum_tree, count_tree;

public:
    MKAverage(int m, int k)
        : m(m), k(k), sum_tree(100001), count_tree(100001) {
        // Total number of elements to consider in the sliding window
        // The number of smallest and largest elements to ignore
    }

    // Add an element to the sliding window
    void addElement(int num) {
        window.push_back(num);
        sum_tree.update(num, num); // Add the value to the sum tree
        count_tree.update(num, 1); // Increment the count for the number

        // If the window exceeds size 'm', remove the oldest element
        if (window.size() > m) {
            int oldest = window.front();
            window.pop_front();
            sum_tree.update(oldest, -oldest); // Remove the value from the sum tree
            count_tree.update(oldest, -1); // Decrement the count for the number
        }
    }

    // Binary search to find the k-th smallest element using count_tree
    int find_kth_smallest(int k) {
        int low = 0, high = 100001;
        while (low < high) {
            int mid = (low + high) / 2;
            if (count_tree.prefix_sum(mid) < k) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

    // Return the MK average
    int calculateMKAverage() {
        // If the window is not yet full, return -1
        if (window.size() < m) {
            return -1;
        }

        // Find the k-th smallest and m-k-th smallest elements
        int lower_bound = find_kth_smallest(k); // k-th smallest element
        int upper_bound = find_kth_smallest(m - k); // m-k-th smallest element

        // Calculate the sum of the elements between lower_bound and upper_bound
        int total_sum = sum_tree.prefix_sum(upper_bound) - sum_tree.prefix_sum(lower_bound);

        // Adjust for elements that fall on the boundary
        total_sum += (count_tree.prefix_sum(lower_bound) - k) * lower_bound;
        total_sum -= (count_tree.prefix_sum(upper_bound) - (m - k)) * upper_bound;

        return total_sum / (m - 2 * k);
    }
};

"""
    