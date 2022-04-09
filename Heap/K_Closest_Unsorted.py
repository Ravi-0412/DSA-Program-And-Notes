# time: O(nlogk)
# some cases not passing
import heapq
def KClosest(arr,n,x,k):
    heap,arr_diff= [], []
    # insert a tuple with abs diff of 'x and arr[i]' with the arr[i]
    for i in range(n):
        diff= abs(x- arr[i])    # taking diff of each ele
        arr_diff.append((-diff, arr[i]))  # to create max heap just change the sign of all numbers 
                                          # before inserting and after poping
    print(arr_diff)
    for i in range(n-1,-1,-1):
        heapq.heappush(heap, arr_diff[i])   # this will create a max heap with key of tuple for ele which is 'diff'
                                            # jiska distance kam hoga wahi closest 'k' ele hoga
                                            # heap me sorting 1st index wala ke anusar hoga agar ek se jyada ele ek bar me insert karte h to
        if len(heap)> k:
            heapq.heappop(heap)
    print(heap)
    # now you will left with k smallest and that will be your ans
    # just print in reverse order the value of array to get the ans in sorted format
    print("{} closest number is: ".format(k))
    for i in range(len(heap)-1,-1,-1):
        print(heap[i][1], end= " ")

# arr= [10, 2, 14, 4, 7, 6]
arr= [-21, 21, 4, -12, 20]
# KClosest(arr,6,5,3)
KClosest(arr,5,0,4)

