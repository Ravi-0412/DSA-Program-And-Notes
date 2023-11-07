# our ans will will be minimum when max_no of bricks will end at same point(from left to right)
# vvi: so now our Q reduces to find the max_no of bricks that end at same point.
# we can use hashmap for this.

# endPoints will be start from each row and bricks width will get added to the endPoints.
# after that we will update our hashmap for that endpoint
# then our ans= row - max_Count(of bricks at any end point).

# time: O(row * width), where width= sum of any row since width is equal for each row.

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        row= len(wall)
        bricksEndingPoints= collections.defaultdict(list)  # [endPoint : no_brick_in_diff_row_that_end_at_this_point]
        max_freq= 0
        for bricks in wall:
            endPoint= 0
            for i in range(len(bricks)- 1):   # "-1" for ignoring the last endPoint
                width= bricks[i]
                endPoint+= width
                bricksEndingPoints[endPoint]= 1 + bricksEndingPoints.get(endPoint, 0)
                max_freq= max(max_freq, bricksEndingPoints[endPoint])
        return row - max_freq