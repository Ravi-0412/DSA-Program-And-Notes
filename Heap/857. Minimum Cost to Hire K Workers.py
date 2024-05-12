# Logic: in notes , page no: 61

# Similar to q : "2542. Maximum Subsequence Score" .
# In that q: first sort in descending order + then apply minHeap

# Here 'first sort in ascending order + then apply maxHeap'.

# Time: O(n*logn + n*logk)

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = [] # (ratio / quality)
        for i in range(len(quality)):
            pairs.append((wage[i]/quality[i], quality[i]))
        pairs.sort(key = lambda x : x[0])   # sorting based on rate
        ans = float('inf')
        total_quality = 0    # of workers seen till now
        maxHeap = []
        for rate, q in pairs:
            heapq.heappush(maxHeap, -1*q)
            total_quality += q
            if len(maxHeap) > k:
                max_q = -1 * heapq.heappop(maxHeap)
                total_quality -= max_q
            if len(maxHeap) == k:
                ans = min(ans, total_quality * rate)
        return ans