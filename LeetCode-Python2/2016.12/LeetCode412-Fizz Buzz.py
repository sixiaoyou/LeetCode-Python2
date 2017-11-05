'''
LeetCode 412:Fizz Buzz
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
'''
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        n=1
        list=[]
        for i in range(n+1):
           if i > 0:
               if i%3==0 and i%5!=0:
                   i="Fizz"
               elif i%5==0 and i%3!=0:
                   i="Buzz"
               elif i%5==0 and i%3==0:
                   i="FizzBuzz"
               list.append(str(i))
        return list