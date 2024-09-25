# Problem description: A jump starts with an odd jump and alternates with an even jump until you get to the end of the line or you can no longer take a step.

# Logic: In the Problem the next jump position is decided on the basis of the parity of jump(Odd/Even):

# Odd Number Jump: Next Greater Smallest position.(ceiling value)
# Even Number Jump: Next Smaller Greatest position.(floor value)

# we can find 'Next Greater Smallest position' and 'nextSmalllerGreatest' and can store in separate arrays.
# See its code at bottom and logic.

# Note for finding the 'nextGreaterSmallest' and 'nextSmallerGreatest' on right.
# you will have to first sort the indices according to their values.
# Like for 'nextGreaterSmallest' , we will sort in ascending order because we want the greater ele to come right side first&&
# for 'nextSmallerGreatest' , we will sort in descending order order because we want the smaller ele to come right side first.

# After this we can use stack .


# Explanation for:  'nextGreaterSmallest':
# arr = [10,13,12,14,15]
# 1) sorting indices by values and storing in a list
# sorted_indices= sorted(range(n), key=lambda x: arr[x]) =  [0, 2, 1, 3, 4]
# 2) finding next_greater_smallest using stack:
# we will get ans = [2,3,3,4,-1]  # index on right for 'nextGreaterSmallest'.
# Now convert into array elements(actual value)
# final ans_value = [12, 14, 14, 15, -1]

# def nextElement(indices):
#     ans = [None] * n
#     stack = []
#     # directly targeting the value of arr 'indices' as it has index as value
#     for i in indices:
#         while stack and i > stack[-1]:
#             # means 'i' is right side of index 'stack[-1]' and since already sorted will get 
#             # nextGreaterSmallest' or nextSmalllestGreater  based on what 'indices is sorted'   
#             ans[stack.pop()] = i 
#             stack.append(i)  # the current index value can be ans for next coming
#         return ans

# Note: if we sort the indices based on decreasing order of values then same function we can use for finding ''nextSmallerGreatest'.

# Note vvi: Finally, When we have possible jump position for each index compute if we can reach to the end index by taking odd or even jump starting from any position.

# Therefore, the Recurrence Relation for odd and even jump position computation are as follows:

# dp[i].odd = dp[odd_jump_index[i]].even
# dp[i].even = dp[even_jump_index[i]].odd

# For each state, we are storing if it is possible to reach the end index of the array or not.
# Also, odd_jump_index refers Next Greater Smallest Element Index and even_jump_index refers Next Smaller Greatest Element index

# Time: O(n*logn), space= O(n)

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)

        def nextElement(indices):
            ans = [None] * n
            stack = []
            # directly targeting the value of arr 'indices' as it has index as value
            for i in indices:
                while stack and i > stack[-1]:
                    # means 'i' is right side of index 'stack[-1]' and since already sorted will get 
                    # nextGreaterSmallest' or nextSmalllestGreater  based on what 'indices is sorted'   
                    ans[stack.pop()] = i 
                stack.append(i)  # the current index value can be ans for next coming
            return ans


        # first getting the 'Next Greater Smallest position' for each index.
        # for this we will sort the indices based on ascending order of values at indices
        sorted_indexes_increasing = sorted(range(n), key=lambda x: arr[x])
        # This will return a list with indices as value in sorted order.
        # This will help in deciding where to next for odd step from any index.
        odd = nextElement(sorted_indexes_increasing)  # will store which index to move on next from index 'i' for odd jum.

        #Now  for ''nextSmalllerGreatest'   for each index.
        # for this we will sort the indices based on descending order of values at indices
        sorted_indexes_decreasing = sorted(range(n), key=lambda x: arr[x], reverse=True)
        # This will return a list with indices as value in sorted order(decreasing)
        # This will help in deciding where to next for even index from any index.
        even = nextElement(sorted_indexes_decreasing)  # will store which index to move on next from index 'i' for even jump.

        # Index 0, represents is it possible to reach last index if we take this index as our 'odd' step
        # Index 1, represents is it possible to reach last index if we take this index as our 'even' step
        dp = [[0, 0] for i in range(n)]
        dp[-1] = [1, 1]  # for last index it is possible for both 'odd' and 'even' jump.

        # go on checking from last 
        for i in range(n-2, -1, -1):
            # check if we can take odd jump from here
            if odd[i] is not None:   # if odd[i] not None: will give error , it only works if nothing is present but 'None' is there as default so checking like this.
                # if odd step is possible then now it will depend on even jump of index where we will land after odd jump.
                dp[i][0] = dp[odd[i]][1]  # take odd jump and check for even jump
            
            # check if we can take even jump from here
            if even[i] is not None:
                # if  even step is possible then now it will depend on odd jump of index where we will land after even jump.
                dp[i][1] = dp[even[i]][0]  # take even jump and check for odd jump

        # return the number of spots marked True in odd
        # we always start with an odd jump, so odd will
        # contain the number of valid jumps to reach the end
        return sum([i[0] for i in dp])
    
# Java
"""
import java.util.*;

public class Solution {
    public int oddEvenJumps(int[] arr) {
        int n = arr.length;
        int[] oddNext = nextElement(arr, true);  // Odd jumps: sorted in increasing order
        int[] evenNext = nextElement(arr, false); // Even jumps: sorted in decreasing order

        boolean[][] dp = new boolean[n][2];
        dp[n - 1][0] = dp[n - 1][1] = true;

        for (int i = n - 2; i >= 0; i--) {
            if (oddNext[i] != -1) dp[i][0] = dp[oddNext[i]][1];
            if (evenNext[i] != -1) dp[i][1] = dp[evenNext[i]][0];
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i][0]) count++;
        }
        return count;
    }

    private int[] nextElement(int[] arr, boolean increasing) {
        int n = arr.length;
        Integer[] indices = new Integer[n];
        for (int i = 0; i < n; i++) indices[i] = i;

        if (increasing) {
            Arrays.sort(indices, (a, b) -> arr[a] == arr[b] ? a - b : arr[a] - arr[b]);
        } else {
            Arrays.sort(indices, (a, b) -> arr[a] == arr[b] ? a - b : arr[b] - arr[a]);
        }

        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        Stack<Integer> stack = new Stack<>();
        for (int i : indices) {
            while (!stack.isEmpty() && i > stack.peek()) {
                ans[stack.pop()] = i;
            }
            stack.push(i);
        }

        return ans;
    }
}

"""


