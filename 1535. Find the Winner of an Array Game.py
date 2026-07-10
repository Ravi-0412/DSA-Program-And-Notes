"""
Logic : The smaller element moves to the back of the array. Once an element loses, 
it can never become the maximum of the entire array, because it just lost to something bigger. 
This means it will never win $k$ consecutive rounds later on.

What happens if k is extremely large (e.g., k = 10^9), but the array size is small (e.g., $n = 7)?
-> If we scan the entire array once and reach the end without any number hitting $k$ consecutive wins, 
it means the number we are left holding is the absolute maximum element of the entire array.
Once the absolute maximum element reaches position 0, it will never lose a game again, no matter how many rounds are played.
time : O(n), space : O(1) 
"""

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current_winner = arr[0]
        win_count = 0
        
        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                win_count += 1
            else:
                # new winner
                current_winner = arr[i]
                win_count = 1
                
            if win_count == k:
                return current_winner
                
        # If the loop completes without hitting k wins, 
        # current_winner is the absolute maximum of the array and will win forever.
        return current_winner

# No of round required = win_count

  
