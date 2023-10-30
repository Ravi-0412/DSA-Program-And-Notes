# logic: if we can make every ele a multiple of  "k" then gcd of array will be in multiple of 'k'.

# for minimum no of operation we can make every ele val= nearest multiple of k.
# this we can get either by removing or adding some element.

# time: O(n)
def minOperation(arr, k):
    ans= 0
    for num in arr:
        # to_remove= num % k     # we can make by subtracting this 
        # to_add= k - to_remove  # we make make by adding this.
        # cost= min(to_remove, to_add)
        # ans+= cost
        ans += min(num % k , k - (num % k))    # in short
    return ans

arr= [4,5,6]
k= 5

# arr= [4,9,6]
# k= 5
print(minOperation(arr, k))