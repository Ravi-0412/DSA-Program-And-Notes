# Logic: if we close at 'i'th hour then, penalty = no of elements on left of i(excluded) having value 'N' + no of elements of right of i(included) having value 'Y'
# number of 'N' passed +  number of 'Y' remaining
# i.e sum of penality when shop is open and customer is not coming('N') + shop is closed and customer is coming('Y')

# from this we get idea of prefix Sum.
# 2) to add penality of 'Y' (right side of 'i' included), we need no of 'Y' on right of 'i'.
# so here we will traverse right to left.

# 2) to add penality of 'N' (left side of 'i'), we need no of 'N' on left of 'i'.
# so here we will traverse left to right.

# After this we have to find the minimum 'i' for which sum of penality is minimum.

# Time: O(n)

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefixSumY = [0]*(n + 1)  # denotes if we close the shop at 'i'th hour then, penality we will get due to 'Y' i.e shop is closed and customer is coming.
        for i in range(n-1, -1, -1):
            if customers[i] == 'Y':
                prefixSumY[i] = prefixSumY[i + 1] + 1
            else:
                prefixSumY[i] = prefixSumY[i + 1]

        prefixSumN = [0]*(n + 1)   # denotes if we close the shop at 'i'th hour then, penality we will get due to 'N' i.e shop was open and customer was not coming.
        for i in range(1, n + 1):
            if customers[i-1] == 'N':
                prefixSumN[i] = prefixSumN[i - 1] + 1
            else:
                prefixSumN[i] = prefixSumN[i - 1]
        # print(prefixSumY,"y")
        # print(prefixSumN,"N")
        earliestHour = n + 1   # ans can't be this
        minPenalty = n + 1    # penality can't ne more than 'n'.
        for i in range(n + 1):
            curHourPenalty = prefixSumY[i] + prefixSumN[i]
            if curHourPenalty < minPenalty:
                earliestHour = i
                minPenalty =  curHourPenalty
        return earliestHour


# Better one: in single pass without prefix sum

# As at any instance i, remaining 'Y' should be minimum and remaining 'N' should be maximum. 
# Therefore, the number of 'Y' passed should be maximum and number of 'N' passed should be minimum.
# So, for that we'll be calculating the score, whenever 'Y' will be found score increases elsewise decreases!
# Maximum score will be recorded, till which the shop will be open and after that shop closes so ind+1 gives the answer.

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        ind = -1
        penality , maxPenality = 0, 0
        for i , c in enumerate(customers):
            if c == 'Y':
                penality += 1
            else:
                penality -= 1
            if penality > maxPenality:
                maxPenality = penality
                ind = i
        return ind + 1
