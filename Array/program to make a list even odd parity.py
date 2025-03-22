"""
Consider both cases: 1) When 1st element is odd and 2) when 1st element is even. 
And take minimum of both
"""
def toggle_parity(expected):
    return 1 if expected == 0 else 0

def count_operations_to_alternate(arr, expected_parity):
    operations = 0
    for num in arr:
        if (num % 2 == 0) != (expected_parity == 1):  # Check if parity is incorrect
            operations += 1
        expected_parity = toggle_parity(expected_parity)  # Alternate parity

    return operations

def min_operations_to_alternate(arr):
    return min(count_operations_to_alternate(arr, 1), count_operations_to_alternate(arr, 0))

# Example test case
items = [6, 5, 9, 7, 3]
print(min_operations_to_alternate(items))  # Output: Minimum operations required
