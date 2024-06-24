# method 1:
def insertion_sort(arr):
    n= len(arr)
    for i in range(1,n):
        temp= arr[i]   # when we will shift the ele then ele at 'i' will change. so we have to store in temp variable.
        j= i-1
        while j>=0 and arr[j]>temp :  # until you find ele <= temp.
                arr[j+1]= arr[j]    # move one 'j' one position ahead to create the space for 'temp'.
                j-= 1
        arr[j+1]= temp    # 'j' will be pointing to index '<=' temp so we will put 'temp' at 'j+1'.


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)


# Java
"""
import java.util.Arrays;

class Solution {
    void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int temp = arr[i]; // Store the current element to be inserted
            int j = i - 1;

            // Move elements of arr[0..i-1], that are greater than temp, to one position ahead
            // of their current position
            while (j >= 0 && arr[j] > temp) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = temp; // Insert temp into the correct position
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr = {12, 11, 13, 5, 6};

        System.out.println("Original array:");
        printArray(arr);

        solution.insertionSort(arr);

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