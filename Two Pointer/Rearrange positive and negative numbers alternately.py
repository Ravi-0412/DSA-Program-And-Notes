# Just similar to : Print alternate odd even in given order
def rearrange_alternate_pos_neg(arr):
    n = len(arr)
    pos_index = 0
    neg_index = 0
    ans = []
    
    while pos_index < n or neg_index < n:
        # Find the next positive number to print
        while pos_index < n and arr[pos_index] < 0:
            pos_index += 1
        if pos_index < n:
            ans.append(arr[pos_index])
            pos_index += 1

        # Find the next negative number to print
        while neg_index < n and arr[neg_index] >= 0:
            neg_index += 1
        if neg_index < n:
            ans.append(arr[neg_index])
            neg_index += 1
    
    return ans

# Test cases
arr1 = [1, 2, 3, -4, -1, 4]
arr2 = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

print(rearrange_alternate_pos_neg(arr1))  # Output: [1, -4, 2, -1, 3, 4]
print(rearrange_alternate_pos_neg(arr2))  # Output: [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]

# Java
"""
Why are we using 'Arrays.toString()'? Why are we don't printing directly?

Reason?
In Java, when you want to print the contents of an array directly using 'System.out.println',
it will print the reference to the array object in memory, which can look something like [I@6d06d69c.

Note: Won't give the array content like Python.

The Arrays.toString() method from the java.util.Arrays class converts the array into a 
human-readable String format. When you call Arrays.toString(array), 
it returns a String that represents the elements of the array in a readable format, such as [1, 2, 3].

e.g:
import java.util.Arrays;

public class ArrayPrintExample {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};

        // Attempting to print the array directly
        System.out.println(numbers);  // Prints the reference: something like [I@6d06d69c

        // Using Arrays.toString() to print the contents
        System.out.println(Arrays.toString(numbers));  // Prints: [1, 2, 3, 4, 5]
    }
}

"""


"""
import java.util.Arrays;

public class RearrangeArray {
    
    // Method to rearrange the array
    public static int[] rearrangeAlternatePosNeg(int[] arr) {
        int n = arr.length;
        int posIndex = 0;  // Pointer for positive numbers
        int negIndex = 0;  // Pointer for negative numbers
        int[] result = new int[n];  // Array to store the result
        
        // Index to fill in the result array
        int index = 0;

        // While there are still elements to process
        while (posIndex < n || negIndex < n) {
            // Find the next positive number
            while (posIndex < n && arr[posIndex] < 0) {
                posIndex++;
            }
            if (posIndex < n) {
                result[index++] = arr[posIndex++];
            }

            // Find the next negative number
            while (negIndex < n && arr[negIndex] >= 0) {
                negIndex++;
            }
            if (negIndex < n) {
                result[index++] = arr[negIndex++];
            }
        }

        return result;  // Return the rearranged array
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 2, 3, -4, -1, 4};
        int[] arr2 = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8};

        // Testing the rearrangement
        System.out.println(Arrays.toString(rearrangeAlternatePosNeg(arr1))); // Output: [1, -4, 2, -1, 3, 4]
        System.out.println(Arrays.toString(rearrangeAlternatePosNeg(arr2))); // Output: [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
    }
}

"""
