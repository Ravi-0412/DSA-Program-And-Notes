# Method 1: Two pointer + extra space

# Time = space = O(n)

def print_interleaved_odd_even(arr):
    n = len(arr)
    odd , even = [], []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    ans = []
    odd_index, even_index = 0, 0
    while odd_index < len(odd) or even_index < len(even):
        if odd_index < len(odd):
            ans.append(odd[odd_index])
            odd_index += 1 
        if even_index < len(even):
            ans.append(even[even_index])
            even_index += 1
    return ans

# Method 2: Without extra space
# Just above logic only. 
# Instead of making 'odd' & 'even' array separately and searching in that.
# Simply search for next odd and next even number in given array only.

# Time = O(n), space = O(1)
def print_interleaved_odd_even(arr):
    n = len(arr)
    odd_index = 0
    even_index = 0
    ans = []
    while odd_index < n or even_index < n:
        # Find the next odd number to print
        while odd_index < n and arr[odd_index] % 2 == 0:
            odd_index += 1
        if odd_index < n:
            ans.append(arr[odd_index])
        odd_index += 1

        # Find the next even number to print
        while even_index < n and arr[even_index] % 2 != 0 :
            even_index += 1
        if even_index < n:
            ans.append(arr[even_index])
        even_index += 1
    return ans

# Related Question:
# 1) Rearrange positive and negative numbers alternately
