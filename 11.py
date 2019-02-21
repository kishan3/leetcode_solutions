class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height.insert(0, 0)
        # print height
        maxA = 0
        st = 1
        en = len(height) - 1
        while st < en:
            # print height[st]
            # print height[en]
            area = min(height[en], height[st]) * (en - st)
            if maxA < area:
                maxA = area
            if height[st] < height[en]:
                st += 1
            else:
                en -= 1
        return maxA