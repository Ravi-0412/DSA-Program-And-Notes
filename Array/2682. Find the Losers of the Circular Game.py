# Just Brtute force

# Constraint is very small , so we can use array to store the count.
# Or can use 'set'.

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        i= 1  # turn
        count= [0]* (n + 1)   # to check where we reach '2' time. 1-based indexing.
        count[1]= 1     # starting from person '1'
        curNum= 1
        while True:
            # next person
            curNum= (curNum + i*k) % n 
            # using 1-based indexing but doing modulus with 'n'. so '0' will mean 'n' only.
            # Since doing % with 'n' so if we have to check whether we reach 'n' separately
            # otherwise we won't get n'
            if curNum== 0:
                curNum= n
            count[curNum]+= 1
            if count[curNum]== 2:
                break
            i+= 1
            
        ans= []
        for i, cnt in enumerate(count):
            if i != 0 and cnt== 0:
                ans.append(i)
        return ans


# Note: We can use 'set()' also.
