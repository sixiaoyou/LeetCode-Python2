'''
LeetCode 202:Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        exist = []
        def result(n):
            sum = 0
            global final
            final = False
            list = []
            exist.append(n)
            if n > 0 and n <= 2 ** 31 - 1:
                while True:
                    y = n % 10
                    n = n / 10
                    list.append(y)
                    if n == 0:
                        break
                for i in list:
                    sum += i ** 2
                if sum == 1:
                    final = True
                    return final
                elif sum in exist:
                    return final
                else:
                    exist.append(sum)
                    result(sum)
            else:
                return final
            return final
        return result(n)