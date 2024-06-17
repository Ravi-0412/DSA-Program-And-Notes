# just similar to "2402. Meeting Rooms III"

# logic: we need to keep track of all projects we can complete using curr 'w'.
# for this we will maintain a  minHeap.
# We need to store (capital , profit) pair to get maxProfit among all possible project.

# And from the all possible projects we have to take the most profitable project, so we will maintain a maxHeap for this.

# time: O(k* 2*logn), space= O(n)
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit= []   # stores the profit of projects we can afford with current 'w'. creating maxHeap to get the maxProfit project 
        minCapital= [(c, p) for c, p in zip(capital, profits)]   # creating minHeap for pair (c, p)
        heapq.heapify(minCapital)
        print(minCapital)

        for i in range(k):
            # add all the profits of projects that we can afford into maxProfit with current capital 'w'. 
            while minCapital and minCapital[0][0] <= w:
                c, p= heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1* p)
            # check if maxProfit is empty. if empty means we can't add any project so simply break  or return
            if not maxProfit:
                return w
            # Add the maxProfit project that we can afford with 'w'.
            w+= -1* heapq.heappop(maxProfit)
        return w
