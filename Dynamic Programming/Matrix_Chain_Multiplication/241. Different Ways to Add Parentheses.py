# just similar logic to '95. Unique Binary Search Trees II'.
# time : Catalan(n)

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n= len(expression)
        
        # operation for an operator
        def helper(leftValue, rightValue, op):
            if op == '+':
                return leftValue + rightValue
            if op == '-':
                return leftValue - rightValue
            if op == '*':
                return leftValue * rightValue

        def solve(expression):
            if expression.isdigit():
                # means if there is only digit then simply return that in a list.
                return [int(expression)]
            if expression in dp:
                return dp[expression]
            ans= []
            # we can split left and right at each operator
            # left side ')' and right side '(' logically
            for i in range(len(expression)):
                if expression[i] in  '-+*':
                    # if operator split at this position
                    leftValues =  solve(expression[: i])
                    rightValues = solve(expression[i+ 1: ])
                    # calculate the values for all possible combinations by splitting at this operator i. exp[i]
                    for leftValue in leftValues:
                        for rightValue in rightValues:
                            ans.append(helper(leftValue, rightValue, expression[i]))
            dp[expression] = ans
            return ans

        dp  =  {}
        return solve(expression)

