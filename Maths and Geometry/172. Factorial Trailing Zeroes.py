# logic: 
"""
number of 10's in a number gives us number of trailing zeros in that number.
"""

# Method 1: Brute force
# logic: we can calcualte the n! and check how many 10's are in there.

# Time: O(n)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        ans = 0
        while factorial % 10 == 0:
            factorial //= 10
            ans += 1
        return ans

# Note: Brute force will not work for bigger input &&
# will wrong answer in java,c++ where factorial can overflow.

# Method 2: Optimisation
# Observation:
"""
What is the property of 10?

We can get 10 from 2 & 5 (2x5). Can you get 10 in any other way? No.

So, let's break it down further.

10 = 2 x 5 [1(2),1(5)]
100 = 2 x 2 x 5 x 5 [2(2),2(5)]
120 = 2 x 2 x 2 x 3 x 5 [3(2),1(3),1(5)]
1200 = 2 x 2 x 2 x 2 x 3 x 5 x 5 [4(2),1(3),2(5)] //2 appears 4 times, 3 appears 1 time, 5 appears 2 times}
50 = 2 x 5 x 5 [1(2),2(5)]

From above you will see, among 5 and 2 whichever appears lowest amount is the count of our trailing zeros.
Note: But for n!, we know we will have more 2's than 5. So ans = no of power of 5 in n!.
Let's see an example:
5! = 1 x 2 x 3 x 4(2x2) x 5 = [3(2),1(5)]

Try writing down couple more example and you will understand. So, in 25! how many 5 will be there?

....x5....x10....x15....x20....x25 = x5...x2x5....x3x5....x4x5....x5x5 = 6 , Because 25 itself has 2 5's in it.

But we know if n>=5 it will have 5 as a factor.

So, based on our intuition so far.

If n=5 ... there will be 1(5)
If n=10 ... there will be 2(5)
If n=15 ... there will be 3(5)
If n=25 ... there will be 5(5) + 1 (5)

Now all we need to do is keep dividing n by 5 and add the result to our existing result until n get to 0.
"""
# time: O(log(5))

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count

# Recursive way:
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: 
            return 0
        return n//5 + self.trailingZeroes(n//5)

# other way
# Logic: for n <= 10**4, maximum powerof '5' that is less than 10**4 is 3125
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return n//5 + n//25 + n//125 + n//625 + n//3125