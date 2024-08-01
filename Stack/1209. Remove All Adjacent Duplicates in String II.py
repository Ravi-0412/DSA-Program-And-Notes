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
# Remove adjacent character having length >= k.

# Link: https://leetcode.com/discuss/interview-question/625140/goldman-sachs-oa-2020-array-burst-problem-birthday-party

# Note: Got this question in Goldman OA and i solved using this method.
# 7 out of 8 test case was passing but don't know why this one is not working.
# Correct c++ code below which is working fully. Have to understand that properly.

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

# c++ code 
"""
vector<string> getShrunkArray(vector<string> &v, int k) {

    vector<string> shrunkArray;
    int n = v.size();
    stack<pair<string,int> > s;
    for(int i=0;i<n;i++) {
        string curr = v[i];
        if(!s.empty()) {
            if(s.top().first == curr) {
                s.top().second += 1;
            } else {
                if(s.top().second >= k) {
                    s.pop();
                    i--;
                } else {
                    s.push({curr, 1});
                }
            }
        } else {
            s.push({curr, 1});
        }
    }

    if(!s.empty() && s.top().second >= k) {
        s.pop();
    }

    while (!s.empty()) {
        pair<string, int> p = s.top();
        s.pop();
        for(int i=0;i<p.second;i++) {
            shrunkArray.push_back(p.first);
        }
    }

    reverse(shrunkArray.begin(), shrunkArray.end());
    return shrunkArray;
}

"""