class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # try:
        #     return nums.index(target)
        # except ValueError:
        #     return -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) / 2

            if target == nums[middle]:
                return middle
            if nums[left] <= nums[middle]:  # first half is sorted
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:  # second half is sortde
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1
