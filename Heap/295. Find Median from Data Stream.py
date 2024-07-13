# method 1: very direct and simple. Brute Force
# just add the num into a list and for median sort the list and return the ans according to the length of the list
# every time median is called, we are sorting the array 
# time: O(1*log1+ 2*log2+ 3*log3 + 4*log4..... + (5*10^4)*log(5*10^4))
class MedianFinder:
    def __init__(self):
        self.nums= []
        
    def addNum(self, num: int) -> None:
        self.nums.append(num)
        
    def findMedian(self) -> float:
        self.nums.sort()
        mid= len(self.nums)//2
        if len(self.nums)%2 != 0:
            return self.nums[mid]
        else:
            return (self.nums[mid] + self.nums[mid-1])/2

# method 2:
# If we can find any data structure which :
# 1) Automtically store element in sorted order in less than O(n) 
# 2) add, delete operation in O(n) then we can solve this question.

# So "sortedList" comes into mind in python.
# It maintaion sorted order autoamtically and supports add, delete operation in O(logn).

# time: O(n*logk)

from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.lst= SortedList()
        
    def addNum(self, num: int) -> None:
        self.lst.add(num)

    def findMedian(self) -> float:
        n= len(self.lst)
        if n % 2:
            return self.lst[n//2]
        return (self.lst[n//2 -1] + self.lst[n//2])/2


# method 3:
# Most important for interview.

# Logic: If we can get two middle in case of even no of elements and middle one in case of odd no of elements
# in O(1) or O(logn) then we can solve the problem.

# But how can we do that?
# If we create two heaps one min and one max heap such that :
# 1) Max Heap store n//2 minimum ele , min Heap store 'n/2' or 'n/2 + 1' maximum elements till now.
# 2) The length of 'maxHeap' is n / 2 at all time and the length of the 'minHeap' is either n / 2 or n / 2 + 1 depend on n's parity. 
# (if even then n//2 else n//2 +1).

# top of min heap: will have minimum(largest n//2 or n/2 + 1 ele)  and
# Top of max heap: will have maximum(smallest n//2 ele) till now.
# And for finding median we only need these two ele.

# in case of odd no of ele , we will try to keep extra ele(median only) at the top of min heap(minHeap[0]).

# So in case of odd ele top of minHeap will give the ans , and in case of odd ele
# (minHeap[0] + maxHeap[0])//2 will give the ans.

# 1) for Adding:
# a) if both heap has equal length means after adding one ele n will be odd.
# so we have to bring one ele from 'maxHeap' to 'minHeap' 
# since 'minHeap' will contain one extra ele(median one only) in case of odd number of ele.
# note: MinHeap will have already 'n/2' maximum element but in case of odd one
# It should get one ele so that minHeap contain 'n/2 + 1' maximum ele.

# To make sure this condition first we have to push current 'num' in maxHeap and then 
# Add the maxium ele of maxHeap into minHeap.

# Short: 
# But we should bring the max ele from 'maxHeap' after adding the curr ele into 'maxHeap'. 
# This will make sure that all ele in minHeap >= all ele in maxHeap.

# Q) why we are not adding directly into 'minHeap'?
# Reason: it will not make sure that "all ele in minHeap >= all ele in maxHeap".

# b) if heap has unequal length i.e len(minHeap) > len(maxHeap) by '1' (no of ele is odd).
# then after adding the curr ele, total no of ele will be even. 
# so in this case both heap should contain equal no of ele follwing the property "all ele in minHeap >= all ele in maxHeap".

# In this case we have to bring one ele from 'minHeap' to 'maxHeap'. 
# we should bring the minium ele from 'minHeap' after adding the curr ele into minHeap.

# for this 1st we will add the curr ele into minHeap then pop the the 1st ele and 
# after that will add that poped ele into 'maxHeap' (like 'a').

# 2) to get the median
# a) if len of heaps is not equal then our median will in 'minHeap' (minHeap will contain extra ele in case if total no of ele is odd).
# b) average of 1st ele in both the heaps will be median.

# time: O(n*logk)

import heapq
class MedianFinder:  
    def __init__(self):
        self.maxHeap, self.minHeap= [], []
        
    def addNum(self, num: int) -> None:
        if len(self.minHeap)== len(self.maxHeap):
            # First push 'num' into maxHeap then pop one ele from maxHeap and at last add that to minHEap.
            heapq.heappush(self.minHeap, -1*heapq.heappushpop(self.maxHeap, -1*num))
        else:
            # First push 'num' into minHeap then pop one ele from minHeap and at last add that to maxHEap.
            heapq.heappush(self.maxHeap, -1*heapq.heappushpop(self.minHeap, num))

    def findMedian(self) -> float:
        if len(self.minHeap)!= len(self.maxHeap): # median is in minHeap at the top
            return self.minHeap[0]
        # if length is equal then return the average
        return (self.minHeap[0] - self.maxHeap[0])/2  # return (self.minHeap[0] + -1*self.maxHeap[0])/2


# my mistake method 4:
# was adding directly first into the 'minHeap' then was checking length .
# may give wrong ans in case of odd ele because median can be in the 'maxHeap' in this case.
class MedianFinder:  
    def __init__(self):
        self.maxHeap, self.minHeap= [], []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -1*heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap)!= len(self.maxHeap): # median is in minHeap at the top
            return self.minHeap[0]
        # if length is equal then return the average
        return (self.minHeap[0] - self.maxHeap[0])/2

# Note: In this type of Q or similar question like :
"2102. Sequentially Ordinal Rank Tracker" 

# Just think how can get the elements that matter to our ans and how to get those ele optimally.
# e.g: in this q only two middle element matters only.

# "2102. Sequentially Ordinal Rank Tracker" :
# only one element matter to us for our ans.


# java
"""
// Not able to find data structure which function same as 'sortedList' in java.
# We can use TreeSet to maintain a sorted collection of numbers and add/ delete operation in O(logn) but TreeSet does not allow duplicates.
# so Treeset won't work here.

// method 3: Using two heaps

class MedianFinder {
    private PriorityQueue<Integer> maxHeap;
    private PriorityQueue<Integer> minHeap;
    
    public MedianFinder() {
        // Max-heap (contains the smaller half of the numbers)
        maxHeap = new PriorityQueue<>((a,b)-> b - a);
        // Min-heap (contains the larger half of the numbers)
        minHeap = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        if (minHeap.size() == maxHeap.size()) {
            // First push 'num' into maxHeap then pop one element from maxHeap and at last add that to minHeap.
            maxHeap.offer(num);
            minHeap.offer(maxHeap.poll());
        } else {
            // First push 'num' into minHeap then pop one element from minHeap and at last add that to maxHeap.
            minHeap.offer(num);
            maxHeap.offer(minHeap.poll());
        }
    }
    
    public double findMedian() {
        if (minHeap.size() != maxHeap.size()) {
            // Median is in minHeap at the top
            return minHeap.peek();
        }
        // If lengths are equal, return the average
        return (minHeap.peek() + maxHeap.peek()) / 2.0;
    }
}
"""
