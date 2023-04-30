class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        s1= 0
        freq1= {}  # will tell the freq of '10' in pre two index
        for i, num in enumerate(player1):
            if 10 in freq1 and freq1[10] > 0:
                s1+= 2*num
            else:
                s1+= num
            if num== 10:
                freq1[10]= 1 + freq1.get(10, 0)
            if i >= 2 and player1[i-2]== 10:
                freq1[10]-= 1

        s2= 0
        freq2= {}
        for i, num in enumerate(player2):
            if 10 in freq2 and freq2[10] > 0:
                s2+= 2*num
            else:
                s2+= num
            if num== 10:
                freq2[10]= 1 + freq2.get(10, 0)
            if i >= 2 and player2[i-2]== 10:
                freq2[10]-= 1
        
        if s1> s2: return 1
        if s1 < s2: return 2
        return 0
    

# same thing using function to make code look good and clean
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        def getScore(arr):
            score= 0
            freq= {}  # will tell the freq of '10' in pre two index
            for i, num in enumerate(arr):
                if 10 in freq and freq[10] > 0:
                    score+= 2*num
                else:
                    score+= num
                if num== 10:
                    freq[10]= 1 + freq.get(10, 0)
                if i >= 2 and arr[i-2]== 10:
                    freq[10]-= 1
            return score

        s1, s2= getScore(player1), getScore(player2)

        if s1> s2: return 1
        if s1 < s2: return 2
        return 0


# method 2: logical one
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        def getScore(arr):
            score= 0
            count= 0
            for num in arr:
                if count > 0:
                    score+= 2*num
                else:
                    score+= num
                if num== 10:  # then for next 2 ele we can do multiply by '2' so make count= 2
                    count= 2
                else:   # decr each time if not equal to '10'.
                    count-= 1  
            return score

        s1, s2= getScore(player1), getScore(player2)

        if s1> s2: return 1
        if s1 < s2: return 2
        return 0