# Brute force
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        for i in range(n-2):
            for j in range(i + 1, n- 1):
                for k in range(j+1, n):
                    if rating[i] > rating[j] > rating[k]:
                        count += 1
                    if rating[i] < rating[j] < rating[k]:
                        count += 1
        return count


# Method 2: Optimising to O(n^2)
# We need to count tripplets {arr[i] < arr[j] < arr[k]} and {arr[i] > arr[j] > arr[k]} where i<j<k.
# So, let's find for every j count of all i and k, so that it will follow either of above 2 conditons.

# For each soldier(j), count how many soldiers on the left and right have less and greater ratings.
# This soldier can form less[left] * greater[right] + greater[left] * less[right] teams.

# Time: O(n^2)

class Solution:
    def numTeams(self, arr: List[int]) -> int:
        count = 0
        length = len(arr)
        for j in range(length):
            left_smaller, left_larger, right_smaller, right_larger = 0, 0, 0, 0
            for i in range(j):
                if arr[i] < arr[j]:
                    left_smaller += 1
                elif arr[i] > arr[j]:
                    left_larger += 1
            for k in range(j + 1, length):
                if arr[j] < arr[k]:
                    right_larger += 1
                elif arr[j] > arr[k]:
                    right_smaller += 1
            count += left_smaller * right_larger + left_larger * right_smaller
        return count

# Later do in O(n*logn). Solution in sheet.

# java
"""
class Solution {
    public int numTeams(int[] arr) {
        int count = 0;
        int len = arr.length;
        for (int j = 0; j < len; j++) {
            int leftSmaller = 0, rightLarger = 0;
            int leftLarger = 0, rightSmaller = 0;
            for (int i = 0; i < j; i++) {
                if (arr[i] < arr[j]) {
                    leftSmaller++;
                } else if (arr[i] > arr[j]) {
                    leftLarger++;
                }
            }
            for (int k = j + 1; k < len; k++) {
                if (arr[j] < arr[k]) {
                    rightLarger++;
                } else if (arr[j] > arr[k]) {
                    rightSmaller++;
                }
            }
            count += leftSmaller * rightLarger + leftLarger * rightSmaller;
        }

        return count;
}
}
"""