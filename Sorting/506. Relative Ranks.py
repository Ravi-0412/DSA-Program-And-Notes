# Method1:
# We need maximum ele one by one. But we also need to keep track of their index.
# For keeping track of index 1st enumerate then sort in reverse order according to value.

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(enumerate(score), key = lambda x : x[1], reverse = True)
        for i in range(len(score)):
            ind , num = sorted_score[i]
            if i == 0:
                score[ind] = "Gold Medal"
            elif i == 1:
                score[ind] = "Silver Medal"
            elif i == 2:
                score[ind] = "Bronze Medal"
            else:
                score[ind] = str(i + 1)
        return score

# Method 2:
# Can use max heap for getting maximum one by one.