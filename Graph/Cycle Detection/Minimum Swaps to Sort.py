# Method 1: sorting + using hashmap
#Link: https://leetcode.com/discuss/general-discussion/1296769/min-no-of-swaps-to-sort-the-array-wrong-approach-vs-correct-approach

# Approach:
"""
Approach:
Store the elements value and their corresponding index in a pair and we have a vector of pairs
now sort the vector according to their value
Now traverse this vector V and compare V[i].second & i
If equal that means they were at the same position in the orignal array so dont do anything else swap V[i] with V[ V[i].second]
Now it may happen that even after swapping the element is not in the correct position so we do i--
In a way we first sort the array and then compare it with the orignal array to to find the swaps.
"""

# Tme: O(n*logn)

class Solution:
    
    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, arr):
        n = len(arr)
        
        # Create a list of pairs (value, index)
        v = [(arr[i], i) for i in range(n)]
        
        # Sort the list using a lambda expression
        v.sort(key=lambda x: x[0])
        
        swaps = 0
        i = 0
        
        while i < n:
            # If the current element is already in the correct position
            if v[i][1] == i:
                i += 1
                continue
            else:
                swaps += 1
                
                # Swap the current element with the correct element
                correct_index = v[i][1]
                v[i], v[correct_index] = v[correct_index], v[i]
        
        return swaps

# java
"""


import java.util.*;

class Solution {
    
    // Function to find the minimum number of swaps required to sort the array.
    public int minSwaps(int[] arr) {
        int n = arr.length;
        
        // Create a list of pairs (value, index)
        List<Pair> v = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            v.add(new Pair(arr[i], i));
        }
        
        // Sort the list using a lambda expression
        v.sort((p1, p2) -> Integer.compare(p1.value, p2.value));
        
        int swaps = 0;
        int i = 0;
        
        // Replace for loop with a while loop
        while (i < n) {
            // If the current element is already in the correct position
            if (v.get(i).index == i) {
                i++;
                continue;
            } else {
                swaps++;
                
                // Swap the current element with the correct element
                Pair temp = v.get(i);
                v.set(i, v.get(v.get(i).index));
                v.set(temp.index, temp);
            }
        }
        
        return swaps;
    }
    
    // Custom Pair class to hold value and index
    static class Pair {
        int value, index;

        public Pair(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }
}

"""

# Method 2: using graph, best one
# Logic:
"""
when we will try to put element at correct position then, it will form a cycle.
And to rearrange those elements of a single cycle we will need 'cycle-size - 1' swaps.

Note: More detailed in ipad 
"""

# Time: O(n*logn)

class Solution:
    
    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, arr):
        n = len(arr)
        # Create a list of pairs (value, index)
        pairs = [(arr[i], i) for i in range(n)]
        
        # Sort the pairs by value
        pairs.sort(key=lambda x: x[0])
        
        # To keep track of visited elements
        visited = [False] * n
        swaps = 0

        for i in range(n):
            # If already visited or already in the correct position
            if visited[i] or pairs[i][1] == i:
                continue
            
            # Find the cycle size
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pairs[j][1]
                cycle_size += 1
            
            # If there is a cycle, add (cycle_size - 1) to swaps
            if cycle_size > 1:
                swaps += (cycle_size - 1)

        return swaps

# java
"""
import java.util.*;

class Solution {
    
    // Function to find the minimum number of swaps required to sort the array.
    public int minSwaps(int[] arr) {
        int n = arr.length;
        
        // Create a list of pairs (value, index)
        List<Pair> pairs = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            pairs.add(new Pair(arr[i], i));
        }
        
        // Sort the pairs by value
        pairs.sort(Comparator.comparingInt(o -> o.value));
        
        // To keep track of visited elements
        boolean[] visited = new boolean[n];
        int swaps = 0;

        for (int i = 0; i < n; i++) {
            // If already visited or in the correct position
            if (visited[i] || pairs.get(i).index == i) {
                continue;
            }
            
            // Find the cycle size
            int cycleSize = 0;
            int j = i;
            while (!visited[j]) {
                visited[j] = true;
                j = pairs.get(j).index;
                cycleSize++;
            }
            
            // Add the swaps needed for the cycle
            if (cycleSize > 1) {
                swaps += (cycleSize - 1);
            }
        }

        return swaps;
    }

    // Helper class to store pairs of value and index
    static class Pair {
        int value, index;

        Pair(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }

}
"""
