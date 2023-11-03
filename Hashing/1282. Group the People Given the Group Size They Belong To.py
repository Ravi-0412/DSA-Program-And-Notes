# Time : O(n)

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        noOfPeopleInGroup = collections.defaultdict(list)  # will keep track of people that should belong to a given gr size.
        for i, groupSize in enumerate(groupSizes):
            noOfPeopleInGroup[groupSize].append(i)
            
        ans = []
        for groupSize , people in noOfPeopleInGroup.items():
            # no = len(people)
            # noOfGroup = no //groupSize    # No of group needed for this gr size
            
            # har people ko gr array me dalte jao. maximum gr ka len = groupSize
            cur = []
            for p in people:
                cur.append(p)
                if len(cur) == groupSize:
                    ans.append(cur)
                    cur = []
        return ans
