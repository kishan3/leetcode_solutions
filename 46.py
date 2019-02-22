class Solution:
    def __init__(self):
        self.result = []

    def permute_(self, nums, left, right):

        if left == right:
            c_n = [ele for ele in nums]
            self.result.append(c_n)
        else:
            for i in range(left, right + 1):
                nums[left], nums[i] = nums[i], nums[left]
                self.permute_(nums, left + 1, right)
                nums[left], nums[i] = nums[i], nums[left]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        left = 0
        right = length - 1
        self.permute_(nums, left, right)
        return self.result
