# Method 1:
"""
Logic: The target will not be found if it is removed from the sequence.
When does this occur? Think about this.

For a target value to be found in every possible search scenario:

1)  Left Condition: All elements to the left of the target must be less than the target. 
If any element to the left is greater than the target, there exists a pivot choice (that greater element)
which would remove the target from the sequence before it can be found.

2) Right Condition: All elements to the right of the target must be greater than the target. 
If any element to the right is less than the target, there exists a pivot choice (that lesser element)
which would remove the target from the sequence before it can be found.

# Time = space = O(n)
"""
class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        left_max = [float('-inf')] * n
        right_min = [float('inf')] * n
        
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], nums[i])
        
        right_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], nums[i])
        
        count = 0
        for i in range(n):
            if (i == 0 or nums[i] >= left_max[i-1]) and (i == n-1 or nums[i] <= right_min[i+1]):
                count += 1
        
        return count

# Method 2: In One pass only
"""
1) The stack is used to keep track of potential binary searchable numbers as we iterate through the array.
2) For each element in the array, we ensure that all elements in the stack are less than or equal to the current element. 
If an element in the stack is greater than the current element, it is popped from the stack because 
it cannot be a binary searchable number (since there's a smaller element to its right).
3) We maintain a variable max to keep track of the maximum value encountered so far.
This helps in ensuring that only elements greater than all previous elements are pushed onto the stack, 
which is a necessary condition for a number to be binary searchable.
"""

def binarySearchableNumbers(self, nums: List[int]) -> int:
    stack = []
    max_so_far = float('-inf')
    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        if num > max_so_far:
            stack.append(num)
        max_so_far = max(max_so_far, num)
    return len(stack)

# in java
"""
import java.util.Stack;

class Solution {
    public int binarySearchableNumbers(int[] nums) {
        Stack<Integer> stack = new Stack<>();
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            while (!stack.isEmpty() && stack.peek() > num) {
                stack.pop();
            }
            if (num > max) {
                stack.push(num);
            }
            max = Math.max(max, num);
        }
        return stack.size();
    }
}
"""
