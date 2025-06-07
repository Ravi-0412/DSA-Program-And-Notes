# Logic: for a sum_of_digit store the maximum and second maximum number.

# Time = space = O(n)

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def sumOfDigit(num):
            sum = 0
            while num:
                num, r = divmod(num, 10)
                sum += r
            return sum

        digitSum = {}
        for num in nums:
            sum = sumOfDigit(num)
            if sum in digitSum:
                first , second = digitSum[sum]
                if num > first:
                    second , first = first , num
                elif num > second:
                    second = num
                digitSum[sum] = [first, second]
            else:
                digitSum[sum] = [num, 0]

        ans = -1
        for key, values in digitSum.items():
            num1, num2 = values
            if num2 != 0:
                ans = max(ans, num1 + num2)
        return ans 


# Shorter way of writing above logic.
# Logic: Since we need maxSum so we can store only maxNo corresponding to a digitSum.
# No need to store the second_max_no . We can use current number to get the ans with already stored number.

# Just like Two sum. Just instead of 'num' as key, we will use 'sum_of_digit'.

# Time = space= O(n)

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def sumOfDigit(num):
            sum = 0
            while num:
                num, r = divmod(num, 10)
                sum += r
            return sum

        digitSum = {}  # [digit_sum : max_num]
        ans = -1
        for num in nums:
            sum = sumOfDigit(num)
            if sum in digitSum:
                ans = max(ans, digitSum[sum] + num)
                digitSum[sum] = max(digitSum[sum], num)
            else:
                digitSum[sum] = num
        return ans

# Note: When you have to find largest/smallest pair among all possible then apply the same above logic.

# Note vvi: Whenver you are asked to 'find pair' or 'count pairs' apply two sum logic.
# in case of 'pair count' store 'frequency' as value.

# Java Code 
"""
import java.util.HashMap;
import java.util.List;

class Solution {
    // Function to calculate the sum of digits of a number
    private int sumOfDigit(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }

    public int maximumSum(List<Integer> nums) {
        HashMap<Integer, int[]> digitSum = new HashMap<>(); // [digit_sum : max_num, second_max_num]
        int ans = -1;

        for (int num : nums) {
            int sum = sumOfDigit(num);
            if (digitSum.containsKey(sum)) {
                int[] pair = digitSum.get(sum);
                if (num > pair[0]) {
                    pair[1] = pair[0];
                    pair[0] = num;
                } else if (num > pair[1]) {
                    pair[1] = num;
                }
            } else {
                digitSum.put(sum, new int[]{num, 0});
            }
        }

        for (int[] values : digitSum.values()) {
            int num1 = values[0], num2 = values[1];
            if (num2 != 0) {
                ans = Math.max(ans, num1 + num2);
            }
        }
        return ans;
    }
}

// Optimized approach similar to two-sum logic
class Solution {
    private int sumOfDigit(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }

    public int maximumSum(List<Integer> nums) {
        HashMap<Integer, Integer> digitSum = new HashMap<>(); // [digit_sum : max_num]
        int ans = -1;

        for (int num : nums) {
            int sum = sumOfDigit(num);
            if (digitSum.containsKey(sum)) {
                ans = Math.max(ans, digitSum.get(sum) + num);
                digitSum.put(sum, Math.max(digitSum.get(sum), num));
            } else {
                digitSum.put(sum, num);
            }
        }
        return ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    // Function to calculate the sum of digits of a number
    int sumOfDigit(int num) {
        int sum = 0;
        while (num) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }

    int maximumSum(vector<int>& nums) {
        unordered_map<int, pair<int, int>> digitSum; // [digit_sum : max_num, second_max_num]
        int ans = -1;

        for (int num : nums) {
            int sum = sumOfDigit(num);
            if (digitSum.count(sum)) {
                auto& [first, second] = digitSum[sum];
                if (num > first) {
                    second = first;
                    first = num;
                } else if (num > second) {
                    second = num;
                }
            } else {
                digitSum[sum] = {num, 0};
            }
        }

        for (auto& [key, values] : digitSum) {
            int num1 = values.first, num2 = values.second;
            if (num2 != 0) {
                ans = max(ans, num1 + num2);
            }
        }
        return ans;
    }
};

// Optimized approach similar to two-sum logic
class Solution {
public:
    int sumOfDigit(int num) {
        int sum = 0;
        while (num) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }

    int maximumSum(vector<int>& nums) {
        unordered_map<int, int> digitSum; // [digit_sum : max_num]
        int ans = -1;

        for (int num : nums) {
            int sum = sumOfDigit(num);
            if (digitSum.count(sum)) {
                ans = max(ans, digitSum[sum] + num);
                digitSum[sum] = max(digitSum[sum], num);
            } else {
                digitSum[sum] = num;
            }
        }
        return ans;
    }
};
"""