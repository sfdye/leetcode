class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        stop_route = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                stop_route[j].add(i)
        queue = collections.deque([(S, 0)])
        seen = set([S])
        while queue:
            stop, count = queue.popleft()
            if stop == T:
                return count
            for route in stop_route[stop]:
                for next_stop in routes[route]:
                    if next_stop not in seen:
                        queue.append((next_stop, count + 1))
                        seen.add(next_stop)
                routes[route] = []
        return -1
