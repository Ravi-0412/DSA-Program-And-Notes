# If not asked for unique pairs then , simple 'two sum' will work.
def find_pairs_with_sum(arr, k):
    seen = {}
    
    for num in arr:
        target = k - num
        if target in seen:
            print((target, num))
        
        # Add num to seen dictionary with its count
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

# Example usage
arr = [1, 5, 7, -1, 5]
k = 6
find_pairs_with_sum(arr, k)


# Now come to actual question where we need to print only unique pair.

# Method1: Sorting
# time = O(n*logn)
def find_pairs_with_sum(arr, k):
    arr.sort()  # Sort the array first
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == k:
            print((arr[left], arr[right]))
            left += 1
            right -= 1
            
            # Skip duplicate elements
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
                
        elif current_sum < k:
            left += 1
        else:
            right -= 1


# method 2: Optimised
# store all pair in set
# Time : O(n)
def find_pairs_with_sum(arr, k):
    seen = {}
    output_pairs = set()  # to keep track of printed pairs
    
    for num in arr:
        target = k - num
        if target in seen:
            # Ensure uniqueness by adding pairs to a set before printing
            pair = (min(target, num), max(target, num))
            if pair not in output_pairs:
                print(pair)
                output_pairs.add(pair)
        
        # Add num to seen dictionary with its count
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

# Other way of writing above but tim = O(n*logn)
def paired_elements(arr, target_sum):
    # Sort the array
    arr.sort()

    # Initialize pointers
    low = 0
    high = len(arr) - 1

    # Dictionary to track unique pairs
    unique_pairs = {}

    # Iterate with two pointers
    while low < high:
        # Check if sum equals the target
        if arr[low] + arr[high] == target_sum:
            # Print pair if elements are not already in the dictionary
            if arr[low] not in unique_pairs or arr[high] not in unique_pairs:
                print("The pair is : (", arr[low], ", ", arr[high], ")")
                unique_pairs[arr[low]] = True
                unique_pairs[arr[high]] = True
            low += 1
            high -= 1
        # Adjust pointers based on sum comparison
        elif arr[low] + arr[high] > target_sum:
            high -= 1
        else:
            low += 1


# Method 3: Without using extra set for checking all pairs
def printPairs(arr, n, sum):
    # Store counts of all elements in map m
    m = {}

    # Traverse through all elements
    for i in range(n):
        # Search if a pair can be formed with arr[i].
        rem = sum - arr[i]
        if rem == arr[i]:       # we need to handle this case seperately
            # Check if the complement is in the map and occurs only once
            if m.get(rem, 0) == 1:
                print(f"({rem}, {arr[i]})")
        elif rem in m and arr[i] not in m:
            # Check if the complement is in the map and the current element is not in the map
            print(f"({rem}, {arr[i]})")
        m[arr[i]] = m.get(arr[i], 0) + 1  # Update the map with the current element's count


