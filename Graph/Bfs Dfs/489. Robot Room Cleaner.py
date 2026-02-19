
"""
Logic link : https://1drv.ms/o/c/2e0ac565ff6aeb82/IgC20s4qd35MTaU9V9Tzi1u0AYecoT4d1-sYC5x2BOWNfh8
"""

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        # face direction: 0(up) , 1(right),  2(down) , 3(left)
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = set()
        # Start from cell (0,0) with the robot initially facing Up (direction index 0)
        self.cleanRoomRecursive(robot, visited, directions, 0, 0, 0)

    def cleanRoomRecursive(self, robot, visited, directions, i, j, faceDirection):
        # mark the current cell as visited
        visited.add((i, j))
        
        # clean the current cell
        robot.clean()
        
        """
        try out 4 different directions : up, right, down, left
        The robot will attempt to move in its current facing direction, then turn right,
        and repeat for all 4 directions.
        k = 0: keep moving towards the current direction that we're facing
        k = 1: make 1 right turn already, and try that new direction
        k = 2: make 2 right turns already, and try that new direction
        k = 3: make 3 right turns already, and try that new direction
        """
        for k in range(4):
            nextFaceDirection = (faceDirection + k) % 4
            iNext = i + directions[nextFaceDirection][0]
            jNext = j + directions[nextFaceDirection][1]
            
            # next cell has not been visited and is accessible
            if (iNext, jNext) not in visited and robot.move():
                self.cleanRoomRecursive(robot, visited, directions, iNext, jNext, nextFaceDirection)
                
                # backtracking: return to (i, j) and face the same direction

                # 1. Turn 180 degrees to face back towards (r, c)
                robot.turnRight()
                robot.turnRight()
                # 2. Move back to (r, c)
                robot.move()
                # 3. Turn 180 degrees again to restore the original orientation
                robot.turnRight()
                robot.turnRight()
            
            # move to the next potential direction
            # the current direction has been explored
            # we should make a right turn, and try to explore another direction
            robot.turnRight()
