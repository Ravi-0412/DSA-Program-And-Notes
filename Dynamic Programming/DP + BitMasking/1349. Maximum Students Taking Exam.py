# Don't know where i am making mistake
# https://www.youtube.com/watch?v=WBlHRJV3YRs



class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:

        def dp(pos, preRow, curRow):
            if pos== m*n:
                return 0
            # find the row and col of cur 'pos'
            i, j= divmod(pos, n)   # dividing by column
            # at the beginning of each row, update the row status.
            if j==0:
                preCur= curRow
                curRow= 0    # bit masking. means no student is placed in curRow
            ans= 0
            # if we don't place the student at cur pos.
            ans= dp(pos+1, preRow, curRow)
            # when we want to place the student.
            if seats[i][j]== ".":
                # we can only place if there is no student at top_left, left and top_right
                top_left= left= top_right= True
                # check if there is student at these places.
                if j >0:
                    # 1) checking at left position
                    # if bit at 'j-1' index is not set in curRow then there is no student at (i, j-1) i.e bit= 0
                    left= (curRow & (1<<(j-1)) == 0)
                    # 2) checking top_left. 
                    # if bit at '(i-1, j-1)' index is not set in preRow then there is no student at (i-1, j-1) i.e bit= 0
                    if i>0:
                        top_left= (preRow & (1 <<(j-1)) == 0)
                # checking top_right
                if j < n-1:
                    top_right= (preRow & (1 <<(j+1)) == 0)

                if top_left and left and top_right:
                    ans= max(ans, 1+ dp(pos+1, preRow, curRow | (1<<j)))
            return ans

        m, n= len(seats), len(seats[0])
        print(m, n)
        return dp(0, 0, 0)