# 1st q: Next greater right
# Q: in case of no greater put '-1'.

# Logic: We need to check the element on right side for ans
# So we will start from right side only.

def nextLargerElement(arr,n):
    stack= [] # will store the all the larger ele till index 'i'
    ans= []
    for i in range(n-1,-1,-1):
        # Remove all element <= nums[i]
        while(stack and stack[-1] <= arr[i]):
                stack.pop()
        if stack:
            # Means we have found the ans for nums[i] and ans = top of stack
            ans.append(stack[-1])
        else:
            # Means i == n- 1 or nums[i] is the largest ele.
            ans.append(-1)
        stack.append(arr[i])  # arr[i] can be also the next greter ele for coming ele

    # now print the ans in reverse to get the ans
    for i in range(n-1,-1,-1):
        print(ans[i], end=" ")

arr= [0,1,8,3,2,4,6,7]
# nextLargerElement(arr,8)

# Java Code 
"""
import java.util.*;

public class Solution {
    public static void nextLargerElement(int[] arr, int n) {
        Stack<Integer> stack = new Stack<>(); // will store the all the larger ele till index 'i'
        ArrayList<Integer> ans = new ArrayList<>();

        for (int i = n - 1; i >= 0; i--) {
            // Remove all element <= arr[i]
            while (!stack.isEmpty() && stack.peek() <= arr[i]) {
                stack.pop();
            }

            if (!stack.isEmpty()) {
                // Means we have found the ans for arr[i] and ans = top of stack
                ans.add(stack.peek());
            } else {
                // Means i == n-1 or arr[i] is the largest ele.
                ans.add(-1);
            }

            stack.push(arr[i]);  // arr[i] can be also the next greater ele for coming ele
        }

        // now print the ans in reverse to get the ans
        for (int i = n - 1; i >= 0; i--) {
            System.out.print(ans.get(i) + " ");
        }
    }

    public static void main(String[] args) {
        int[] arr = {0, 1, 8, 3, 2, 4, 6, 7};
        nextLargerElement(arr, arr.length);
    }
}

"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

void nextLargerElement(vector<int>& arr, int n) {
    stack<int> st; // will store the all the larger ele till index 'i'
    vector<int> ans;

    for (int i = n - 1; i >= 0; i--) {
        // Remove all element <= arr[i]
        while (!st.empty() && st.top() <= arr[i]) {
            st.pop();
        }

        if (!st.empty()) {
            // Means we have found the ans for arr[i] and ans = top of stack
            ans.push_back(st.top());
        } else {
            // Means i == n-1 or arr[i] is the largest ele.
            ans.push_back(-1);
        }

        st.push(arr[i]);  // arr[i] can be also the next greater ele for coming ele
    }

    // now print the ans in reverse to get the ans
    for (int i = n - 1; i >= 0; i--) {
        cout << ans[i] << " ";
    }
}

int main() {
    vector<int> arr = {0, 1, 8, 3, 2, 4, 6, 7};
    nextLargerElement(arr, arr.size());
    return 0;
}

"""

# 2nd Question:  next greater left
# just same as next greater right

# Note vvi: All variations are same only just change the direction of 'for' loop and 
# condition of 'while' loop according to the question.

# Logic: We need to check the element on left side for ans
# So we will start from left side only.

def nextGreaterLeft(arr):
    stack= []
    ans= []
    for i in range(len(arr)):
        # Remove all element <= nums[i]
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    return ans
# arr= [0,1,8,3,2,4,6,7]
arr= [100, 80, 60, 70, 60, 75, 85]
print(nextGreaterLeft(arr))

# Java Code 
"""
import java.util.*;

public class Solution {
    public static List<Integer> nextGreaterLeft(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            // Remove all element <= arr[i]
            while (!stack.isEmpty() && stack.peek() <= arr[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                ans.add(stack.peek());
            } else {
                ans.add(-1);
            }
            stack.push(arr[i]);
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] arr = {100, 80, 60, 70, 60, 75, 85};
        List<Integer> result = nextGreaterLeft(arr);
        System.out.println(result);
    }
}

"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<int> nextGreaterLeft(vector<int>& arr) {
    stack<int> st;
    vector<int> ans;

    for (int i = 0; i < arr.size(); i++) {
        // Remove all element <= arr[i]
        while (!st.empty() && st.top() <= arr[i]) {
            st.pop();
        }
        if (!st.empty()) {
            ans.push_back(st.top());
        } else {
            ans.push_back(-1);
        }
        st.push(arr[i]);
    }
    return ans;
}

int main() {
    vector<int> arr = {100, 80, 60, 70, 60, 75, 85};
    vector<int> res = nextGreaterLeft(arr);
    for (int val : res) {
        cout << val << " ";
    }
    cout << endl;
    return 0;
}

"""

# 3rd: Next smaller left program

def nextSmallerLeft(arr):
    stack= []
    ans= []
    for i in range(len(arr)):
        # Remove all element >= nums[i]
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    return ans
arr= [2,5,8,3,2,4,1,7]
# print(nextSmallerLeft(arr))


# other way:
# Traverse right to left.
# Here will store ans as index not actual value.

# next_smaller_left = [-1]*n
# stack2 = []
# for i in range(n-1, -1, -1):
#     # 'i' will be ans for all the elements in stack till top of stack is > a[i].
#     while stack2 and a[stack2[-1]] > a[i]:
#         ind = stack2.pop()
#         next_smaller_left[ind] = i
#     stack2.append(i)

