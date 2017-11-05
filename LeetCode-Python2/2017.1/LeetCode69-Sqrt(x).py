'''
LeetCode 69:Sqrt(x)
Implement int sqrt(int x).

Compute and return the square root of x.



Subscribe to see which companies asked this question

'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low=0
        high=x
        while(low<=high):
            mid=(low+high)/2
            if (mid**2)<x:
                low=mid+1
            elif (mid**2)>x:
                high=mid-1
            else:
                return mid
        return high
