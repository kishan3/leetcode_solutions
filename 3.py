class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = i
        ans = 0
        n = len(s)
        hash_set = set()
        while i < n and j < n:
            if s[j] not in hash_set:
                hash_set.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                hash_set.remove(s[i])
                i += 1
        return ans, s[i:j]
