# first convert all the number into even.
# Then keep on dividing until max_ele is even.

# vvi: for odd number , we can perform only one operation i.e n*2 for one time since it will become 'even' after multiplying with '2'.
# on even number we can perform operation any number of time till it becomes odd.

# How to think of this approach and explainin interview?
# If we make all numbers even then if we get our maximum ele as odd then no longer we can perform any operation
# to minimise our ans.

# How to do this?
# We only need to keep track of minimum ele and maximum ele.
# But we have to perform operation on maximum ele again and again i.e we need to get maximum ele and perform operation each time.
# for this maxHeap comes into mind.

# Note vvvi: Whenever you have to perform operation on min/max ele again and again 
# (i.e do operation and put the result and again in array and do the same operation on new array),
# always think of min/max heap respectively.

# So for performing operation on maximum ele we can use maxHeap and can use a varible for keepingh track of minimum ele.

# time: O(n*logn*logm + n)   # we have to make the highest number('m') to odd number so 'logm' i.e maximum variation of max number.

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maxHeap= []   # creating maxHeap to get the maximum of the array in logn.
        minimum= float('inf')   # will keep track of minimum ele in the array at any point of time.
        # O(nlogn)
        for n in nums:
            if n % 2:  # if odd
                n= n*2   # making all odd to its maximum possible value it can take.
            minimum= min(minimum, n)
            heapq.heappush(maxHeap, -1*n)   # creating the maxHeap so pushing the negative value.

        difference= float('inf')    # will give the difference between minValue and maxValue at any point of time.
        # o(n*logn*logm)   # we have to make the highest number('m') to odd number so 'logm' i.e maximum variation of max number.
        while -1* maxHeap[0] % 2==0:   # while max ele is even. Reducing the max and max can be reduced to an odd number.
            maximum= -1* heapq.heappop(maxHeap)            
            difference= min(difference, maximum- minimum)
            minimum= min(minimum, maximum//2)
            heapq.heappush(maxHeap, -1* maximum//2)
        return min(difference, -1* maxHeap[0]- minimum)  # update last time also.

