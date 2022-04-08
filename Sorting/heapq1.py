# 'haep' has some inbulit function
# import heapq
# arr= [5,7,9,1,3]
# heapq.heapify(arr)  # will create min heap
# print("the created heap is:\n", arr)
# heapq.heappush(arr,4)   # will insert '4' into the min heap 
#                         # and then will create the heap  automatically
# print(arr)
# print ("The popped item using heappushpop() is: ", end="") 
# print(heapq.heappushpop(arr,3)) # first insert the element(here '3') then pop 
#                                 # the smallest element from the resultant heap 
# print(arr)
# print ("The popped item using heapreplace() is : ",end="")
# print (heapq.heapreplace(arr, 2))    # first pop the smallest element then insert 
#                                     # the given  element into the heap resultant heap 
# print(arr)

# print("modified heap after insertion is:\n",arr)
# print("the popped and smallest element is:",end="")
# print(heapq.heappop(arr))  # will pop and return the smallest element
# print(arr)


# heap sort using 'heapq'
# import heapq
# def heapsort(arr):
#     heapq.heapify(arr)
#     print("created heap is: ", arr)
#     return [heapq.heappop(arr) for i in range(len(arr))]  # will pop the smallest element on by one
#                                                           # and will create a list of those elements
#                                                           # which will sort the element in ascending order
# arr= [1,3,0,8,5,9,2,6]
# print(heapsort(arr))


# # 'heappush' can be also used to insert tuple
# import heapq
# h= []
# heapq.heappush(h,(5,'write code'))
# heapq.heappush(h, (7, 'release product'))
# heapq.heappush(h, (1, 'write spec'))
# print(heapq.heappop(h))


# returning n largest element
import heapq
arr= [1,2,6,3,9,7,5,4,6,7,4]
print("the created heap is:\n", arr)
k= 4 # no of element you want to return or kth largest element 
     # depending upon whether key is specified or not
# print(heapq.nlargest(k,arr,key=None))  # will return list of k largest element in the array
# key (Optional): Specifies a function that has only one argument. If specified,
# a comparison key is extracted from each item in the iterable.
# print(heapq.nlargest(k,arr))   # this will also give the same output
# to gate kth largest element
print("{} the largest element is: {}".format(k,heapq.nlargest(k,arr)[-1]))  # will give kth largest element

# similarly 'nsmallest(k,arr,key=fun)' for smallest element
