'''
LeetCode 258:Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def result(num):
            sum = 0
            list = []
            global final
            if num > 0 and num <= 2 ** 31 - 1:
                while True:
                    y = num % 10
                    num = num / 10
                    list.append(y)
                    if num == 0:
                        break
                for i in list:
                    sum += i
                if sum < 10:
                    final = sum
                else:
                    result(sum)
            else:
                final = 0
            return final
        return result(num)
