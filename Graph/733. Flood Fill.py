# my mistake: i didn't understand the Q properly. please read every Q properly first. Don't blindly go to solve after reading half of the Q.
# note: i am making this mistake in almost Q and one of the main reason for Q takes a lot of time to solve.
# First read match the input vs output for few test cases an dthen only go to find algorithm and then at alst code.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q= deque([(sr,sc,image[sr][sc])])
        while q:
            for i in range(len(q)):
                r, c, pixel= q.popleft()  # clr= pixel at that (r,c)
                image[r][c]= color
                directions= [[-1,0],[1,0],[0,-1],[0,1]]  # up,down,left,right
                for dr,dc in directions:
                    row,col= r+ dr, c+ dc
                    if 0<=row < len(image) and 0<= col < len(image[0]) and image[row][col]== pixel and image[row][col]!=color:
                        q.append((row,col,image[row][col]))
        return image