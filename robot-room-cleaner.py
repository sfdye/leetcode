# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
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
        """
        :type robot: Robot
        :rtype: None
        """
        move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(i, j, cleaned, d):
            robot.clean()
            cleaned.add((i, j))
            for k in range(4):
                x, y = move[(d + k) % 4]
                if (i + x, j + y) not in cleaned and robot.move():
                    dfs(i + x, j + y, cleaned, (d + k) % 4)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnLeft()

        dfs(0, 0, set(), 0)
