class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        st1 = str(x)
        return st1[::-1] == st1