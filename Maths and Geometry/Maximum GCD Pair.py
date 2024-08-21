# Method 1:
# Brute force: check every pair
# Time: O(n^2 * log(max(arr)))

# Method 2: 
# time: O(N * sqrt(arr[i]))
import math

class Solution:
    def MaxGcd (self, n, arr):
    	high = max(arr)
    	# Array to store the count of divisors. just like bucket sort to save the complexity
    	divisors = [0] * (high + 1)

    	i = 0
    	while i < n:
    
    		# Calculating all the divisors
    		j = 1
    		while j <= math.sqrt(arr[i]):
    			if (arr[i] % j == 0):
    				# Incrementing count for divisor
    				divisors[j] += divisors[j] + 1
    
    				# 'Element/divisor' is also a divisor
    				# Checking if both divisors are not same
    				if (j != arr[i] // j):
    					divisors[arr[i] // j] += 1
    			j += 1
    		i += 1
    
    	# Checking the highest potential GCD. so traverse from right in 'divisors' array
    	# and if you find count of any divisor > 1 then that will be our ans.
    	i = high
    	while i >= 1:
    		# If this divisor can divide at least 2
    		# numbers, it is a GCD of at least 1 pair
    		if (divisors[i] > 1):
    			return i
    		i = i - 1
    	return 1


# Method 3:
# Logic: 
"""
We can use the same logic, divisor occurrence but with a simple optimization. 
Instead of calculating divisor for each number separately. We will calculate divisors collectively
and calculate the answer accordingly. We will traverse each number and then
it all multiple till max_element and will keep track of the number of elements 
for which the current number is the divisor and if the occurrence is greater than 1 we will update our answer.
"""

import math

from math import gcd
from collections import Counter

class Solution:
    def MaxGcd(self, n, arr):
        # Find the maximum element in the array
        max_elem = max(arr)
        
        # Create a frequency array to count multiples of each number
        count = [0] * (max_elem + 1)
        
        # Count the frequency of each element in the array
        for num in arr:
            count[num] += 1
        
        # Iterate from the maximum possible GCD down to 1
        for g in range(max_elem, 0, -1):
            multiple_count = 0
            # Count multiples of g
            for multiple in range(g, max_elem + 1, g):
                multiple_count += count[multiple]
            # If there are at least two multiples of g, it's the maximum GCD
            if multiple_count >= 2:
                return g
        
        return 1  # If no valid GCD is found (this should not happen for valid input)