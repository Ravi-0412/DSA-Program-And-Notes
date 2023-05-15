# Just Brtute force

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        i= 1
        count= [0]* 51   # to check where we reach '2' time. 1-based indexing.
        count[1]= 1     # starting from person '1'
        curNum= 1
        while True:
            # nect person
            curNum= (curNum + i*k) % n 
            # using 1-based indexing but doing modulus with 'n'. so '0' will mean 'n' only.
            if curNum== 0:
                curNum= n
            count[curNum]+= 1
            if count[curNum]== 2:
                break
            i+= 1
            
        ans= []
        for i, cnt in enumerate(count):
            if i != 0 and i<= n and cnt== 0:
                ans.append(i)
        return ans

