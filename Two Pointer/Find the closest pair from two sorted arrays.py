# just "two sum logic"

# here closest_pair_sum can be greater or lesser than 'k'.
# so after every possible sum update 'minDiff'.

# Time : O(n)

def printClosest(arr1, arr2, k):
    m, n= len(arr1), len(arr2)
    minDiff= float('inf')
    ele1, ele2= 0, 0  # to store the ans
    l= 0  # will point to 1st index in arr1
    r= n-1  # will point to the last index in arr2
    while l < m and r >=0:
        sum= arr1[l] + arr2[r]
        diff= abs(k- sum)
        if diff < minDiff:
            minDiff= diff
            ele1, ele2= arr1[l], arr2[r]
        if diff== 0:
            break
        if sum > k:
            r-= 1
        else:
            l += 1
    print("pair is: ", ele1, ele2)


arr1= [1, 4, 5, 7]
arr2= [10, 20, 30, 40]
# x= 32
x= 50

printClosest(arr1, arr2, x)

