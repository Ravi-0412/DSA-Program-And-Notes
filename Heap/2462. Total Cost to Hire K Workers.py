# Time: O(n*logn)

# Logic: we have to get minimum from a set of ele so heap should come into mind.

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        minHeap = []   # Will push (cost[i], i)
        l, r = 0, n - 1

        # push the 'candidates' ele from left side
        while l < candidates :
            heapq.heappush(minHeap, (costs[l] , l))
            l += 1
        
        # push the 'candidates' ele from right side. But we may left with less no of ele than candidates so using 2nd case
        while r >= n - candidates and r >= l:
            heapq.heappush(minHeap, (costs[r] , r))
            r -= 1
        # Now 'l' will represent 1st ele from left that we need to add if we pop element from left.
        # r: will represent 1st ele from right that we need to add if we pop element from right.
        
        ans = 0
        # we need to get k ele from heap for min cost
        for i in range(k):
            cost , ind = heapq.heappop(minHeap)
            ans += cost

            # Now we have to put ele in heap from that side from which we poped the cur ele i.e either left or right
            if ind < l :
                # Means cur poped ele id from left. so we will push next  ele from left only
                if l <= r:  # then only we can push
                    heapq.heappush(minHeap, (costs[l] , l))
                    l += 1

            else:
                # Means cur poped ele id from right. so we will push next  ele from right only
                if l <= r:  # then only we can push
                    heapq.heappush(minHeap, (costs[r] , r))
                    r -= 1
        return ans
