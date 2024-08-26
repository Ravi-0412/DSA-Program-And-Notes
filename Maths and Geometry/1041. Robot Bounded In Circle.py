# The key observation is that the "trajectory of the path does not matter 
# but the direction after one run of the instruction does!".
# Ans: Just return true if the final position does not change or the facing direction is different from the beginning.

# How?
# i) After all the instructions, if robot is at (0,0), that means the robot will be at (0,0) after every cycle, so must be true.
# ii) After all the instructions, if robot is not at (0,0) and face north, 
# say it's at (x,y), that means after every cycle, robot moves [x-0, y-0] but its direction is still the starting direction (north), 
# that means it will keep moving further away from (0,0) infinitely if we continue to repeat the loop, therefore false.
# iii) After all the instructions, if robot is not at (0,0) and face non-north, then it means:
#       if direction is east, that means robot turns right after every cycle i.e (from north to east), 
#       (from east -> south), (from south -> west), from(west -> North).
# so eventually it will stay in the same area instead of moving further away from (0,0) infinitely
#       same thing for every other non-north directions.

# Simplest code
# java
"""
class Solution {
    public boolean isRobotBounded(String instructions) {
        if (instructions.length() == 0)
            return false;
        int x = 0;
        int y = 0;  // initial points of the robot
        String directions = "North"; // initial direction of robot
        for (char ch: instructions.toCharArray()) {
            if (ch == 'G') {
                if (directions.equals("North"))
                    y += 1;
                else if (directions.equals("South"))
                    y -= 1;
                else if(directions.equals("East"))
                    x += 1;
                else
                    x -= 1;
            }
            else if (ch == 'L') {
                if (directions.equals("North"))
                    directions = "West";
                else if (directions.equals("West"))
                    directions = "South";
                else if (directions.equals("South"))
                    directions = "East";
                else directions = "North";
            }
            else if (ch == 'R') {
                if (directions.equals("North"))
                    directions = "East";
                else if (directions.equals("East"))
                    directions = "South";
                else if (directions.equals("South"))
                    directions = "West";
                else directions = "North";
            }
        }
        // return true if we are at (0,0)
        if (x == 0 && y == 0)
            return true;
        // if we are in north direction after one cycle then return False
        if (directions.equals("North"))
            return false;
        return true;
    }
}
"""

# Method 2:
# just shortcut of above using keeping a pointer on direction array.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Directions: 0 - up(North), 1 - left(West), 2 - down(South), 3 - right(East)
        dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # taking initial direction as North and G = 1 , made this array.
        i = 0  # Direction index, starting facing upwards
        
        # Initial position of the robot
        x, y = 0, 0
        
        # Iterate through each instruction in the string
        for instruction in instructions:
            if instruction == 'L':
                # Turn left: Increment direction index (rotate counterclockwise)
                i = (i + 1) % 4
            elif instruction == 'R':
                # Turn right: Decrement direction index (rotate clockwise)
                i = (i + 3) % 4
            else:
                # Move in the current direction
                x += dir[i][0]
                y += dir[i][1]
        
        # After executing all instructions, check if the robot returns to the starting position
        # or if it ends up facing a different direction than it started
        return (x == 0 and y == 0) or i != 0


# java
"""
class Solution {
    public boolean isRobotBounded(String instructions) {
        // Directions: 0 - up, 1 - left, 2 - down, 3 - right
        int[][] dir = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
        int i = 0; // Direction index, starting facing upwards
        
        // Initial position of the robot
        int x = 0;
        int y = 0;
        
        // Iterate through each instruction in the string
        for (int s = 0; s < instructions.length(); s++) {
            char instruction = instructions.charAt(s);
            
            // Check if it's a rotation
            if (instruction == 'L') {
                // Turn left: Increment direction index (rotate counterclockwise)
                i = (i + 1) % 4; // Modulo 4 ensures it loops back to 0 after reaching 3
            } else if (instruction == 'R') {
                // Turn right: Decrement direction index (rotate clockwise)
                i = (i + 3) % 4; // Equivalent to (i - 1 + 4) % 4 to handle negative values
            } else {
                // Move in the current direction
                x += dir[i][0]; // Update x coordinate based on current direction
                y += dir[i][1]; // Update y coordinate based on current direction
            }
        }
        
        // After executing all instructions, check if the robot returns to the starting position
        // or if it ends up facing a different direction than it started
        return (x == 0 && y == 0) || i != 0;
    }
}
"""
