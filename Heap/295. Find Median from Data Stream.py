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

# method 2: you can optimise the above solution
# instead of sorting the list each time median is called
# just add the number in the list in sorted order only
# this operation will take O(n) each time 
# so overall time : O(n*n)= O(n^2)


# method 2: 
# make two heap, one maxHeap(will contain smaller val only) and one minHeap(will contain larger val only) with properties: 
# i)  values in maxHeap <= value in minHeap
# ii) no of elements in both the heap should be equal(in case of even no) or difference in length of both the heaps should be max equal to '1'.
# Note:  maxHeap will contain the values till mid(or mid+1) and minHeap will contain values from/after mid if we will assume a sorted list combining both the heaps (maxHeap + minHeap).
# Note: infact top ele in maxHeap will give median ele if len(maxHeap) > len(minHeap) and same for 'minHeap'

# if number is odd, then the heap having larger size will give the ans since that will be having 'mid' ele when of the sorted list.
# if number is even then, avg of the largest value from maxHeap and smallest value from minHeap will give the ans, because maxHeap will contain the 1st mid value and minHeap will contain the 2nd mid val.

# Note: using one heap we will not get the middle two values.

# for adding: we will automatically add in the maxHeap
# after adding into maxHeap we will check for two cases:
# i)  out of order cases i.e if max ele in maxHeap is greater than smallest ele in minHeap. All ele in maxHEap <= All ele in minHeap.
# ii) uneven size of both the heaps. size difference must be max '1' then only we will get the median directly.

# pushing and poping take O(logn) in heap
# this q was based on this approach only
# time: O(n*logn)

import heapq
class MedianFinder:  
    def __init__(self):
        self.maxHeap, self.minHeap= [], []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1*num)    # since we are appending in maxHeap so mutliply by -1
        # check if heaps are not in order?
        if self.maxHeap and self.minHeap and (-1*self.maxHeap[0]) > self.minHeap[0]:
            # remove the ele from maxHeap and append that ele to the minHEap
            val= -1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
            
        # now check uneven size?
        if len(self.maxHeap)> len(self.minHeap) +1:  # diff can't be more than one
            # remove the ele from maxHeap and append that ele to the minHEap
            val= -1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
            
        if len(self.minHeap)> len(self.maxHeap) +1:  # diff can't be more than one
            # remove the ele from minHeap and append that ele to the maxHeap
            val= heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1*val)

    def findMedian(self) -> float:
        # if len of both the heaps are unequal then means total no of elements is odd so return the ele from heap which has larger length
        if len(self.maxHeap) > len(self.minHeap):
            return -1*self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        # if length is equal then return the average
        return (-1*self.maxHeap[0] + self.minHeap[0])/2


# method 3: very concise and logical
# meaning of minHeap and maxHeap is same as above.

# The length of 'maxHeap' n / 2 at all time and the length of the 'minHeap' is either n / 2 or n / 2 + 1 depend on n's parity. (if even then n//2 else n//2 +1).

# 1) for Adding:
# a) if both heap has equal length means after adding one ele n will be odd.
# so we have to bring one ele from 'maxHeap' to 'minHeap' since 'minHeap' will contain oen extra ele(median one only) in case of odd number of ele.
# But we should bring the max ele from 'maxHeap' after adding the curr ele into 'maxHeap'. 
# This will make sure that all ele in minHeap >= all ele in maxHeap.

# Q) why we are not adding directly into 'minHeap'?
# Reason: it will not make sure that "all ele in minHeap >= all ele in maxHeap".

# b) if heap has unequal length i.e len(minHeap) > len(maxHeap) by '1'.
# then after adding the curr ele, total no of ele will be even. so in this case both heap should contain equal no of ele follwing the property "all ele in minHeap >= all ele in maxHeap".

# In this case we have to bring one ele from 'minHeap' to 'maxHeap'. we should bring the minium ele from 'minHeap' after adding the curr ele into minHeap.
# for this 1st we will add the curr ele into minHeap then pop the the 1st ele and after that will add that poped ele into 'maxHeap'. (like 'a').

# 2) to get the median
# a) if len of heaps is not equal then our median will in 'minHeap' (minHeap will contain extra ele in case if total no of ele is odd).
# b) average of 1st ele in both the heaps will be median.

# time: O(n*logk)

class MedianFinder:  
    def __init__(self):
        self.maxHeap, self.minHeap= [], []
        
    def addNum(self, num: int) -> None:
        if len(self.minHeap)== len(self.maxHeap):
            heapq.heappush(self.minHeap, -1*heapq.heappushpop(self.maxHeap, -1*num))
        else:
            heapq.heappush(self.maxHeap, -1*heapq.heappushpop(self.minHeap, num))

    def findMedian(self) -> float:
        if len(self.minHeap)!= len(self.maxHeap): # median is in minHeap at the top
            return self.minHeap[0]
        # if length is equal then return the average
        return (self.minHeap[0] - self.maxHeap[0])/2  # return (self.minHeap[0] + -1*self.maxHeap[0])/2


# method 4: using "sortedList"
# very easy (method 1 only but time complexity is optimised due to "SortedList").
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


# my mistake method 3:
# was adding directly first into the 'minHeap' then was checking length .
# may the wrong ans in case of odd ele because median can be in the 'maxHeap' in this case.
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