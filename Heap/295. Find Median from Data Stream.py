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


# method 3: 
# make two heap, one maxHeap(will contain smaller val only) and one minHeap(will contain larger val only) with properties: 
# i)  values in maxHeap <= value in minHeap
# ii) no of elements in both the heap should be equal(in case of even no) or difference in length of both the heaps should be equal to '1'
# basically maxHeap will contain the values till mid(or mid+1) and minHeap will contain values from/after mid

# if number is odd, then the heap having larger size will give the ans and
# if number is even then, avg of the largest value from maxHeap and smallest value from minHeap will give the ans
# we only care about two values but if we use only one heap, we will not get the middle two values
# but in this we will get that

# for adding: we will automatically add in the maxHeap
# after adding into maxHeap we will check for two cases:
# i)  out of order cases i.e if max ele in maxHeap is greater than smallest ele in minHeap
# ii) uneven size of both the heaps

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
