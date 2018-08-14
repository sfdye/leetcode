class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        if not image:
            return []

        oldColor = image[sr][sc]

        if newColor == oldColor:
            return image

        N, M = len(image), len(image[0])

        def dfs(i, j):
            if i < 0 or i >= N or j < 0 or j >= M or image[i][j] != oldColor:
                return
            image[i][j] = newColor
            for k in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                dfs(i + k[0], j + k[1])

        dfs(sr, sc)
        return image
