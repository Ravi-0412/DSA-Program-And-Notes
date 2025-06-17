# Method 1: 

# Logic: We have to minimise the idle time for overall minimum time.
# And for this we need to utilise the cooldown time between two task.
# And for reducing cooldown time between tasks process the most frequent one first as 
# during cooldown time of most frequent task we can schedule other tasks. => utilising cooldwon period thus reducing idle time.

# Note: if you process the less frequent char first then at last a lot of most frequent char will left 
# and you have to wait increasing idle.

# So from here we can think of using maxheap based on freq of each char

# most frequent task to ek bar pick karne pe uskla count decr karke phir se add karna hoga next time most freq find karne ke liye
# kyonki picked one ka freq count decr karne pe may be ab most freq nhi rah payega

# when a task has been processed at time 't' then next time it will be processed at time 't+n'.
# To check if any taks is available to process at any time 't' we will take help of 'Queue'

# here only frequency of each letter(task) will matter not their name.

# Logic: Each time take one most frequent element and add into queue with (cnt, next_time)
# Now check if we can process any task at this time or not.
# If we can process then again add that task in heap for later.

# time: O(26*logn + m*n). m= #tasks. in case tasks= a,a,a,a,... we may have to wait till m*n

import collections
from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq= Counter(tasks)
        # make a maxHeap with the freq of each char,only we have to take freq of each letter
        maxHeap= [-cnt for cnt in freq.values()]    # have to make max heap. Only here freq will matter.
                                                    # For checking same type of task, we are using queue to keep track of time.
        heapq.heapify(maxHeap)  
        q= collections.deque()
        time= 0
        # if maxHeap is empty and Q is not empty it means there is no ele whose next_process time is matching with curr_time 
        # then it will be counted as idle
        while maxHeap or q:  
            time+= 1
            if maxHeap:  
                # Process the most freq task available at this time 
                cnt= 1+ heapq.heappop(maxHeap)   # basically decr the freq of current task(made max heap with negative value so adding '1')
                if cnt!= 0:  # means same task has more time to process so add in 'Q' with [count,next_process_time]
                    q.append((cnt, time+ n))   # this task can be processed next time at 'time+n'
            # each time check if there is any task that can be processed at curr time, only need to check the 1st one as we are doing one task at a time
            if q and q[0][1]== time:  # then push into the maxHeap, only the count of task 
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
    

# Method 2: 
# Better one
# using logic of Q: "358. Rearrange String k Distance Apart".
# 1) We need to arrange the characters in string such that each same character is K distance apart,
#  where distance in this problems is time b/w two similar task execution.

# 2) Idea is to add them to a priority Q and sort based on the highest frequency.
# And pick the task in each round of 'n' with highest frequency. As you pick the task, 
# decrease the frequency, and put them back after the round.

from collections import defaultdict, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return -1
        
        # Step 1: Build a frequency map for tasks
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        # Step 2: Use max heap to schedule tasks by their frequencies
        maxHeap = []
        for key, value in freq.items():
            heapq.heappush(maxHeap, (-value, key))  # Store as (-frequency, task) for max heap

        cnt = 0
        while maxHeap:
            # Interval for cooldown
            interval = n + 1
            # Temporary list to store tasks to be updated
            temp = []
            
            # Process tasks within the interval
            while interval > 0 and maxHeap:
                neg_freq, task = heapq.heappop(maxHeap)
                freq_count = -neg_freq
                freq_count -= 1  # Decrease frequency since task is executed
                temp.append((freq_count, task))
                interval -= 1
                cnt += 1
            
            # Update tasks back to heap if they have remaining counts
            for freq_count, task in temp:
                if freq_count > 0:
                    heapq.heappush(maxHeap, (-freq_count, task))
            
            # If heap is empty, all tasks are processed
            if not maxHeap:
                break
            
            # If interval > 0, CPU is idle
            cnt += interval
        
        return cnt

