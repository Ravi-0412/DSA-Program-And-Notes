# Logic: 
# The idea is to compare the key with middle 3 elements, if present then return the index.
# If not present, then compare the key with middle element to decide whether to go in left half or right half. 
# Comparing with middle element is enough as all the elements after mid+2 must be greater than element mid and
# all elements before mid-2 must be smaller than mid element.

# Python 3 program to find an element
# in an almost sorted array

# A recursive binary search based function.
# It returns index of x in given array arr[l..r]
# is present, otherwise -1


def binarySearch(arr, l, r, x):

	if (r >= l):

		mid = int(l + (r - l) / 2)

		# If the element is present at one
		# of the middle 3 positions
		if (arr[mid] == x):
			return mid
		if (mid > l and arr[mid - 1] == x):
			return (mid - 1)
		if (mid < r  and arr[mid + 1] == x):
			return (mid + 1)

		# If element is smaller than mid, then
		# it can only be present in left subarray
		if (arr[mid] > x):
			return binarySearch(arr, l, mid - 2, x)   # 'mid-1' we already checked above

		# Else the element can only
		# be present in right subarray
		return binarySearch(arr, mid + 2, r, x)      # 'mid + 1' we already checked above

	# We reach here when element
	# is not present in array
	return -1


arr = [3, 2, 10, 4, 40]
n = len(arr)
x = 4
result = binarySearch(arr, 0, n - 1, x)
if (result == -1):
	print("Element is not present in array")
else:
	print("Element is present at index", result)

# This code is contributed by Smitha Dinesh Semwal.
