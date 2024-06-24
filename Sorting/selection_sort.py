def swap(arr,x,y):
    temp= arr[x]
    arr[x]= arr[y]
    arr[y]= temp

def selection_sort(arr):
    n= len(arr)
    for i in range(n-1):
        min_index= i
        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index= j
        swap(arr,min_index,i)

lst= []
n= int(input("enter the number of elements \n")) 
print("enter the elements")   
for i in range(n):
    ele= int(input())
    lst.append(ele)

selection_sort(lst)
print(lst)


# Java
"""
import java.util.Arrays;

public class Solution {
    // Function to swap elements in an array
    static void swap(int[] arr, int x, int y) {
        int temp = arr[x];
        arr[x] = arr[y];
        arr[y] = temp;
    }

    // Function to perform selection sort
    static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            // Swap the found minimum element with the first element of the unsorted part
            swap(arr, minIndex, i);
        }
    }

    public static void main(String[] args) {
        int[] arr = {8, 4, 2, 1, 7, 5, 3, 6};

        System.out.println("Original array:");
        printArray(arr);

        selectionSort(arr);

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