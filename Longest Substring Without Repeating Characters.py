"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = maxLength = 0
        dic = {}

        for i in range(len(s)):
            # head不能往前移动
            if s[i] in dic and head <= dic[s[i]]:
                head = dic[s[i]] + 1
            # 更新index
            dic[s[i]] = i
            maxLength = max(maxLength, i - head + 1)

        return maxLength

s = Solution()
print(s.lengthOfLongestSubstring('abba'))
