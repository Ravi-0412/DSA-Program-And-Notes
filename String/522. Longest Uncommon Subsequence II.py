# Part 1 of this Q: 521. Longest Uncommon Subsequence I

# Logic: Asking for longest so there will be only two cases in this:
# 1) if both equal then ans = -1
# 2) ans = max(len(a), len(b))

# Now come to this question

# Logic: Commented in code

# Time: O(m * (m + n))

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def subsequence(a, b):
            if len(a) >= len(b): 
                # if len(a) > len(b) then also not possible and if length is equal tehn they must be equal which is also not possible
                return False
            i , j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1   # will incr only in equal case.
                j += 1   # 'j' will be incremented always
            return i == len(a)

        freq = Counter(strs)
        exclude = [c for c, f in freq.items() if f > 1]  # freq is more than one so these can't be ans.
        possible_ans = [c for c, f in freq.items() if f == 1]   # ans will be from one of these
        # sort according to decreasing order of length for easier track of ans.
        possible_ans.sort(key = lambda x : len(x) , reverse = True)
        # Now check string in possible_ans one by one if that can be our ans.
        # For this we have to check each string if that is subsequence of any of the string in 'exclude'
        
        # But if exclude is empty then longest string in possible_ans will be our ans.
        if not exclude:
            return len(possible_ans[0])
        
        # otherwise we have to check one by one
        for s in possible_ans:
            is_sub = False
            for s1 in exclude:
                if subsequence(s, s1):
                    is_sub = True
                    exclude.append(s)
                    break
                # else:
                #     print(s, "sub")
                #     return len(s)
            if is_sub == False:
                return len(s)
        return -1