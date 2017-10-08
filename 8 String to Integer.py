"""
8. String to Integer (atoi)
"""
class Solution:
	def aToi(self, str):
		str = str.strip()
		n = len(str)
		flag = 1
		i = 0
		result = 0

		if  i < n and str[i] == '+':
			i += 1
		elif i < n and str[i] == '-':
			flag = -1
			i += 1

		while i < n:
			if str[i].isdigit():
				# overflow & underflow
				if result > 214748364 or (result == 214748364 and int(str[i]) >= 8):
					if flag == 1:
						return 2147483647
					else:
						return -2147483648
				result = result * 10 + int(str[i])
				i += 1
			else:
				break
		return result * flag

if __name__ == '__main__':
	s = Solution()
	print(s.aToi('+1234w34'))
	print(s.aToi('   456er12'))
	print(s.aToi('789 123'))
	print(s.aToi('09911111111711'))
