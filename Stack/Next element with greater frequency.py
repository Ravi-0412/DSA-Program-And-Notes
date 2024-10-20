"""
Just same as find next greater element on right, just check the frequency here ,
Instead of checking the value.

So 1st find the freq of each element and store in hashmap,, after that this question reduces to 'Find next element on right'
having greater frequency.
"""


# Time = space = O(n)
from collections import defaultdict

class Solution:
    def print_next_greater_freq(self,arr,n):
        freq = defaultdict(int)
        for num in arr:
            freq[num] += 1
            
        ans = [-1]* n
        stack = []
        for i in range(n):
            while stack and freq[arr[stack[-1]]] < freq[arr[i]]:
                ans[stack.pop()] = arr[i]
            stack.append(i)
        return ans

# java
"""
class Solution {
    public int[] printNextGreaterFreq(int[] arr, int n) {
        // Step 1: Create a frequency map to store the count of each element
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : arr) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        // Step 2: Initialize the result array with -1 and a stack for indices
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        Stack<Integer> stack = new Stack<>();

        // Step 3: Traverse the array and use the stack to find the next greater frequency
        for (int i = 0; i < n; i++) {
            // While the stack is not empty and the frequency of the current element
            // is greater than the frequency of the element at the index stored at the top of the stack
            while (!stack.isEmpty() && freq.get(arr[stack.peek()]) < freq.get(arr[i])) {
                ans[stack.pop()] = arr[i];
            }
            // Push the current index to the stack
            stack.push(i);
        }

        // Step 4: Return the result array
        return ans;
    }
}
"""
