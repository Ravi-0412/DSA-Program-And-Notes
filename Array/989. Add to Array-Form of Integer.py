# time= space= O(n)

# since we need the given array as integer, so for this first converted into string and then to integer.
# then add with 'k'.
# after that then again convert the num we go6 after addition into string and then convert into list 
# finally return 
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        b= "".join(str(n) for n in num)  # first converting the arr into string
        s= str(int(b) + k)    # converted the array into integer and added 'k' and then into string.
        ans= [int(c) for c in s]   # fianlly converted the atring ans into list 
        return ans