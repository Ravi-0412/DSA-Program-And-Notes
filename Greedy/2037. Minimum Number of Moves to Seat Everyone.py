# logic: we jus have to make both the array equal.
# for minimum operation , we have to match smallest to smallest and largest to largest.
# so just sort both the arrays and add the difference of abs value in ans.

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for i in range(len(seats)):
            ans += abs(seats[i] - students[i])
        return ans
