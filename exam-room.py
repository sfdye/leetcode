class ExamRoom:
    def dist(self, x, y):
        if x == -1:
            return -y
        elif y == self.N:
            return -(self.N - 1 - x)
        else:
            return -(abs(x - y) // 2)

    def __init__(self, N):
        self.N = N
        self.pq = [(self.dist(-1, N), -1, N)]

    def seat(self):
        _, x, y = heapq.heappop(self.pq)
        if x == -1:
            seat = 0
        elif y == self.N:
            seat = self.N - 1
        else:
            seat = (x + y) // 2
        heapq.heappush(self.pq, (self.dist(x, seat), x, seat))
        heapq.heappush(self.pq, (self.dist(seat, y), seat, y))
        return seat

    def leave(self, p):
        head = tail = None
        for interval in self.pq:
            if interval[1] == p:
                tail = interval
            if interval[2] == p:
                head = interval
            if head and tail:
                break
        self.pq.remove(head)
        self.pq.remove(tail)
        heapq.heapify(self.pq)
        heapq.heappush(self.pq, (self.dist(head[1], tail[2]), head[1], tail[2]))
