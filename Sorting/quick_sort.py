# Pivot_index of 'num'(pivot) means aisa index say 'j' find karna h 
# i) jiske bad i.e ele on right side of j' i.e from 'j+1' to 'n-1' is  >= num and
# ii) left side 'i' ele is <= pivot.
# then num ko 'j' pe rakh de to 'num' sort jo jaye i.e left me <= and right me >=.

# Note: But case me equal_to(=) condition lagayenge tb galat ho jayega. Isliye kisi ek case me lagana h.


def partition(arr,low,up):
    i, j= low, up
    pivot = arr[low]
    while i < j:
        # 1) for getting all ele on right > pivot. Find 1st index where arr[j] <= pivot.
        # increment 'i' until you find any element <= pivot
        while arr[j] > pivot:
            j-= 1
        # 2) for getting all ele on left  <= pivot. Find 1st index where arr[i] > pivot.
        # increment 'i' until you find any element greater than pivot
        while i < j and arr[i] <= pivot: 
            i+= 1
        if i < j:
            # Bringing smaller ele to left and bigger ele to right.
            arr[i], arr[j]= arr[j], arr[i]
    #wherever this condition fails means we have found 
	# the proper position of pivot and 'j' will give that
    # now,swap a[j] with pivot for proper position of pivot element

    # arr[j], pivot= pivot, arr[j]  # this will give incorrect output because you are just swapping the
                                    # arr[j] with value of pivot, not inside the array
                                    # but you have to change with element at pivot index then 
                                    #only it will get swapped inside the array
    arr[j], arr[low]= arr[low], arr[j]
    # after this pivot element will be get sorted
    # 'j' returns the proper index of pivot element i.e
	# all the elements on the left side of this index value 
	# will be smaller than the pivot element and all
	# the elements on the right side will be greater than pivot element
    return j

def quick_sort(arr,low,up):
    if(low < up):  # checking if there is more than one element.
        q= partition(arr,low,up)
        quick_sort(arr,low,q-1)
        quick_sort(arr,q+1,up)


# Java
"""
class Solution {
    public void quickSort(int[] arr, int low, int up) {
        if (low < up) { // Checking if there is more than one element
            int q = partition(arr, low, up);
            quickSort(arr, low, q - 1);
            quickSort(arr, q + 1, up);
        }
    }

    private int partition(int[] arr, int low, int up) {
        int i = low, j = up;
        int pivot = arr[low];

        while (i < j) {
            // Find the first element from the right that is <= pivot
            while (arr[j] > pivot) {
                j--;
            }
            // Find the first element from the left that is > pivot
            while (i < j && arr[i] <= pivot) {
                i++;
            }
            if (i < j) {
                // Swap elements to bring smaller elements to the left and larger to the right
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        // Swap the pivot element to its correct position
        arr[low] = arr[j];
        arr[j] = pivot;

        return j;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr = {10, 7, 8, 9, 1, 5};
        int n = arr.length;

        System.out.println("Unsorted array: ");
        for (int num : arr) {
            System.out.print(num + " ");
        }

        solution.quickSort(arr, 0, n - 1);

        System.out.println("\nSorted array: ");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}

"""