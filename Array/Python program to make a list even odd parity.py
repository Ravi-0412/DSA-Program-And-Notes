# Logic: 
"""
first element can be either odd or even".
so find ans taking 1st element as odd and 1st element as even.
And for final answer take minimum of both cases.
"""
# time : O(n* logn)
def helper(items, expected):
    countOp = 0
    for i in items:
        while i % 2 != expected:
            if not i:
                # if expected is 1 and i is 0 (not i) then, only in this case it will execute
                return float("inf")  # Not possible
            i //= 2
            countOp += 1
        expected = 1 - expected   # or 1 ^ expected
    return countOp
 
def getMinimumOperations(items):
    return min(helper(items, 1), helper(items, 0)) 

items = [6, 5, 9, 7, 3]
print("ans = ", getMinimumOperations(items))