class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], K: int) -> List[int]:
        s = 0
        w = []
        for i in range(len(nums)):
            s += nums[i]
            if i >= K:
                s -= nums[i - K]
            if i >= K - 1:
                w.append(s)
        max_i = 0
        left = [0] * len(w)
        for i in range(len(w)):
            if w[i] > w[max_i]:
                max_i = i
            left[i] = max_i
        right = [0] * len(w)
        max_i = len(w) - 1
        for i in range(len(w) - 1, -1, -1):
            if w[i] >= w[max_i]:
                max_i = i
            right[i] = max_i
        ans = None
        for j in range(K, len(w) - K):
            i, k = left[j - K], right[j + K]
            if not ans or w[i] + w[j] + w[k] > w[ans[0]] + w[ans[1]] + w[ans[2]]:
                ans = i, j, k
        return ans
