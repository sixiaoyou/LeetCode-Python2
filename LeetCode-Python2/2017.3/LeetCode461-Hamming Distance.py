'''
LeetCode 461:Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
 0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.




Subscribe to see which companies asked this question.

'''
class SolutionV1(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')

class SolutionV2(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x >= 0 and x < 2 ** 31 and y >= 0 and y < 2 ** 31:
            list1 = []
            z = x ^ y
            list1 = list(bin(z))
            return list1.count('1')

