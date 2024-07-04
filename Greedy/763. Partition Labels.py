# time= space= O(n)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n= len(s)
        # form a hashmap which will store the last index of each char.
        last_index = {s[i]: i for i in range(n)}   # s[i]: key ans 'i': value
        start, ans= 0, []    # 'i' denotes the start of the partition
        while start < n:
            # minimum length will be equal to last index of 'start'.
            # but it can go beyond also if char before 'last_index[s[start]]' have last occurence beyond 'last_index[s[start]]'
            # so we need ti check that
            end, j= last_index[s[start]], start +1
            while j < end:
                if last_index[s[j]] > end:
                    end= last_index[s[j]]
                j+= 1
            # now we have go the 1st partition. end will denote the last index of partition.
            ans.append(end- start +1)
            start = end +1   # now we will search for next partition from this index
        return ans




