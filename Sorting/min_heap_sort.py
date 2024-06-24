def Heapify(arr,n,i):   # 'i': index of root node of the subtree
    smallest= i  # intialise smallest as root(parent)
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

def Build_Min_Heap(arr):
    k= int(len(arr)/2) - 1      # loop goes only upto (n/2 -1) because after this
                                # position there will be no child of any element
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


# # for sorting the array    
def Heap_Sort(arr):
    n= len(arr)
    Build_Min_Heap(arr)
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


# Java
"""
import java.util.Arrays;

class Solution {
    // Function to heapify a subtree rooted at index i in array arr of size n
    void heapify(int[] arr, int n, int i) {
        int smallest = i; // Initialize smallest as root
        int l = 2 * i + 1; // Left child position
        int r = 2 * i + 2; // Right child position

        // If left child is smaller than root
        if (l < n && arr[l] < arr[smallest])
            smallest = l;

        // If right child is smaller than smallest so far
        if (r < n && arr[r] < arr[smallest])
            smallest = r;

        // If smallest is not root
        if (smallest != i) {
            // Swap arr[i] and arr[smallest]
            int temp = arr[i];
            arr[i] = arr[smallest];
            arr[smallest] = temp;

            // Recursively heapify the affected sub-tree
            heapify(arr, n, smallest);
        }
    }

    // Function to build a min heap
    void buildMinHeap(int[] arr) {
        int n = arr.length;
        // Build heap (rearrange array)
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }
    }

    // Function to perform heap sort
    void heapSort(int[] arr) {
        int n = arr.length;
        buildMinHeap(arr);

        // One by one extract an element from heap
        for (int i = n - 1; i > 0; i--) {
            // Move current root to end
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Call heapify on the reduced heap
            heapify(arr, i, 0);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr = {100, 50, 20, 1, 3, 10, 5, 1, 1, 1};

        System.out.println("Original array:");
        printArray(arr);

        solution.heapSort(arr);

        System.out.println("Sorted array in ascending order:");
        printArray(arr);
    }

    // Utility function to print an array
    static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}

"""