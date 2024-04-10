#  Q: The way we exactly play the snake and ladder game in Ludo.

# logic: Just we have to apply bfs or multisource bfs.
# Main problem and tough part of this Q is to convert the Square no -> coordinates.
# After that exactly same as bfs..
# Understand this conversion properly by drawing on pen and paer for more clarity.

# my mistake: i was finding the exact col by taking the 'row_no' from top i.e 
# after calculating the exact row no from top.

# Note:This Q can be also asked like this:"find the minimum number of dice throws required to reach the last cell(destination) from the source (1st cell)."

# time= space= O(n*n)

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n= len(board)

        def SquareNoToCoordinate(square):  # will return the coordinate of the 'square' no.
            r, c= divmod(square- 1, n)   # square no is in '1' based indexing.
            # so for getting the coordinates in '0' based indexing(board) dividing by 'n'. 
            # it will give row no from bottom , so from top row no will be...
            row_no= (n -1) - r   # board is zero based indexing so subtracting with 'n-1'.
            # for finding exact col(due to cell no from left->right, right->left in alternate row) , 
            
            # it will depend on whether 'r' is odd or even from bottom
            if r% 2== 0:  # if even
                return [row_no, c]
            return [row_no, n-c-1]    

        q= collections.deque([])
        visited= set()
        q.append((1, 0))  # [squareNo, step]
        visited.add(1)  # (square No)
        while q:
            square, steps= q.popleft()
            # move to all the possible places. just we throw the dice and move acc to what no we will get.
            for i in range(1, 7):
                nextSquare= square + i  # next cell no we will take
                # check if this cell is snake or ladder.
                # for this we need value of this cell from board.
                # And for this 1st we have to get the coordinates of nextSqaure
                r, c= SquareNoToCoordinate(nextSquare)
                # Now check if this is position of snake or ladder
                if board[r][c]!= -1:
                    nextSquare= board[r][c]
                # check if nextSqaure is destination
                if nextSquare== n*n:
                    return steps + 1
                # Add the 'nextSquare' in 'q' if not visited and <= n*n
                if nextSquare < n*n and nextSquare not in visited:
                    q.append((nextSquare, steps +1))
                    visited.add(nextSquare)
        return -1


# my mistake: i was finding the exact col by taking the 'row_no' from top i.e 
# after calculating the exact row no from top.
# it will depend from bottom.

def SquareNoToCoordinate(square):  # will return the coordinate of the 'square' no.
            r, c= divmod(square- 1, n)   # square no is in '1' based indexing.
            # so for getting the coordinates in '0' based indexing(board) dividing by 'n-1'. 
            # it will give row no from bottom , so from top row no will be...
            r= (n -1) - r   # board is zero based indexing so subtracting with 'n-1'
            # for finding exact col , it will depend on whether row is odd or even
            if r% 2:  # if odd from top
                return [r, c]
            return [r, n-c-1]



