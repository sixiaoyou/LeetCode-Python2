'''
LeetCode 263:Ugly Number
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''
class SolutionV1(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<1:
            return False
        elif num == 1:
            return True
        else:
            if num%2!=0 and num%3!=0 and num%5!=0:
                return False
            else:
                nums = [2, 3, 5]
                list = []
                while num%2== 0 or num%3==0 or num%5==0:
                    if num%2==0:
                        num = num / 2
                        list.append(num)
                    elif num%3==0:
                        num = num / 3
                        list.append(num)
                    else:
                        num=num/5
                        list.append(num)
                for i in list:
                    if i not in nums and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i != 1:
                        return False
                return True

#网友实现：http://bookshadow.com/weblog/2015/08/19/leetcode-ugly-number/
class SolutionV2(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        else:
            for i in [2, 3, 5]:
                while num % i == 0:
                    num /= i
            return num == 1