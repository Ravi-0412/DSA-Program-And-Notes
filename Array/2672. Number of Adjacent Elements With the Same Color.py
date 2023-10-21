# Intution:
# When we add one number to nums then only impact of this to left & right adacent values.
# Like it can have same adjacent to the previous or to the next one only.
# So we have to check the status of adjacent equality before updating the index and after updating the index.


# logic: index pe color add karne se phle adjacent 'pre' and 'next' index ka color check karo, 
# Agar same hoga tb 'abhi tak jo ans me h usme '-1' kar denge.
# Reason: Agar same color hua to change karne ke bad count decrease hoga.

# then us index pe color change kar do.
# change karne ke bad check karo same color to nhi h iska adjacent ke pass.
# Agar h tb ans ko badha do.
# Reason: Agar same color hua to change karne ke bad count badhega.


# time= space= O(n)

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ans= []
        curAns= 0
        nums= [0]* n
        for index1, color in queries:
            pre= nums[index1 -1] if index1 > 0 else 0
            next= nums[index1 +1] if index1 < n-1 else 0
            # if 'index1' is colored and have same color as prev index
            if nums[index1] and pre== nums[index1]:
                curAns-= 1
            # if 'index1' is colored and have same color as next index
            if nums[index1] and next== nums[index1]:
                curAns-= 1
            # assign the color
            nums[index1]= color
            # check if pre index has same color
            if pre== nums[index1]:
                curAns+= 1
            # check if next index has same color
            if next== nums[index1]:
                curAns+= 1
            ans.append(curAns)
        return ans