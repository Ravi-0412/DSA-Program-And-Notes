def Heapify(arr,n,i):   # 'i': index of root node of the subtree from which we are starting the heapify function
                        # n denotes no of element in the subtree(before which we have to check)
    largest= i  # intialise largest as root(parent)
    l= 2*i +1   # left child postion of root (index is starting from 0)
    r= 2*i +2   # right child position of root
    if(l<n and arr[l]>arr[largest]):
        largest= l   # if left child is greater than root then make it largest
    if(r<n and arr[r]>arr[largest]):
        largest= r      # if right child is greater than root then make it largest
    if(largest!= i):            # if largest is not root means there is one child 
			                    # whose value is greater than its parent then,swap that child with 
							    # the parent to maintain max heap property
        arr[largest], arr[i]= arr[i], arr[largest]
        Heapify(arr,n,largest)  # again call heapify after each swap to maintain property of max heap

def Build_Max_Heap(arr):
    k= int(len(arr)/2) - 1      # loop goes only upto (n/2 -1) because after this
                                # position there will be no child of any element i.e start from last non-leaf node
    for i in range(k,-1,-1):
        Heapify(arr,len(arr),i)
    print("max heap is: ", arr)

# for sorting the array    
def Heap_Sort(arr):
    n= len(arr)
    Build_Max_Heap(arr)
    # one by one extract(delete) an element from the heap
    for i in range(n-1,0,-1):  # going till index '1' only because at last 0th ele will get sorted automatically
        # move the current root to the last
		# by this will largest element will go to the end and finally we will get sorted array
        arr[i] ,arr[0]= arr[0],arr[i]  # now one element is sorted i.e last ele went to last index
        Heapify(arr,i,0)  # again call heapify after each swap to maintain property of max heap. last index before we have to check will be 'i' only


# for kth largest element in the array
# def Heap_Sort(arr):
#     n= len(arr)
#     count= 0
#     k= int(input("enter the kth element"))
#     Build_Max_Heap(arr)
#     for i in range(n-1,0,-1):
#         arr[i] ,arr[0]= arr[0],arr[i]
#         count+= 1
#         if(count==k):
#             print("{}th largest elemnt is: {}".format(k,arr[i]))
#         Heapify(arr,i,0)


# # for deleting an element in the max heap 
# # any operations on heap just modify the build heap function
# def Build_Max_Heap(arr):
#     n= len(arr)
#     k= int(len(arr)/2) - 1      
#     for i in range(k,-1,-1):
#         Heapify(arr,len(arr),i)
#     print("max heap is: ", arr)
#     key= int(input("enter the element to delete \n"))
#     for i in range(n):
#         if(arr[i]==key):
#             arr[i],arr[n-1]= arr[n-1], arr[i]
#         Heapify(arr,n-1,i)
#     print("heap after deleting {} is {}: ".format(key,arr[0:n-1]))


# arr= [1,4,2,9,4,5,2,3,3,0,0]
# arr= [1,5,6,8,12,14,16,1]
arr= [100,50,20,1,3,10,5]
# Build_Max_Heap(arr)  # for operations on max heap
Heap_Sort(arr)
print("sorted array in ascending order: ", arr)




    

