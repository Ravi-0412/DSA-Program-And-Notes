# time= O(n)
# Method 1: 
# Logic: Make another array and put num in proper order
# After that copy these value in original arrays.

# Time = Space = O(n)

def Reorder(arr,indices):
    n = len(arr)
    temp = [0] * n;
    # arr[i] should be present at index[i] index
    for i in range(0,n):
        temp[indices[i]] = arr[i]

    # Copy temp[] to arr[]
    for i in range(0,n):
        arr[i] = temp[i]
        indices[i] = i


# Method 2: Optimising space to O(1).

# logic: start checking from index '0', if ele is at its correct position then only proceed to next ele.
# otherwise keep on swapping ele to its proper index and "indexes" also.

def Reorder(arr, indices):
    n= len(arr)
    i= 0
    while i < n:
        # curr ele is not at proper position
        if indices[i] != i:
            # send the curr ele to its proper index by swapping and also swap indices to check for next ele.
            ind= indices[i]  # to this index curr ele 'i'th ele of array should go.
            arr[i], arr[ind]= arr[ind], arr[i]
            indices[i], indices[ind]= indices[ind], indices[i]
        # curr ele is at proper position, so simply move further to chekc for next ele.
        # incr 'i' only in this case, because after swapping the cur ele at 'i' may not be at its correct position.
        else:
            i+= 1
    print("final num arr is :", arr)
    print("final indices arr is :", indices)
    
    
# arr= [10, 11, 12]
# indices = [1, 0, 2]

# arr=     [50, 40, 70, 60, 90]
# indices = [3,  0,  4,  1,  2]

arr = [10, 20, 30, 40, 50]
indices = [3, 1, 4, 0, 2] 

print(Reorder(arr, indices))


# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    // Method 1: Using extra space O(n)
    public void Reorder(int[] arr, int[] indices) {
        int n = arr.length;
        int[] temp = new int[n];

        // arr[i] should be present at index[i] index
        for (int i = 0; i < n; i++) {
            temp[indices[i]] = arr[i];
        }

        // Copy temp[] to arr[]
        for (int i = 0; i < n; i++) {
            arr[i] = temp[i];
            indices[i] = i;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] arr = {10, 20, 30, 40, 50};
        int[] indices = {3, 1, 4, 0, 2};

        s.Reorder(arr, indices);

        System.out.println("Final num arr is: " + Arrays.toString(arr));
        System.out.println("Final indices arr is: " + Arrays.toString(indices));
    }
}
//Method 2
import java.util.*;

class Solution {
    public void Reorder(int[] arr, int[] indices) {
        int n = arr.length;
        int i = 0;

        while (i < n) {
            // Current element is not at the correct position
            if (indices[i] != i) {
                // Send the current element to its proper index by swapping and also swap indices
                int ind = indices[i];  // This index should contain the current element
                int temp = arr[i];
                arr[i] = arr[ind];
                arr[ind] = temp;

                temp = indices[i];
                indices[i] = indices[ind];
                indices[ind] = temp;
            } else {
                // Current element is at the correct position, move further
                i++;
            }
        }

        System.out.println("Final num arr is: " + Arrays.toString(arr));
        System.out.println("Final indices arr is: " + Arrays.toString(indices));
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] arr = {10, 20, 30, 40, 50};
        int[] indices = {3, 1, 4, 0, 2};

        s.Reorder(arr, indices);
    }
}
"""

# C++ Code 
"""
//Method 1
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    // Method 1: Using extra space O(n)
    void Reorder(vector<int>& arr, vector<int>& indices) {
        int n = arr.size();
        vector<int> temp(n, 0);

        // arr[i] should be present at index[i] index
        for (int i = 0; i < n; i++) {
            temp[indices[i]] = arr[i];
        }

        // Copy temp[] to arr[]
        for (int i = 0; i < n; i++) {
            arr[i] = temp[i];
            indices[i] = i;
        }
    }
};

int main() {
    Solution s;
    vector<int> arr = {10, 20, 30, 40, 50};
    vector<int> indices = {3, 1, 4, 0, 2};

    s.Reorder(arr, indices);

    cout << "Final num arr is: ";
    for (int num : arr) cout << num << " ";
    cout << "\nFinal indices arr is: ";
    for (int index : indices) cout << index << " ";
    cout << endl;

    return 0;
}
//Method 2
class Solution {
public:
    void Reorder(vector<int>& arr, vector<int>& indices) {
        int n = arr.size();
        int i = 0;

        while (i < n) {
            // Current element is not at the correct position
            if (indices[i] != i) {
                // Send the current element to its proper index by swapping and also swap indices
                int ind = indices[i];  // This index should contain the current element
                swap(arr[i], arr[ind]);
                swap(indices[i], indices[ind]);
            } else {
                // Current element is at the correct position, move further
                i++;
            }
        }

        cout << "Final num arr is: ";
        for (int num : arr) cout << num << " ";
        cout << "\nFinal indices arr is: ";
        for (int index : indices) cout << index << " ";
        cout << endl;
    }
};
"""