def merge_sort(arr,low,up):
    if(low<up):   # to check if there is more than one element.
        mid= low+ (up-low)//2
        print(mid, "mid")
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,up)
        merge(arr,low,mid,up)

def merge(arr,low,mid,up):
    low1,up1,low2,up2= low,mid,mid+1,up
    b= []
    while(low1<= up1 and low2<= up2):
        if(arr[low1] <= arr[low2]):
            b.append(arr[low1])
            low1+=1
        else:
            b.append(arr[low2])
            low2+=1
    while(low1<=up1):
        b.append(arr[low1])
        low1+=1
    while(low2<=up2):
        b.append(arr[low2])
        low2+=1
    j= low
    k= 0
    # Now copy array 'b' to original array 'arr' for index 'low' to 'up'.
    while(j<=up):
        arr[j]= b[k]
        j+= 1
        k+= 1
    print(arr[low:mid + 1], arr[mid +1 : up])

arr= [8, 4, 2, 1]
# arr= []
n= len(arr)

merge_sort(arr,0,n-1)
print(arr)


# Java
"""
import java.util.Arrays;

class Solution {
    // Function to perform merge sort
    void mergeSort(int[] arr, int low, int up) {
        if (low < up) {
            int mid = low + (up - low) / 2;
            mergeSort(arr, low, mid);
            mergeSort(arr, mid + 1, up);
            merge(arr, low, mid, up);
        }
    }

    // Function to merge two sorted subarrays arr[low..mid] and arr[mid+1..up]
    void merge(int[] arr, int low, int mid, int up) {
        // Sizes of the two subarrays
        int n1 = mid - low + 1;
        int n2 = up - mid;

        // Create temporary arrays
        int[] left = new int[n1];
        int[] right = new int[n2];

        // Copy data to temporary arrays left[] and right[]
        for (int i = 0; i < n1; i++)
            left[i] = arr[low + i];
        for (int j = 0; j < n2; j++)
            right[j] = arr[mid + 1 + j];

        // Merge the temporary arrays back into arr[low..up]
        int i = 0, j = 0; // Initial indexes of left and right subarrays
        int k = low; // Initial index of merged subarray

        while (i < n1 && j < n2) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        // Copy remaining elements of left[], if any
        while (i < n1) {
            arr[k] = left[i];
            i++;
            k++;
        }

        // Copy remaining elements of right[], if any
        while (j < n2) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr = {8, 4, 2, 1};

        System.out.println("Original array:");
        printArray(arr);

        solution.mergeSort(arr, 0, arr.length - 1);

        System.out.println("Sorted array:");
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
