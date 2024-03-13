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
