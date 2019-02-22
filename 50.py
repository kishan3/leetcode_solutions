class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        pow = self.myPow(x, n / 2)

        if n % 2 == 0:
            return pow * pow

        return x * pow * pow
