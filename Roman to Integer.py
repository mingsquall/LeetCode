"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

基本字符：
I、V、X、L、C、D、M
相应的阿拉伯数字：
1．5、10、50、100、500、1000

(1)相同的数字连写，所表示的数等于这些数字相加得到的数，如：Ⅲ = 3；
(2)小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数， 如：Ⅷ = 8；Ⅻ = 12；
(3)小的数字，（限于Ⅰ、X 和C）在大的数字的左边，所表示的数等于大数减小数得到的数，如：Ⅳ= 4；Ⅸ= 9；

"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0

        for i in range(0, len(s)):
            sum = sum + map[s[i]]
            if i > 0 and map[s[i - 1]] < map[s[i]]:
                # 因为本来应该减去这个小的数，但是上一次循环还加了一次，于是这次就减去2次
                sum = sum - 2 * map[s[i]]

        return sum

