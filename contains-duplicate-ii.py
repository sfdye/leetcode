class T:
    def __init__(self, num, pos):
        self.num = num
        self.pos = pos

    def __str__(self):
        return 'num={}, pos={}'.format(self.num, self.pos)

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        a = [T(num,index) for index,num in enumerate(nums)]
        a.sort(key=lambda x: (x.num, x.pos))

        for i in range(len(a)-1):
            if a[i].num == a[i+1].num and a[i+1].pos-a[i].pos <= k:
                return True

        return False
