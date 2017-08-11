class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return ' '.join(s.split()[::-1])
        return ' '.join(reversed(s.split()))
s = Solution()
print(s.reverseWords('I love u'))
