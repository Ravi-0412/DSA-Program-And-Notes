# Logic: Just same logic as "1047. Remove All Adjacent Duplicates In String".
# only diff: Here we can only remove if no of same element including current char is >= k.
# for this add the count of same char also with character in stack.

# 1) when you see any char check if top of stack has same char,:
# a) if same then:
# a.1) increment the count of top of stack by '1'.
# a.2) After incr check if count == k .
# a.2.1) if == k then pop 
# b) else append current char with number = 1.

# Time = space = O(n)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []  # [[char, count]]
        for i in range(n):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
                if stack[-1][1] == k :
                    stack.pop()
            else:
                stack.append([s[i], 1])
        ans = ""
        for i in range(len(stack)):
            ans += stack[i][0] * stack[i][1]          
        return ans
    
# java
"""
import java.util.Stack;

class Solution {
    public String removeDuplicates(String s, int k) {
        Stack<int[]> stack = new Stack<>();  // Stack to store characters and their counts

        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek()[0] == c) {
                stack.peek()[1]++;
                if (stack.peek()[1] == k) {
                    stack.pop();
                }
            } else {
                stack.push(new int[]{c, 1});    // c is converted to its ASCII value
                // if c is 'a', its ASCII value is 97. So, new int[]{'a', 1} becomes new int[]{97, 1}
            }
        }

        StringBuilder result = new StringBuilder();
        while (!stack.isEmpty()) {
            int[] top = stack.pop();
            for (int i = 0; i < top[1]; i++) {
                result.append((char) top[0]);     // Convert ASCII value back to character
            }
        }

        return result.reverse().toString();
    }
}


// using pair class instead of inserting array in 'stack'
import java.util.Stack;

class Solution {
    public String removeDuplicates(String s, int k) {
        int n = s.length();
        Stack<Pair> stack = new Stack<>();  // Stack to store characters and their counts

        for (int i = 0; i < n; i++) {
            if (!stack.isEmpty() && stack.peek().ch == s.charAt(i)) {
                stack.peek().count += 1;
                if (stack.peek().count == k) {
                    stack.pop();
                }
            } else {
                stack.push(new Pair(s.charAt(i), 1));
            }
        }

        StringBuilder ans = new StringBuilder();
        while (!stack.isEmpty()) {
            Pair p = stack.pop();
            for (int j = 0; j < p.count; j++) {
                ans.append(p.ch);
            }
        }
        
        return ans.reverse().toString();
    }

    class Pair {
        char ch;
        int count;
        
        Pair(char ch, int count) {
            this.ch = ch;
            this.count = count;
        }
    }
}

"""


# Follow up question:
"""
Q) Remove adjacent character having length >= k.
-> It is tricky because you cannot immediately pop the stack when the count hits k. 
You have to wait until the character changes to see if the total consecutive length ended up being k or more.
Link: https://leetcode.com/discuss/interview-question/625140/goldman-sachs-oa-2020-array-burst-problem-birthday-party

Mine logic below and mistake:
-> The main issue in mine current code is that you are only checking the "future" (i + 1). 
If you pop a group, the new top of the stack might now match the next character in the string, 
or it might match a group that was already there, potentially creating a new sequence of length >= K.

See correct code below
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []  # [[char, count]]
        for i in range(n):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
                if stack[-1][1] >= k :
                    if (i + 1 < n and s[i] != s[i+ 1]) or i == n - 1:
                        stack.pop()
            else:
                stack.append([s[i], 1])
        
        ans = ""
        for i in range(len(stack)):
            ans += stack[i][0] * stack[i][1]          
        return ans
        
obj = Solution()
# s = "abbccccdd"
# k = 3

# s = "abbcccdeaffff"
# k = 3

# s = "aabcddeeedccbaa"
# k =3

s= "abcccdee"
k = 3
print("String after removal is: ", obj.removeDuplicates(s, k))


# Correct code for follow ups:
"""
The Logic Thought Process:
1. Delayed Deletion: We use a stack to store [character, count]. Instead of popping as soon as count == k, we wait until we encounter a different character.
2. The "Check and Pop" Trigger: When s[i] is different from stack[-1], we check: "Was the group we just finished >= K?" If yes, pop it.
3. Recursive Merging: This is the most important part. After popping a group, the "new" top of the stack might be the same as the current character s[i]. 
We must merge them and check the count again.Final Cleanup: After the loop ends, the very last group in the stack needs a final check to see if it qualifies for removal.
4. Final Cleanup: After the loop ends, the very last group in the stack needs a final check to see if it qualifies for removal.

Time = space = O(N)
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack stores [char, count]
        stack = []
        
        for char in s:
            # If stack is not empty and current char matches the top of the stack
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                # Before adding a NEW character, check if the previous 
                # group completed a sequence of length >= k
                if stack and stack[-1][1] >= k:
                    stack.pop()
                    
                    # CRITICAL: After popping, the current 'char' might match 
                    # the NEW top of the stack. We must handle this "merge".
                    if stack and stack[-1][0] == char:
                        stack[-1][1] += 1
                    else:
                        stack.append([char, 1])
                else:
                    # Previous group was < k, so just add the new char
                    stack.append([char, 1])
        
        # Final check: The last group processed in the loop might be >= k
        if stack and stack[-1][1] >= k:
            stack.pop()
            
        # Reconstruct the string
        return "".join(char * count for char, count in stack)
