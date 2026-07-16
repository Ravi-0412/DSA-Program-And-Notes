"""
we just have to find minimum size of window containing a duplicate.
"""

# Method 1 : Simplest
"""
Track Last Seen Index
Every time we encounter a card we've seen before, we calculate the distance, update our minimum answer, and update its index to the current one.
"""

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # Maps card value -> its most recent index in the array
        last_seen = {}
        min_cards = float('inf')
        
        for i, card in enumerate(cards):
            if card in last_seen:
                # Calculate the total consecutive cards picked up between the duplicates
                consecutive_count = i - last_seen[card] + 1
                min_cards = min(min_cards, consecutive_count)
            
            # Always update to the latest index to get the tightest/smallest gap
            last_seen[card] = i
            
        return min_cards if min_cards != float('inf') else -1

# Method 2: Sliding window + Hashmap
import collections

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        seen = collections.defaultdict(int)
        ans = float('inf')  # Use infinity to avoid conflicts if the answer is exactly 'n'
        left = 0
        
        for right in range(n):
            seen[cards[right]] += 1
            
            # If the window size is greater than the count of unique elements,
            # it means we have at least one duplicate pair in our current window.
            while (right - left + 1) > len(seen):
                ans = min(ans, right - left + 1)
                card_to_remove = cards[left]
                seen[card_to_remove] -= 1
                if seen[card_to_remove] == 0:
                    del seen[card_to_remove]
                left += 1
                
        return ans if ans != float('inf') else -1

  
