# Root to leaf
def Heapify(arr,n,i):   # 'i': index of root node of the subtree, n: no of ele till we have to traverse
    smallest= i  # intialise smallest as root(parent). using '0' based indexing
    l= 2*i +1   # left child postion of root
    r= 2*i +2   # right child position of root
    if(l<n and arr[l]<arr[smallest]):
        smallest= l   # if left child is smaller than root then make it smallest
    if(r<n and arr[r]<arr[smallest]):
        smallest= r      # if right child is smaller than root then make it smallest
    if(smallest!= i):            # if smallest is not root means there is one child 
			                    # whose value is smaller than its parent then,swap that child with 
							    # the parent to maintain max heap property
        arr[smallest], arr[i]= arr[i], arr[smallest]
        Heapify(arr,n,smallest)  # again call heapify after each swap to maintain property of max heap

# bottom up
def Build_Min_Heap(arr):
    k= int(len(arr)/2) - 1      # loop goes only upto (n/2 -1) because after this
                                # position there will be no child of any element in complete Binary Tree
    for i in range(k,-1,-1):
        Heapify(arr,len(arr),i)
    print("min heap is: ", arr)


# # for kth smallest element in the array
# def Heap_Sort(arr):
#     n= len(arr)
#     count= 0
#     k= int(input("enter the kth element"))
#     Build_Min_Heap(arr)
#     for i in range(n-1,0,-1):
#         arr[i] ,arr[0]= arr[0],arr[i]
#         count+= 1
#         if(count==k):
#             print("{}th smallest element is: {}".format(k,arr[i]))
#         Heapify(arr,i,0)


# # for sorting the array in descending order
def Heap_Sort(arr):
    n= len(arr)
    Build_Min_Heap(arr)
    # heapq.heapify(arr)  # this is not allowed here, have to implement from basic

    # one by one extract(delete) an element from the heap
    for i in range(n-1,0,-1):
        # move the current root to the last
		# by this will largest element will go to the end and finally we will get sorted array
        arr[i] ,arr[0]= arr[0],arr[i]
        Heapify(arr,i,0)  # again call heapify after each swap to maintain property of max heap


arr= [100,50,20,1,3,10,5,1,1,1]
Heap_Sort(arr)
print("sorted array in descending order: ", arr)
# Build_Min_Heap(arr)  # for operations on max heap


