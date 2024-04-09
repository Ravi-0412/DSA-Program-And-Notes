# Logic; On left of 'k' , maximum we can add time = tickets[k] for each ticket.
# On left,maximum we can add time = tickets[k] - 1 for each ticket. 


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        ans = tickets[k]
        for i in range(k):
            ans += min(tickets[k] , tickets[i])
        for i in range(k+1, n):
            ans += min(tickets[k] - 1, tickets[i])
        return ans