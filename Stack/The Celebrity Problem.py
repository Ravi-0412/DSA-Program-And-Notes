# for each people check if he is celebrity or not.
# by comparing with other people.
# time: O(n^2)

def findCelebrity(n, knows):
    for i in range(n):
        isCelebrity= True    # initially 
        for j in range(n):
            if i==j:
                continue
            if knows(j, i)== False or knows(i, j)== True:
                isCelebrity= False
        if isCelebrity== True:
            return i
    return -1


# method 2:
# Note: very new concept and thought process. keep this concept into mind.
# Q: given 'n^2' relations(brute force one) find the ans in O(n).
# Algo:
# 1) put all 'n' people into stack.
# 2) pop two people and check which can't be the celebrity between two till len(stack)>=2.
# after comparing two we can surely say that one of them can't be celebrity.
# Put the people which can be celebrity in stack after comparing.
# By repeating this step, we will be left with only one people in stack.
# But surey we can't say that he will be the celebrity because we have not compared with many people.

# 3) for making sure whether the only left person in stack is celebrity or not.
# just check him with all people.
# if he is celebrity then return its id else return -1.

# Note: This method is based on like: if this happens then he can't be the ans and so on.

def findCelebrity(n, knows):
    stack= []
    for i in range(n):
        stack.append(i)
    while len(stack) >= 2:
        p1= stack.pop()
        p2= stack.pop()
        if knows(p2, p1): 
            # means p2 knows p1 -> p2 can't be celebrity but 'p1' can be celebrity so put 'p1' into stack
            stack.append(p1)
        else: 
            # means p2 doesn't knows p1 -> p1 can't be celebrity but 'p2' can be celebrity so put 'p2' into stack
            stack.append(p2)
    # now chekc the only person left in stack is celebrity or not.
    p= stack.pop()
    for i in range(n):
        if i==p:
            continue
        if knows(p, i) or not knows(i, p):   # then 'p' can't be celebrity
            return -1
    return p

# Method 2:
# Optimsied to O(1) space

def findCelebrity(n, knows):
    # Assume the first person is the potential celebrity
    candidate = 0
    
    for i in range(1, n):
        # If the current candidate knows 'i', then 'i' could be the celebrity
        if knows(candidate, i):
            candidate = i
        # Else, 'i' is not a celebrity, so keep the current candidate
    
    # Verify if the candidate is indeed a celebrity
    for i in range(n):
        if i == candidate:
            continue  # Skip the candidate
        
        # If the candidate knows someone or someone doesn't know the candidate, they can't be a celebrity
        if knows(candidate, i) or not knows(i, candidate):
            return -1  # No celebrity found
    
    return candidate 

# Java Code 
"""
//Method 1
class Solution {
    public int findCelebrity(int n, boolean[][] knowsMatrix) {
        for (int i = 0; i < n; i++) {
            boolean isCelebrity = true;

            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (!knowsMatrix[j][i] || knowsMatrix[i][j]) {
                    isCelebrity = false;
                    break;
                }
            }

            if (isCelebrity) return i;
        }
        return -1;
    }
}
//Method 2
import java.util.Stack;

class Solution {
    public int findCelebrity(int n, boolean[][] knowsMatrix) {
        Stack<Integer> stack = new Stack<>();

        // Push all people into the stack
        for (int i = 0; i < n; i++) {
            stack.push(i);
        }

        // Compare two people until only one is left in the stack
        while (stack.size() >= 2) {
            int p1 = stack.pop();
            int p2 = stack.pop();

            if (knowsMatrix[p2][p1]) {
                stack.push(p1); // p2 knows p1 -> p2 can't be celebrity, but p1 can be
            } else {
                stack.push(p2); // p2 does not know p1 -> p1 can't be celebrity, but p2 can be
            }
        }

        // Verify if the remaining person is the celebrity
        int candidate = stack.pop();

        for (int i = 0; i < n; i++) {
            if (i == candidate) continue;
            if (knowsMatrix[candidate][i] || !knowsMatrix[i][candidate]) {
                return -1; // Not a celebrity
            }
        }

        return candidate;
    }
}
//Method 3
class Solution {
    public int findCelebrity(int n, boolean[][] knowsMatrix) {
        int candidate = 0;

        // Find the potential celebrity
        for (int i = 1; i < n; i++) {
            if (knowsMatrix[candidate][i]) {
                candidate = i; // If candidate knows i, then candidate can't be a celebrity
            }
        }

        // Verify if the candidate is indeed a celebrity
        for (int i = 0; i < n; i++) {
            if (i == candidate) continue;
            if (knowsMatrix[candidate][i] || !knowsMatrix[i][candidate]) {
                return -1; // No celebrity found
            }
        }

        return candidate;
    }
}

"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>

using namespace std;

bool knows(int a, int b); // Assume this function is predefined

class Solution {
public:
    int findCelebrity(int n) {
        for (int i = 0; i < n; i++) {
            bool isCelebrity = true;

            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (!knows(j, i) || knows(i, j)) {
                    isCelebrity = false;
                    break;
                }
            }

            if (isCelebrity) return i;
        }
        return -1;
    }
};
//Method 2
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

bool knows(int a, int b); // Assume this function is predefined

class Solution {
public:
    int findCelebrity(int n) {
        stack<int> st;

        // Push all people into the stack
        for (int i = 0; i < n; i++) {
            st.push(i);
        }

        // Compare two people until only one is left in the stack
        while (st.size() >= 2) {
            int p1 = st.top(); st.pop();
            int p2 = st.top(); st.pop();

            if (knows(p2, p1)) {
                st.push(p1); // p2 knows p1 -> p2 can't be celebrity, but p1 can be
            } else {
                st.push(p2); // p2 does not know p1 -> p1 can't be celebrity, but p2 can be
            }
        }

        // Verify if the remaining person is the celebrity
        int candidate = st.top(); st.pop();

        for (int i = 0; i < n; i++) {
            if (i == candidate) continue;
            if (knows(candidate, i) || !knows(i, candidate)) {
                return -1; // Not a celebrity
            }
        }

        return candidate;
    }
};
//Method 3
#include <iostream>
#include <vector>

using namespace std;

bool knows(int a, int b); // Assume this function is predefined

class Solution {
public:
    int findCelebrity(int n) {
        int candidate = 0;

        // Find the potential celebrity
        for (int i = 1; i < n; i++) {
            if (knows(candidate, i)) {
                candidate = i; // If candidate knows i, then candidate can't be a celebrity
            }
        }

        // Verify if the candidate is indeed a celebrity
        for (int i = 0; i < n; i++) {
            if (i == candidate) continue;
            if (knows(candidate, i) || !knows(i, candidate)) {
                return -1; // No celebrity found
            }
        }

        return candidate;
    }
};
"""