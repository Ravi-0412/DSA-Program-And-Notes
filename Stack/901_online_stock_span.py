# just same method of finding 'next greater left'.

# Method 1: Brute force
# For each price find the 'next greater left'.
# Time: o(n * n)

# Metho2: Optimising
# If we keep (price, ans) then for further number greater than 'price'
# We don't have to traverse again fully.
# Because 'accumulated_ans' we are storing in stack.

# One price will be pushed once and popped once.
# So 2 * N times stack operations and N times calls.

# Amortized time = O(1)

class StockSpanner:
    
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1  # for cur 'price'
        while self.stack and self.stack[-1][0] <= price:
            p, days = self.stack.pop()
            ans += days
        self.stack.append((price, ans))
        return ans
