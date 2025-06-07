# time: O(nlogk)
# my mistakes: i was not able to handle the case when diff is equal
# and we have to return in sorted order-> this not said in Q but we have to return like this only
import heapq
def KClosest(arr,n,x,k):
    heap= []
    for i in range(len(arr)-1,-1,-1):
        diff= abs((x- arr[i]))
        heapq.heappush(heap, (-diff, arr[i]))
        if len(heap)> k:
            heapq.heappop(heap)
    for i in range(len(heap)):
        temp= heapq.heappop(heap)
        print(temp[1], end= " ")


# correct one
# Note: when we pass more than one parameter in heap then it will make the heap acc to first para only.
# If in case the first para is equal then it will make acc to the 2nd para and so on

# so to bring the small house no in case of match, add the num with negative sign
class Solution:
    def Kclosest(self, arr, n, x, k):
        from heapq import heapify,heappush,heappop
        heap=[]
        for i in arr:
            heapq.heappush(heap,(-abs(x-i),-i))   # to handle when distance(diff) is equal
            if len(heap)>k:
                heapq.heappop(heap)
        ans=[]
        for ele in heap:
            # print(-(i[1]),end=" ")
            ans.append(-ele[1])
        return sorted(ans)


# arr= [10, 2, 14, 4, 7, 6]
arr= [-21, 21, 4, -12, 20]
# KClosest(arr,6,5,3)
KClosest(arr,5,0,4)


# Java Code 
"""
import java.util.*;

class Solution {
    public List<Integer> KClosest(int[] arr, int n, int x, int k) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0]) return Integer.compare(b[1], a[1]); // To prioritize smaller numbers in case of tie
            return Integer.compare(b[0], a[0]);
        });

        for (int num : arr) {
            maxHeap.offer(new int[]{Math.abs(x - num), num});

            if (maxHeap.size() > k) {
                maxHeap.poll();
            }
        }

        List<Integer> ans = new ArrayList<>();
        while (!maxHeap.isEmpty()) {
            ans.add(maxHeap.poll()[1]);
        }

        Collections.sort(ans); // Ensuring sorted order as per original method
        return ans;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] arr = {-21, 21, 4, -12, 20};
        List<Integer> result = sol.KClosest(arr, 5, 0, 4);

        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> KClosest(vector<int>& arr, int n, int x, int k) {
        priority_queue<pair<int, int>> maxHeap;

        for (int i = arr.size() - 1; i >= 0; i--) {
            int diff = abs(x - arr[i]);
            maxHeap.push({-diff, arr[i]});

            if (maxHeap.size() > k) {
                maxHeap.pop();
            }
        }

        vector<int> ans;
        while (!maxHeap.empty()) {
            ans.push_back(maxHeap.top().second);
            maxHeap.pop();
        }

        sort(ans.begin(), ans.end()); // Ensuring sorted order as per original method
        return ans;
    }
};

int main() {
    vector<int> arr = {-21, 21, 4, -12, 20};
    Solution sol;
    vector<int> result = sol.KClosest(arr, 5, 0, 4);
    
    for (int num : result) {
        cout << num << " ";
    }

    return 0;
}
"""
