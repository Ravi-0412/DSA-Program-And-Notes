# just same as we do addition of two linklist using two pointer.

# time: O(n+ m)

class Solution:
    	def findSum(self, X, Y):
	    X, Y= X.lstrip('0'), Y.lstrip('0')
	    if not X:  # if X had only '0'.
	        X= '0'
	    if not Y:  # if Y had only '0'.
	        Y= '0'
	    carry= 0
	    n, m= len(X), len(Y)
	    i, j= n-1, m-1
	    ans= ""
	    while i>= 0 or j>= 0 or carry:
	        curSum= carry
	        if i>= 0:
	            curSum+= ord(X[i])- ord('0')   # instead of 'curSum+= int(X[i])'.
	            i-= 1
	        if j>= 0:
	            curSum+= ord(Y[j])- ord('0')
	            j-= 1
	        carry, num= divmod(curSum, 10)
	        ans= str(num) + ans
	    return ans