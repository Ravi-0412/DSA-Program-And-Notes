# logic: 1)  If has enough power then do 'Face-up' with minimal value of token so that
# we can increase score by '1' with minimal use of power.
# Here we need to get unplayed token having minimum token value.

# 2) If not enough power then if score is > 0 then increase your score by as much as possible 
# reducing score by '1'. Here we need to get unplayed token having maximum token value.

# From these we get intution of sorting + Two pointer.

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        score = 0
        ans = 0
        i, j = 0, n - 1  # 'i' will denote minimum unused token and 'j': will denote max unused token . 
        while i <= j:
            if power >= tokens[i] :
                score += 1
                ans = max(ans, score)
                power -= tokens[i]
                i += 1
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        return ans