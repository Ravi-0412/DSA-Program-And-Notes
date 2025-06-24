# Method 1:
# Find the ways and then call function to evaluate infix expression i.e 
# "227. Basic Calculator II".

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []

        def calculate(s):
            stack= []
            num, lastOperator= 0, "+"
            for c in s:
                if c== ' ':
                    continue
                if c.isdigit():  # for more than one digit number
                    num= num*10 + int(c)
                else:
                    if lastOperator== "+" :
                        stack.append(num)
                    elif lastOperator== "-" :
                        stack.append(-1* num)
                    elif lastOperator== "*" :
                        temp= stack.pop()
                        stack.append(temp * num)
                    num, lastOperator= 0, c
            # doing the operation for last operator as it will be left to operate.
            if lastOperator== "+" :
                stack.append(num)
            elif lastOperator== "-" :
                stack.append(-1* num)
            elif lastOperator== "*" :
                temp= stack.pop()
                stack.append(temp * num)
            return sum(stack)

        def backtrack(num, ways):
            if not num:
                # print(ways)
                if calculate(ways) == target:
                    ans.append(ways)
                return
            for i in range(1, len(num) + 1):
                s = num[: i]
                if len(s) > 1 and s[0] == "0":
                    # to handle addition of '05' , '0005' etc. 
                    # i.e handling leading zero
                    # continue
                    break   # in this you can't get possible way considering same remaining num.
                if num[i : ] != "":
                    backtrack(num[i: ], ways + s + "+")
                    backtrack(num[i: ], ways + s + "-" )
                    backtrack(num[i: ], ways + s +  "*")
                else:
                    backtrack(num[i: ], ways + s )
        
        backtrack(num, "")
        return ans

# Java Code 
"""
import java.util.*;

public class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> ans = new ArrayList<>();

        backtrack(num, "", target, ans);  // backtrack(num, ways)
        return ans;
    }

    private void backtrack(String num, String ways, int target, List<String> ans) {
        if (num.isEmpty()) {
            // print(ways)
            if (calculate(ways) == target) {
                ans.add(ways);
            }
            return;
        }

        for (int i = 1; i <= num.length(); i++) {
            String s = num.substring(0, i);
            if (s.length() > 1 && s.charAt(0) == '0') {
                // to handle addition of '05' , '0005' etc. 
                // i.e handling leading zero
                // continue
                break;   // in this you can't get possible way considering same remaining num.
            }

            if (i < num.length()) {
                backtrack(num.substring(i), ways + s + "+", target, ans);
                backtrack(num.substring(i), ways + s + "-", target, ans);
                backtrack(num.substring(i), ways + s + "*", target, ans);
            } else {
                backtrack(num.substring(i), ways + s, target, ans);
            }
        }
    }

    private int calculate(String s) {
        Stack<Integer> stack = new Stack<>();
        int num = 0;
        char lastOperator = '+';
        for (char c : s.toCharArray()) {
            if (c == ' ') continue;
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');  // for more than one digit number
            } else {
                if (lastOperator == '+') {
                    stack.push(num);
                } else if (lastOperator == '-') {
                    stack.push(-1 * num);
                } else if (lastOperator == '*') {
                    int temp = stack.pop();
                    stack.push(temp * num);
                }
                num = 0;
                lastOperator = c;
            }
        }

        // doing the operation for last operator as it will be left to operate.
        if (lastOperator == '+') {
            stack.push(num);
        } else if (lastOperator == '-') {
            stack.push(-1 * num);
        } else if (lastOperator == '*') {
            int temp = stack.pop();
            stack.push(temp * num);
        }

        int sum = 0;
        for (int val : stack) sum += val;
        return sum;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> ans;
        backtrack(num, "", target, ans);  // backtrack(num, ways)
        return ans;
    }

private:
    void backtrack(string num, string ways, int target, vector<string>& ans) {
        if (num.empty()) {
            // print(ways)
            if (calculate(ways) == target) {
                ans.push_back(ways);
            }
            return;
        }

        for (int i = 1; i <= num.length(); ++i) {
            string s = num.substr(0, i);
            if (s.length() > 1 && s[0] == '0') {
                // to handle addition of '05' , '0005' etc. 
                // i.e handling leading zero
                // continue
                break;   // in this you can't get possible way considering same remaining num.
            }

            string rem = num.substr(i);
            if (!rem.empty()) {
                backtrack(rem, ways + s + "+", target, ans);
                backtrack(rem, ways + s + "-", target, ans);
                backtrack(rem, ways + s + "*", target, ans);
            } else {
                backtrack(rem, ways + s, target, ans);
            }
        }
    }

    int calculate(const string& s) {
        stack<int> stack;
        int num = 0;
        char lastOperator = '+';
        for (char c : s) {
            if (c == ' ') continue;
            if (isdigit(c)) {
                num = num * 10 + (c - '0');  // for more than one digit number
            } else {
                if (lastOperator == '+') {
                    stack.push(num);
                } else if (lastOperator == '-') {
                    stack.push(-1 * num);
                } else if (lastOperator == '*') {
                    int temp = stack.top(); stack.pop();
                    stack.push(temp * num);
                }
                num = 0;
                lastOperator = c;
            }
        }

        // doing the operation for last operator as it will be left to operate.
        if (lastOperator == '+') {
            stack.push(num);
        } else if (lastOperator == '-') {
            stack.push(-1 * num);
        } else if (lastOperator == '*') {
            int temp = stack.top(); stack.pop();
            stack.push(temp * num);
        }

        int sum = 0;
        while (!stack.empty()) {
            sum += stack.top();
            stack.pop();
        }
        return sum;
    }
};
"""

