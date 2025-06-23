# method 1

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

# Java Code 
"""
public class Solution {
    // knows(a, b) is defined externally
    boolean knows(int a, int b);

    public int findCelebrity(int n) {
        for (int i = 0; i < n; i++) {
            boolean isCelebrity = true;  // initially
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (!knows(j, i) || knows(i, j)) {
                    isCelebrity = false;
                }
            }
            if (isCelebrity == true) {
                return i;
            }
        }
        return -1;
    }
}

"""

# C++ Code 
"""
// knows(a, b) is defined externally
bool knows(int a, int b);

class Solution {
public:
    int findCelebrity(int n) {
        for (int i = 0; i < n; i++) {
            bool isCelebrity = true;  // initially
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (!knows(j, i) || knows(i, j)) {
                    isCelebrity = false;
                }
            }
            if (isCelebrity == true) {
                return i;
            }
        }
        return -1;
    }
};

"""

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

# Java Code 
"""
import java.util.*;

public class Solution {
    // Assume this method is defined externally
    boolean knows(int a, int b);

    public int findCelebrity(int n) {
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            stack.push(i);
        }

        while (stack.size() >= 2) {
            int p1 = stack.pop();
            int p2 = stack.pop();

            if (knows(p2, p1)) {
                // means p2 knows p1 -> p2 can't be celebrity but 'p1' can be celebrity so put 'p1' into stack
                stack.push(p1);
            } else {
                // means p2 doesn't know p1 -> p1 can't be celebrity but 'p2' can be celebrity so put 'p2' into stack
                stack.push(p2);
            }
        }

        // now check the only person left in stack is celebrity or not.
        int p = stack.pop();
        for (int i = 0; i < n; i++) {
            if (i == p) continue;
            if (knows(p, i) || !knows(i, p)) {
                // then 'p' can't be celebrity
                return -1;
            }
        }
        return p;
    }
}

"""

# C++ Code 
"""
#include <stack>
using namespace std;

// Assume this function is defined externally
bool knows(int a, int b);

class Solution {
public:
    int findCelebrity(int n) {
        stack<int> stack;
        for (int i = 0; i < n; i++) {
            stack.push(i);
        }

        while (stack.size() >= 2) {
            int p1 = stack.top(); stack.pop();
            int p2 = stack.top(); stack.pop();

            if (knows(p2, p1)) {
                // means p2 knows p1 -> p2 can't be celebrity but 'p1' can be celebrity so put 'p1' into stack
                stack.push(p1);
            } else {
                // means p2 doesn't know p1 -> p1 can't be celebrity but 'p2' can be celebrity so put 'p2' into stack
                stack.push(p2);
            }
        }

        // now check the only person left in stack is celebrity or not.
        int p = stack.top(); stack.pop();
        for (int i = 0; i < n; i++) {
            if (i == p) continue;
            if (knows(p, i) || !knows(i, p)) {
                // then 'p' can't be celebrity
                return -1;
            }
        }
        return p;
    }
};

"""

# Method 3:
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
public class Solution {
    // Assume this method is defined externally
    boolean knows(int a, int b);

    public int findCelebrity(int n) {
        // Assume the first person is the potential celebrity
        int candidate = 0;

        for (int i = 1; i < n; i++) {
            // If the current candidate knows 'i', then 'i' could be the celebrity
            if (knows(candidate, i)) {
                candidate = i;
            }
            // Else, 'i' is not a celebrity, so keep the current candidate
        }

        // Verify if the candidate is indeed a celebrity
        for (int i = 0; i < n; i++) {
            if (i == candidate) continue;  // Skip the candidate

            // If the candidate knows someone or someone doesn't know the candidate, they can't be a celebrity
            if (knows(candidate, i) || !knows(i, candidate)) {
                return -1;  // No celebrity found
            }
        }

        return candidate;
    }
}

"""

# C++ Code 
"""
// Assume this function is defined externally
bool knows(int a, int b);

class Solution {
public:
    int findCelebrity(int n) {
        // Assume the first person is the potential celebrity
        int candidate = 0;

        for (int i = 1; i < n; i++) {
            // If the current candidate knows 'i', then 'i' could be the celebrity
            if (knows(candidate, i)) {
                candidate = i;
            }
            // Else, 'i' is not a celebrity, so keep the current candidate
        }

        // Verify if the candidate is indeed a celebrity
        for (int i = 0; i < n; i++) {
            if (i == candidate) continue;  // Skip the candidate

            // If the candidate knows someone or someone doesn't know the candidate, they can't be a celebrity
            if (knows(candidate, i) || !knows(i, candidate)) {
                return -1;  // No celebrity found
            }
        }

        return candidate;
    }
};

"""