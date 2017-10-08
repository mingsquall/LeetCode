"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""
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

class Solution1(object):
    def reverseWords(self, s):
        i = 0
        result = ''
        for j in range(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                if i < j:
                    result = s[i:j] + ' ' + result
                i = j + 1
        return result.strip()

s = Solution1()
print(s.reverseWords('I love u'))
