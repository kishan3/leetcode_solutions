class Solution(object):

    @staticmethod
    def median(arr, length):
        if length == 0:
            return -1
        if length % 2 == 0:
            return (arr[length / 2] + arr[length / 2 - 1]) / 2
        else:
            return arr[length / 2]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            elif nums1[i] == nums2[j]:
                result.append(nums1[i])
                result.append(nums2[j])
                i += 1
                j += 1
            else:
                result.append(nums2[j])
                j += 1
        if len(nums1[i:]) > 0:
            result.extend(nums1[i:])
        elif len(nums2[j:]) > 0:
            result.extend(nums2[j:])
        length = len(result)
        print result
        if length % 2 == 0:
            return (result[length / 2] + result[length / 2 - 1]) / 2.0
        else:
            return result[length / 2]
