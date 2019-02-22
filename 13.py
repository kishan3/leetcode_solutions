class Solution(object):
    def value(self, r):
        if r == "I":
            return 1
        if r == "V":
            return 5
        if r == "X":
            return 10
        if r == "L":
            return 50
        if r == "C":
            return 100
        if r == "D":
            return 500
        if r == "M":
            return 1000

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0

        while i < len(s):
            v1 = self.value(s[i])

            if i + 1 < len(s):
                v2 = self.value(s[i + 1])

                if v1 >= v2:
                    res += v1
                    i += 1
                else:
                    res = res + v2 - v1
                    i += 2
            else:
                res += v1
                i += 1
        return res
