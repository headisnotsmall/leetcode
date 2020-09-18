'''
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
'''


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        moves = list(instructions)
        loc = [0, 0]
        turn = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        facing = turn[0]
        n = 0
        while True:
            for movement in moves:
                if movement == "G":
                    loc[0] = loc[0] + facing[0]
                    loc[1] = loc[1] + facing[1]
                elif movement == "L":
                    for i in range(4):
                        if facing == turn[i]:
                            facing = turn[(i + 1) % 4]
                            facing = turn[(i + 1) % 4]
                            break
                elif movement == "R":
                    for i in range(4):
                        if facing == turn[i]:
                            facing = turn[(i - 1) % 4]
                            facing = turn[(i - 1) % 4]
                            break
            if loc == [0, 0]:
                return True
            else:
                n += 1
                if n == 100:
                    return False


# better solution

'''
for i in instructions:
            if i == 'R': dx, dy = dy, -dx
            if i == 'L': dx, dy = -dy, dx
            if i == 'G': x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0,1)
'''
        
#         x = 0
#         y = 0
#         dx = 0
#         dy = 1
        
        
#         for i in instructions:
#             if i=='R':
#                 dx = dy
#                 dy = -dx
#             if i=='L':
#                 dx = -dy
#                 dy = dx
                
#             if i=='G':
#                 x = x+dx
#                 y = y+dy
        
#First condition returning back to 0,0, indicates a circle
#Second condition if the change in direction (dx and dy)is not facing north, i.e., 0,1, then it will get back to the initial sequence in some steps
#return (x,y)==(0,0) or (dx,dy)!=(0,1)
#return (x==0 and y==0) or not(dx==0 and dy==1)