import math


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        zeros_count = 0
        minus = 1
        sum_of_logs = 0
        for num in nums:
            if num < 0:
                minus *= -1
            if num == 0:
                zeros_count += 1
            else:
                sum_of_logs += math.log(abs(num))

        if zeros_count > 1:
            return [0] * len(nums)
        elif zeros_count == 1:
            ans = []
            for num in nums:
                if num != 0:
                    ans.append(0)
                else:
                    ans.append(minus * round(math.exp(sum_of_logs)))
        else:
            ans = []
            for num in nums:
                if num < 0:
                    ans.append(
                        -minus * round(math.exp(sum_of_logs-math.log(abs(num)))))
                else:
                    ans.append(
                        minus * round(math.exp(sum_of_logs-math.log(num))))
        return ans
