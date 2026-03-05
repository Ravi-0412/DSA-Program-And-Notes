
"""
Logic: in notes , page no: 61
Similar to q : "2542. Maximum Subsequence Score" .
In that q: first sort in descending order + then apply minHeap
Here 'first sort in ascending order + then apply maxHeap'.

"1. Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group."
So for any two workers in the paid group,
we have wage[i] : wage[j] = quality[i] : quality[j]
So we have wage[i] : quality[i] = wage[j] : quality[j]
We pay wage to every worker in the group with the same ratio compared to his own quality.

"2. Every worker in the paid group must be paid at least their minimum wage expectation."
For every worker, he has an expected ratio of wage compared to his quality.

So to minimize the total wage, we want a small ratio.
So we sort all workers with their expected ratio, and pick up K first worker.
Now we have a minimum possible ratio for K worker and we their total quality.

As we pick up next worker with bigger ratio, we increase the ratio for whole group.
Meanwhile we remove a worker with highest quality so that we keep K workers in the group.
We calculate the current ratio * total quality = total wage for this group.

We redo the process and we can find the minimum total wage.
Because workers are sorted by ratio of wage/quality.
For every ratio, we find the minimum possible total quality of K workers.

for more clarity: 
Note : To satisfy everyone in a group of K people, your Unit Rate must be the Maximum (wage / quality​) ratio among the people you picked. 
If you pick a lower rate, the most "expensive" person will quit.
Total Cost=Unit Rate×(Sum of all Qualities in the group)
1. To make this cost as small as possible, you have two levers:
    Keep the Unit Rate low.
    Keep the Sum of Qualities low.

We can't just pick the K people with the lowest ratios, because they might have huge qualities. 
We can't just pick the K people with the lowest qualities, because they might have huge ratios.

So we do this:
    Sort all workers by their ratio (qualitywage​).
    Start from the smallest ratio and slowly move up.
    As you move, the current worker's ratio is the "Unit Rate" for your group.
    Since the Unit Rate is fixed by the current worker, the only way to lower the cost is to pick K−1 other workers (from the ones you've already seen) who have the smallest qualities.

Q) "However, it is possible that current worker 
has the highest quality, so you removed his quality in the last step, 
which leads to the problem that you are "using his ratio without him".
Answer: It doesn't matter. The same group will be calculated earlier with smaller ratio.

And it doesn't obey my logic here: For a given ratio of wage/quality, find minimum total wage of K workers.

explain this ?
    
Time Complexity
O(NlogN) for sort.
O(NlogK) for priority queue.
"""

import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # 1. Calculate ratios and pair them with quality
        # We sort by ratio so that for any worker 'i', their ratio 
        # can satisfy all workers from '0' to 'i'.
        workers = sorted([(w / q, q) for q, w in zip(quality, wage)])
        
        min_cost = float('inf')
        sum_quality = 0
        max_heap = [] # We use a Max-Heap to track (and remove) the highest qualities
        
        for ratio, q in workers:
            # Add the current worker's quality to our potential pool
            sum_quality += q
            heapq.heappush(max_heap, -q) # Negative because Python has a Min-Heap
            
            # If our pool grows larger than K, we must fire someone.
            # Logic: To minimize (Ratio * Sum_Quality), we fire the person 
            # with the LARGEST quality to bring the sum down.
            if len(max_heap) > k:
                sum_quality += heapq.heappop(max_heap) # Subtracts the max quality
            
            # Once we have exactly K workers, we calculate the cost.
            # Because we sorted by ratio, the current 'ratio' is the 
            # minimum required to satisfy the most 'expensive' person in our heap.
            if len(max_heap) == k:
                min_cost = min(min_cost, ratio * sum_quality)
                
        return float(min_cost)

# Follow ups :
"""
1.The "Budget" Constraint
Interviewer: "What if you are given a fixed budget B, and instead of hiring exactly K workers, 
you want to hire the maximum number of workers possible?" 

It changes the problem from "minimize cost for a fixed size" to "maximize size for a fixed cost." 
Because we still have the proportionality rule, the "Total Cost" for a group is always (Current Ratio×Sum of Quality).

Logic & Thought Process
1. Sort by Ratio: Just like before, we sort workers by their qualitywage​ ratio. As we iterate, the current worker's ratio is our "Unit Rate."
2. Greedy Quality Management: Since the ratio is fixed for the group, the only way to fit more people into the budget B is to pick workers with the lowest qualities.
3. Dynamic Window:
  Add the current worker.
  Calculate the cost: Current Ratio×Sum of Quality.
  If the cost exceeds B, we must remove the worker with the highest quality to bring the cost down.
  Repeat this until the cost is ≤B.
4. Record the Max: The answer is the maximum number of workers we managed to hold in our heap at any point.

Time: O(N *logN) , space : O(N)
"""

import heapq

class Solution:
    def maxWorkersWithinBudget(self, quality: List[int], wage: List[int], budget: float) -> int:
        # Step 1: Sort by ratio (wage/quality)
        # We need the ratio to be the 'Unit Rate' for everyone currently in the heap
        workers = sorted([(w/q, q) for q, w in zip(quality, wage)])
        
        max_workers = 0
        sum_quality = 0
        max_heap = [] # Stores qualities of workers we are currently 'hiring'
        
        for ratio, q in workers:
            # 1. Add current worker to our potential group
            sum_quality += q
            heapq.heappush(max_heap, -q) # Max-heap to track the most 'expensive' quality
            
            # 2. Check if this group exceeds the budget at the current ratio
            # Cost = Ratio * Total Quality
            # We use a while loop because we might need to remove multiple 
            # high-quality workers to fit the budget at this new (higher) ratio.
            while max_heap and (ratio * sum_quality) > budget:
                # Remove the worker who consumes the most 'budget' (highest quality)
                highest_q = -heapq.heappop(max_heap)
                sum_quality -= highest_q
            
            # 3. Update the maximum number of workers we've successfully hired
            max_workers = max(max_workers, len(max_heap))
            
        return max_workers

"""
2. The "Quality Threshold"
Interviewer: "What if there is a rule that you cannot hire anyone whose quality is below a certain value Q_min or above Q_max?"

The Adjustment: This is a simple pre-filtering step. Before you even start the ratio calculation or sorting,
you iterate through the lists and remove any workers who don't meet the quality criteria.
"""
