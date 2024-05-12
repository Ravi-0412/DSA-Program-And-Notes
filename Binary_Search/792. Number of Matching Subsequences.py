# Logic: 1) Store all the indices of a character in a list.
# 2) for each word check if all character indexes are in increasing order.
# if in increasing order then that is one of the subseqence.

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexes = collections.defaultdict(list)
        # store indices of all character in a list
        for i, c in enumerate(s):
            indexes[c].append(i)
        ans = 0
        for word in words:
            pre = -1
            isSub = True
            for c in word:
                # find if any index exist for 'c' which is >= pre.
                next = bisect.bisect_right(indexes[c] , pre)
                if next >= len(indexes[c]):
                    # No possible index
                    isSub = False
                    break
                else:
                    # update pre
                    pre = indexes[c][next]
            ans = ans + 1 if isSub else ans
        return ans


# Note: Say given any char occur maxium 2 times.
# then we only need to store the 1st and last index.
# then , for each char check first with its first index then with 2nd index for increasing order of indexes.