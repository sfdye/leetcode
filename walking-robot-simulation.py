class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x = y = d = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        obstacles = set(map(tuple, obstacles))
        ans = 0
        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                for _ in range(command):
                    if (x + dx[d], y + dy[d]) not in obstacles:
                        x += dx[d]
                        y += dy[d]
                        ans = max(ans, x ** 2 + y ** 2)

        return ans
