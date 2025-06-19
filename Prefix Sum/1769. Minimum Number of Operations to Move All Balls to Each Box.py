# Method 1: 
# Brute force
# Time: O(n^2), space: O(n)

"""
Just find the distance of each from one on left and right for each index.
"""

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Get the total number of boxes
        n = len(boxes)
        # Initialize the answer array with zeros
        ans = [0] * n
        
        # Iterate over each box to calculate the number of operations required
        for i in range(n):
            # Initialize the count of operations required to move balls from the left
            leftCount = 0
            # Start checking boxes to the left of the current box
            j = i - 1
            while j >= 0:  # Continue until the first box
                if boxes[j] == '1':  # If a box contains a ball
                    # Add the distance between the current box and the box with the ball
                    leftCount += i - j
                j -= 1  # Move to the previous box
            
            # Initialize the count of operations required to move balls from the right
            rightCount = 0
            # Start checking boxes to the right of the current box
            k = i + 1
            while k < n:  # Continue until the last box
                if boxes[k] == '1':  # If a box contains a ball
                    # Add the distance between the current box and the box with the ball
                    rightCount += k - i
                k += 1  # Move to the next box
            
            # The total operations for the current box is the sum of left and right operations
            ans[i] = leftCount + rightCount
        
        # Return the result array with the minimum number of operations for each box
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public int[] minOperations(String boxes) {
        // Get the total number of boxes
        int n = boxes.length();
        // Initialize the answer array with zeros
        int[] ans = new int[n];

        // Iterate over each box to calculate the number of operations required
        for (int i = 0; i < n; i++) {
            // Initialize the count of operations required to move balls from the left
            int leftCount = 0;
            // Start checking boxes to the left of the current box
            int j = i - 1;
            while (j >= 0) {  // Continue until the first box
                if (boxes.charAt(j) == '1') {  // If a box contains a ball
                    // Add the distance between the current box and the box with the ball
                    leftCount += i - j;
                }
                j--;  // Move to the previous box
            }

            // Initialize the count of operations required to move balls from the right
            int rightCount = 0;
            // Start checking boxes to the right of the current box
            int k = i + 1;
            while (k < n) {  // Continue until the last box
                if (boxes.charAt(k) == '1') {  // If a box contains a ball
                    // Add the distance between the current box and the box with the ball
                    rightCount += k - i;
                }
                k++;  // Move to the next box
            }

            // The total operations for the current box is the sum of left and right operations
            ans[i] = leftCount + rightCount;
        }

        // Return the result array with the minimum number of operations for each box
        return ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<int> minOperations(string boxes) {
        // Get the total number of boxes
        int n = boxes.length();
        // Initialize the answer array with zeros
        vector<int> ans(n, 0);

        // Iterate over each box to calculate the number of operations required
        for (int i = 0; i < n; i++) {
            // Initialize the count of operations required to move balls from the left
            int leftCount = 0;
            // Start checking boxes to the left of the current box
            int j = i - 1;
            while (j >= 0) {  // Continue until the first box
                if (boxes[j] == '1') {  // If a box contains a ball
                    // Add the distance between the current box and the box with the ball
                    leftCount += i - j;
                }
                j--;  // Move to the previous box
            }

            // Initialize the count of operations required to move balls from the right
            int rightCount = 0;
            // Start checking boxes to the right of the current box
            int k = i + 1;
            while (k < n) {  // Continue until the last box
                if (boxes[k] == '1') {  // If a box contains a ball
                    // Add the distance between the current box and the box with the ball
                    rightCount += k - i;
                }
                k++;  // Move to the next box
            }

            // The total operations for the current box is the sum of left and right operations
            ans[i] = leftCount + rightCount;
        }

        // Return the result array with the minimum number of operations for each box
        return ans;
    }
};
"""

# Methoid 2: 
# short version of Method 1

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        for i in range(n):
            for j in range(n):
                if boxes[j] == '1':
                    ans[i] += abs(j-i)
        return ans

# Java Code 
"""
class Solution {
    public int[] minOperations(String boxes) {
        int n = boxes.length();
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (boxes.charAt(j) == '1') {
                    ans[i] += Math.abs(j - i);
                }
            }
        }

        return ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <string>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        vector<int> ans(n, 0);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (boxes[j] == '1') {
                    ans[i] += abs(j - i);
                }
            }
        }

        return ans;
    }
};
"""

# Method 3: 
# Optimised to O(n)
"""
DP Left to Right and Right To Left

Let leftDist[i] is the total distance after moving all the ball from the left side to ith box.
Let leftBallCnt is the number of balls after moving all the ball from the left side to ith box so far.
To calculate leftDist[i], we need to move leftBallCnt balls from (i-1)th box by one, so total distance:
leftDist[i] = leftDist[i-1] + leftBallCnt
Do the same with rightDist[i] and rightBallCnt in the right side.
To calculate total distance after moving all the ball from the left and the right side to ith box:
ans[i] = leftDist[i] + rightDist[i]
"""

class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)

        leftDist = [0] * n
        leftBallCnt = int(boxes[0])
        for i in range(1, n):
            leftDist[i] = leftDist[i - 1] + leftBallCnt
            leftBallCnt = leftBallCnt + int(boxes[i])

        rightDist = [0] * n
        rightBallCnt = int(boxes[n - 1])
        for i in range(n - 2, -1, -1):
            rightDist[i] = rightDist[i + 1] + rightBallCnt
            rightBallCnt = rightBallCnt + int(boxes[i])

        ans = [0] * n
        for i in range(n):
            ans[i] = leftDist[i] + rightDist[i]
        return ans

# Java Code 
"""
class Solution {
    public int[] minOperations(String boxes) {
        int n = boxes.length();

        int[] leftDist = new int[n];
        int leftBallCnt = boxes.charAt(0) - '0';

        for (int i = 1; i < n; i++) {
            leftDist[i] = leftDist[i - 1] + leftBallCnt;
            leftBallCnt += boxes.charAt(i) - '0';
        }

        int[] rightDist = new int[n];
        int rightBallCnt = boxes.charAt(n - 1) - '0';

        for (int i = n - 2; i >= 0; i--) {
            rightDist[i] = rightDist[i + 1] + rightBallCnt;
            rightBallCnt += boxes.charAt(i) - '0';
        }

        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = leftDist[i] + rightDist[i];
        }

        return ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();

        vector<int> leftDist(n, 0);
        int leftBallCnt = boxes[0] - '0';

        for (int i = 1; i < n; i++) {
            leftDist[i] = leftDist[i - 1] + leftBallCnt;
            leftBallCnt += boxes[i] - '0';
        }

        vector<int> rightDist(n, 0);
        int rightBallCnt = boxes[n - 1] - '0';

        for (int i = n - 2; i >= 0; i--) {
            rightDist[i] = rightDist[i + 1] + rightBallCnt;
            rightBallCnt += boxes[i] - '0';
        }

        vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            ans[i] = leftDist[i] + rightDist[i];
        }

        return ans;
    }
};
"""