# Method 2:
# evaluating expression within same function taking more parameters.

# Explanation:
# We use backtracking to generate all possible expressions by adding +, -, * to between the digits of s string.
# There is no priority since there are no parentheses ( and ) in our s string, so we can evaluate the expression on the fly to save time.

# There are total 3 operators:
# a) + operator: newResult = resSoFar + num
# b)  - operator: newResult = resSoFar - num.
# c) * operator: We need to keep the prevNum so that to calculate newResult we need to minus prevNum then
# plus with prevNum * num. So newResult = resSoFar - prevNum + prevNum * num.

# more about '*':
# Consider 1 + 2 * 4 and in the call where we are currently evaluating 1 + 2.
# path = "1 + 2"
# cur = 3
# prev = 2 (got newly added from the previous backtrack call)

# in the for loop
# now = 4 , to the operand "*" -> we'll get the correct result 9 if we do
# curr - prev + prev * now  i.e 3 - 2 + 2 * 4 = 9

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []

        def backtrack(i, ways, resultSoFar, prevNo):
            if i == len(num):
                if resultSoFar == target:
                    ans.append(ways)
                return
            for j in range(i + 1, len(num) + 1):
                s = num[i : j]
                if len(s) > 1 and num[i] == "0":
                    break
                number = int(s)
                if i == 0:
                    # First ele so pick it without any operator
                    backtrack(j, ways + s , resultSoFar + number , number)
                else: 
                    backtrack(j, ways + "+" + s, resultSoFar + number, number)
                    backtrack(j, ways + "-" + s, resultSoFar - number, -number)  # with sign we need to evaluate when we will see '*' next.
                    backtrack(j, ways + "*" + s,  resultSoFar -prevNo + prevNo * number , prevNo * number) 

        backtrack(0, "", 0, 0)
        return ans

# Java Code 
"""
import java.util.*;

public class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> ans = new ArrayList<>();

        backtrack(num, target, 0, "", 0, 0, ans);
        return ans;
    }

    void backtrack(String num, int target, int i, String ways, long resultSoFar, long prevNo, List<String> ans) {
        if (i == num.length()) {
            if (resultSoFar == target) {
                ans.add(ways);
            }
            return;
        }

        for (int j = i + 1; j <= num.length(); j++) {
            String s = num.substring(i, j);
            if (s.length() > 1 && num.charAt(i) == '0') {
                break;  // to handle addition of '05', '0005' etc.
                        // i.e handling leading zero
                        // in this you can't get possible way considering same remaining num.
            }

            long number = Long.parseLong(s);

            if (i == 0) {
                // First ele so pick it without any operator
                backtrack(num, target, j, ways + s, number, number, ans);
            } else {
                backtrack(num, target, j, ways + "+" + s, resultSoFar + number, number, ans);
                backtrack(num, target, j, ways + "-" + s, resultSoFar - number, -number, ans);
                backtrack(num, target, j, ways + "*" + s, resultSoFar - prevNo + prevNo * number, prevNo * number, ans); 
                // with sign we need to evaluate when we will see '*' next.
            }
        }
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> ans;
        backtrack(num, target, 0, "", 0, 0, ans);
        return ans;
    }

private:
    void backtrack(const string& num, int target, int i, string ways, long resultSoFar, long prevNo, vector<string>& ans) {
        if (i == num.size()) {
            if (resultSoFar == target) {
                ans.push_back(ways);
            }
            return;
        }

        for (int j = i + 1; j <= num.size(); ++j) {
            string s = num.substr(i, j - i);
            if (s.length() > 1 && num[i] == '0') {
                break;  // to handle addition of '05' , '0005' etc.
                        // i.e handling leading zero
                        // in this you can't get possible way considering same remaining num.
            }

            long number = stol(s);

            if (i == 0) {
                // First ele so pick it without any operator
                backtrack(num, target, j, ways + s, number, number, ans);
            } else {
                backtrack(num, target, j, ways + "+" + s, resultSoFar + number, number, ans);
                backtrack(num, target, j, ways + "-" + s, resultSoFar - number, -number, ans);
                backtrack(num, target, j, ways + "*" + s, resultSoFar - prevNo + prevNo * number, prevNo * number, ans);
                // with sign we need to evaluate when we will see '*' next.
            }
        }
    }
};
"""