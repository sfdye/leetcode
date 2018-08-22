class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        prev = 0
        ans = [0] * n
        for log in logs:
            job, op, time = log.split(":")
            job, time = int(job), int(time)
            if op == "start":
                if stack:
                    ans[stack[-1]] += time - prev
                stack.append(job)
                prev = time
            else:
                ans[stack.pop()] += time - prev + 1
                prev = time + 1
        return ans
