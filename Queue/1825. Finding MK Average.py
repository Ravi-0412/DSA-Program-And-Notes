# Logic: Just focus on how we will get sum of those remaining ele for which we have to find the average.

# Intutition: We need to remove the ele from start if len(data_structure) > m.
# so 'deque' comes into mind.

# But for calculatiing the average , we need to sort each time and remove 'first_k' and 'last_k' 
# so deque alone is not enough.

# So we need somthing that stores all 'm' element in sorted order always.
# for this 'sortedList' comes into mind.

# So finally we will store all upcoming element into sorted list and will check if it's length is > m
# then we will remove the possible ele and make decision accordingly.

# see the code for more clear explanation.

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
        