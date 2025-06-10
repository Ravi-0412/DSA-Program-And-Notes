

# here we are greedy about finding the 1st ele of group.
# and first ele must be minimum only and for this we will use minHeap

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n= len(hand)
        if n % groupSize!= 0:
            return False
        if groupSize== 1:
            return True
        cnt= collections.defaultdict(int)
        for num in hand:
            cnt[num]+= 1
        heapq.heapify(hand)    # since we want minimum each time for a group
        print(hand)
        for i in range(n//groupSize):
            # finding the 1st ele of group
            first_ele= heapq.heappop(hand)
            # check if this ele has already occured to it's frequency and find the ele with atleast one freq remaining.
            while cnt[first_ele]== 0:
                first_ele = heapq.heappop(hand)
            
            # now find all the elements of the group, we have got the starting ele of gr in 'start'
            # other remaining number must be consecutive to that.
            for i in range(groupSize):
                cnt[first_ele]-= 1
                if cnt[first_ele] < 0:  # means this no is not available or it has been used equal to no of times of it's frequency.
                    return False
                first_ele+= 1
        return True


# Method 2: No need of heap, we can sort and use pointer
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # Time: O(nlogn) + O(n*W)
        counter = Counter(hand) # O(n)
        hand.sort() # O(nlogn)
        i, n = 0, len(hand)
        while i < n: # O(n)
            cur = hand[i]
            for j in range(W): # O(W)
                if cur+j not in counter:
                    return False
                counter[cur+j] -= 1
                if counter[cur+j] == 0:
                    del counter[cur+j]
            # Move 'i' to the next smaller element from which we can start next group
            while i < n and hand[i] not in counter:
                i += 1
        return True
    
# Brute force will be very tough and complicated in this. so we have to find any pattern.

# Java Code 
"""
// Method 1: Using Min Heap
import java.util.*;

class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        int n = hand.length;
        if (n % groupSize != 0) return false;
        if (groupSize == 1) return true;

        Map<Integer, Integer> cnt = new HashMap<>();
        for (int num : hand) {
            cnt.put(num, cnt.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int num : hand) {
            minHeap.offer(num);
        }

        for (int i = 0; i < n / groupSize; i++) {
            int first_ele = minHeap.poll();
            while (cnt.get(first_ele) == 0) {
                first_ele = minHeap.poll();
            }

            for (int j = 0; j < groupSize; j++) {
                cnt.put(first_ele, cnt.getOrDefault(first_ele, 0) - 1);
                if (cnt.get(first_ele) < 0) return false;
                first_ele++;
            }
        }
        return true;
    }
}

// Method 2: Using sorting and Counter map
class Solution2 {
    public boolean isNStraightHand(int[] hand, int W) {
        Map<Integer, Integer> counter = new TreeMap<>();
        for (int num : hand) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        Arrays.sort(hand);
        int i = 0, n = hand.length;
        while (i < n) {
            int cur = hand[i];
            for (int j = 0; j < W; j++) {
                if (!counter.containsKey(cur + j)) return false;
                counter.put(cur + j, counter.get(cur + j) - 1);
                if (counter.get(cur + j) == 0) {
                    counter.remove(cur + j);
                }
            }
            while (i < n && !counter.containsKey(hand[i])) {
                i++;
            }
        }
        return true;
    }
}

"""

# C++ Code 
"""
// Method 1: Using Min Heap
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int n = hand.size();
        if (n % groupSize != 0) return false;
        if (groupSize == 1) return true;

        unordered_map<int, int> cnt;
        for (int num : hand) {
            cnt[num]++;
        }

        priority_queue<int, vector<int>, greater<int>> minHeap(hand.begin(), hand.end());

        for (int i = 0; i < n / groupSize; i++) {
            int first_ele = minHeap.top(); minHeap.pop();
            while (cnt[first_ele] == 0) {
                first_ele = minHeap.top(); minHeap.pop();
            }

            for (int j = 0; j < groupSize; j++) {
                cnt[first_ele]--;
                if (cnt[first_ele] < 0) return false;
                first_ele++;
            }
        }
        return true;
    }
};

// Method 2: Using sorting and Counter map
#include <map>

class Solution2 {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        map<int, int> counter;
        for (int num : hand) {
            counter[num]++;
        }

        sort(hand.begin(), hand.end());
        int i = 0, n = hand.size();
        while (i < n) {
            int cur = hand[i];
            for (int j = 0; j < W; j++) {
                if (counter.find(cur + j) == counter.end()) return false;
                counter[cur + j]--;
                if (counter[cur + j] == 0) {
                    counter.erase(cur + j);
                }
            }
            while (i < n && counter.find(hand[i]) == counter.end()) {
                i++;
            }
        }
        return true;
    }
};

"""