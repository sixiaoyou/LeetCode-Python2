'''LeetCode 7:Reverse Integer
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
注意点：int的范围，输入输出都要注意
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        list=[]
        sum=0
        z=0
        x=1234
        if x>=-2**31 and x<=2**31-1:
          if x > 0:
            while True:
              y=x%10
              x=x/10
              z+=1
              list.append(y)
              if x==0:
                  break
            for j in list:
              if z > 0:
                #if j != 0
                 sum+=j*10**(z-1)
                 z=z-1
            if sum >= -2 ** 31 and sum <= 2 ** 31 - 1:
               return sum
            else:
               return 0
          else:
            while True:
              y=-x%10
              x=-(-x/10)
              z+=1
              list.append(y)
              if -x==0:
                  break
            for j in list:
              if z > 0:
                sum-=j*10**(z-1)
                z=z-1
              if -sum >= -2 ** 31 and -sum <= 2 ** 31 - 1:
                return sum
              else:
                return 0
        else:
            return  0