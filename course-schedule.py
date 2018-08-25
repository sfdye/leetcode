class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        ind = [0] * numCourses
        outd = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            ind[u] += 1
            outd[v].append(u)

        queue = collections.deque()
        for i in range(numCourses):
            if ind[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            u = queue.popleft()
            count += 1
            for v in outd[u]:
                ind[v] -= 1
                if ind[v] == 0:
                    queue.append(v)

        return count == numCourses
