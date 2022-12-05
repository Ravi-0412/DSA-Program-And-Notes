# time: O(nlogk)
# my mistakes: i was not able to handle the case when diff is equal
# and we have to return in sorted order-> this not said in Q but we have to return like this only
import heapq
def KClosest(arr,n,x,k):
    heap= []
    for i in range(len(arr)-1,-1,-1):
        diff= abs((x- arr[i]))
        heapq.heappush(heap, (-diff, arr[i]))
        if len(heap)> k:
            heapq.heappop(heap)
    for i in range(len(heap)):
        temp= heapq.heappop(heap)
        print(temp[1], end= " ")


# correct one
# Note: when we pass more than one parameter in heap then it will make the heap acc to first para only.
# If in case the first para is equal then it will make acc to the 2nd para and so on

# so to bring the small house no in case of match, add the num with negative sign
class Solution:
    def Kclosest(self, arr, n, x, k):
        from heapq import heapify,heappush,heappop
        heap=[]
        for i in arr:
            heapq.heappush(heap,(-abs(x-i),-i))   # to handle when distance(diff) is equal
            if len(heap)>k:
                heapq.heappop(heap)
        ans=[]
        for ele in heap:
            # print(-(i[1]),end=" ")
            ans.append(-ele[1])
        return sorted(ans)


# arr= [10, 2, 14, 4, 7, 6]
arr= [-21, 21, 4, -12, 20]
# KClosest(arr,6,5,3)
KClosest(arr,5,0,4)

