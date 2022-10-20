# when you include any ele incr the sum also
# time: O(2*n)
# space: O(n)
def subsetSums(arr,sum):
    if not arr:
        print(sum,end=" ")
        return
    subsetSums(arr[1:],sum + arr[0])
    subsetSums(arr[1:],sum)

arr= [5,2,1]
subsetSums(arr,0)   # no need to take ans and find the sum

