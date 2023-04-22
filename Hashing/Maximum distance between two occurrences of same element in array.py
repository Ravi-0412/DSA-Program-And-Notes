# logic: we will only update the value when we will see the ele for first time since we have to find the maximum distance.
# if we update always then it will reduce the length.

# Note: in case of finding smallest , we will update everytime
# time= space= O(n)
class Solution:
    def maxDistance(self, arr, n):
        firstTime= {}
        ans= 0  
        for i, n in enumerate(arr):
            if n in firstTime:
                ans= max(ans, i- firstTime[n])
            else:
                firstTime[n]= i
        return ans
    


# Q: "Minimum distance between any two equal elements in an Array"
class Solution:
    def maxDistance(self, arr, n):
        firstTime= {}
        ans= float('inf')
        for i, n in enumerate(arr):
            if n in firstTime:
                ans= min(ans, i- firstTime[n])
            # update everytime with latest index to get minimum length.    
            firstTime[n]= i  
        return ans