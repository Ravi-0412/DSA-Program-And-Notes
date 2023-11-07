# logic: just same logic as prefixSum.

# Traverse the words and when the cur word start and end with vowel, add 1 to the prefixCount else= pre prefixCount.

# Queries are just same finding the prefixSum between two index 'i' and 'j' both inclusive.
# which= prefixSum[j + 1] - prefixSum[i], when we use 1-based indexing in prefixSum.

# time: O(n + m)

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n= len(words)
        prefixCount= [0]* (n + 1)  # using 1-based indexing 
        for i, word in enumerate(words):
            if word[0] in ('a', 'e', 'i', 'o', 'u') and word[-1] in ('a', 'e', 'i', 'o', 'u') :
                prefixCount[i + 1]= 1 + prefixCount[i]
            else:
                prefixCount[i + 1]= prefixCount[i]
                
        ans= []
        for i, j in queries:
            count= prefixCount[j + 1] - prefixCount[i]
            ans.append(count)
        return ans


