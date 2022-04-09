# just like 'finding kth largest' 
# to get the first smallest ele , you have only to traverse till 'k+1' ele of the array
# as these ele can go till point only 
# after inserting k+1 element in heap , you will start getting the smallest ele at top in heap
# just same as pre don eQ
# after loop end just do the same for remaining ele in heap
import heapq
def Sort_K_Sorted(arr,k):
    heap, ans= [], []
    for num in arr:
        heapq.heappush(heap,num)     
        if len(heap)> k:   # for getting           
            ans.append(heapq.heappop(heap))    
    # After this all elements except k largest element will get sorted 
    # arr will contain only 'k largest ele'
    while(heap):
        ans.append(heapq.heappop(heap))  
    return ans  

arr= [6, 5, 3, 2, 8, 10, 9]
print("sorted array is: ")
print(Sort_K_Sorted(arr, 3))
