class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # reverse the matrix and to invert the no take 'XOR' with '1'
        # return  [[row[-i]^1 for i in range(1,len(row)+1)] for row in image]    

        # return  [[i^1 for i in reversed(row)] for row in image]

        # return [[1-i for i in row[::-1]] for row in image]     # better one full with basic