# Java Code 
"""
import java.util.*;

public class Solution {

    public static List<Integer> nextSmallerLeft(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            // Remove all element >= nums[i]
            while (!stack.isEmpty() && stack.peek() >= arr[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                ans.add(stack.peek());
            } else {
                ans.add(-1);
            }
            stack.push(arr[i]);
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] arr = {2, 5, 8, 3, 2, 4, 1, 7};
        List<Integer> result = nextSmallerLeft(arr);
        System.out.println(result);
    }

    /*
     other way:
     Traverse right to left.
     Here will store ans as index not actual value.

    // int[] next_smaller_left = new int[n];
    // Arrays.fill(next_smaller_left, -1);
    // Stack<Integer> stack2 = new Stack<>();
    // for (int i = n - 1; i >= 0; i--) {
    //     // 'i' will be ans for all the elements in stack till top of stack is > a[i].
    //     while (!stack2.isEmpty() && a[stack2.peek()] > a[i]) {
    //         int ind = stack2.pop();
    //         next_smaller_left[ind] = i;
    //     }
    //     stack2.push(i);
    // }
    */
}

"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<int> nextSmallerLeft(const vector<int>& arr) {
    stack<int> stack;
    vector<int> ans;
    for (int i = 0; i < arr.size(); i++) {
        // Remove all element >= nums[i]
        while (!stack.empty() && stack.top() >= arr[i]) {
            stack.pop();
        }
        if (!stack.empty()) {
            ans.push_back(stack.top());
        } else {
            ans.push_back(-1);
        }
        stack.push(arr[i]);
    }
    return ans;
}

int main() {
    vector<int> arr = {2, 5, 8, 3, 2, 4, 1, 7};
    vector<int> result = nextSmallerLeft(arr);
    for (int val : result) cout << val << " ";
    cout << endl;

    /*
     other way:
     Traverse right to left.
     Here will store ans as index not actual value.

    // vector<int> next_smaller_left(n, -1);
    // stack<int> stack2;
    // for (int i = n - 1; i >= 0; i--) {
    //     // 'i' will be ans for all the elements in stack till top of stack is > a[i].
    //     while (!stack2.empty() && a[stack2.top()] > a[i]) {
    //         int ind = stack2.top();
    //         stack2.pop();
    //         next_smaller_left[ind] = i;
    //     }
    //     stack2.push(i);
    // }
    */
}
"""

# 4th Question: Next smaller right program
def nextSmallerRight(arr):
    stack= []
    ans= []
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if stack :
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    result= ans[::-1]
    return result
arr= [2,5,8,3,2,4,1,7]
# print(nextSmallerRight(arr))


# other way:
# traverse left to right
# Here will store index as ans not actual value.

# Same logic as method 3rd.

# next_smaller_right = [-1] * n
# stack1 = []
# for i in range(n):
#     while stack1 and a[stack1[-1]] > a[i]:
#         ind = stack1.pop()
#         next_smaller_right[ind] = i
#     stack1.append(i)

# Java Code 
"""
import java.util.*;

public class Solution {

    public static List<Integer> nextSmallerRight(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();

        for (int i = arr.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() >= arr[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                ans.add(stack.peek());
            } else {
                ans.add(-1);
            }
            stack.push(arr[i]);
        }

        Collections.reverse(ans);
        return ans;
    }

    public static void main(String[] args) {
        int[] arr = {2, 5, 8, 3, 2, 4, 1, 7};
        List<Integer> result = nextSmallerRight(arr);
        System.out.println(result);
    }

    /*
     other way:
     traverse left to right
     Here will store index as ans not actual value.

     Same logic as method 3rd.

    // int[] next_smaller_right = new int[n];
    // Arrays.fill(next_smaller_right, -1);
    // Stack<Integer> stack1 = new Stack<>();
    // for (int i = 0; i < n; i++) {
    //     while (!stack1.isEmpty() && a[stack1.peek()] > a[i]) {
    //         int ind = stack1.pop();
    //         next_smaller_right[ind] = i;
    //     }
    //     stack1.push(i);
    // }
    */
}

"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

vector<int> nextSmallerRight(vector<int>& arr) {
    stack<int> stack;
    vector<int> ans;

    for (int i = arr.size() - 1; i >= 0; i--) {
        while (!stack.empty() && stack.top() >= arr[i]) {
            stack.pop();
        }
        if (!stack.empty()) {
            ans.push_back(stack.top());
        } else {
            ans.push_back(-1);
        }
        stack.push(arr[i]);
    }

    reverse(ans.begin(), ans.end());
    return ans;
}

int main() {
    vector<int> arr = {2, 5, 8, 3, 2, 4, 1, 7};
    vector<int> result = nextSmallerRight(arr);
    for (int val : result) cout << val << " ";
    cout << endl;

    /*
     other way:
     traverse left to right
     Here will store index as ans not actual value.

     Same logic as method 3rd.

    // vector<int> next_smaller_right(n, -1);
    // stack<int> stack1;
    // for (int i = 0; i < n; i++) {
    //     while (!stack1.empty() && a[stack1.top()] > a[i]) {
    //         int ind = stack1.top();
    //         stack1.pop();
    //         next_smaller_right[ind] = i;
    //     }
    //     stack1.push(i);
    // }
    */
}

"""


# Extension : 
# Questions that based on these:
# 1) 496. Next Greater Element I
# 2) 503. Next Greater Element II
# 3) 739. Daily Temperatures 
# 4) 901. Online Stock Span
