class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        data = {'{': '}',
                '[': ']',
                '(': ')'
                }

        for i in s:
            if i in data.keys():
                stack.append(i)
            else:
                if len(stack) > 0:
                    x = stack.pop()
                    if data[x] == i:
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
