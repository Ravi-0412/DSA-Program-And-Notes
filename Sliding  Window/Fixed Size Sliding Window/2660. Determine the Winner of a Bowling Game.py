# time = space = O(n)
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        def getScore(arr):
            score= 0
            freq= {}  # will tell the freq of '10' in pre two index. max freq = 2
            for i, num in enumerate(arr):
                if 10 in freq and freq[10] > 0:
                    # if cur num = 10 or we have seen '10' in previous two
                    score+= 2*num
                else:
                    score+= num
                # Add the freq if = 10
                if num== 10:
                    freq[10]= 1 + freq.get(10, 0)
                # Remove freq if 2nd prev ele = 10
                if i >= 2 and arr[i-2]== 10:
                    freq[10]-= 1
            return score

        s1, s2= getScore(player1), getScore(player2)

        if s1> s2: return 1
        if s1 < s2: return 2
        return 0


# method 2: More better one
# Just replace the frequency hashmap in above method by varaible.
# time = O(n)
# space = O(1)

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        def getScore(arr):
            score= 0
            count= 0 # will count the no of 10 seen in previous two turn. max = 2
            for num in arr:
                if count > 0:
                    score+= 2*num
                else:
                    score+= num
                if num== 10:  # then for next 2 ele we can do multiply by '2' because of cur ele if = 10 .so make count= 2
                    count= 2
                else:   # decr each time if not equal to '10'. Effect of prev 10 will be now only to one next element.
                    count-= 1  
            return score

        s1, s2= getScore(player1), getScore(player2)

        if s1> s2: return 1
        if s1 < s2: return 2
        return 0