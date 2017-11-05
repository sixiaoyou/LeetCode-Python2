'''
LeetCode566:Reshape the Matrix

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
'''


import numpy as np
import itertools

#网友实现：https://discuss.leetcode.com/topic/87899/python-solutions
class SolutionV1(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums

#网友实现：https://discuss.leetcode.com/topic/87899/python-solutions
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        it = itertools.chain(*nums)
        return [list(itertools.islice(it, c)) for _ in xrange(r)]

#网友实现:https://discuss.leetcode.com/topic/87851/java-concise-o-nm-time
class SolutionV3(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m=len(nums[0])
        nums1=[[[] for i in range(c)]for i in range (r)]
        if r * c != len(nums) * m:
            return nums
        else:
            for i in range(len(nums)*m):
                nums1[i/c][i%c]=nums[i/m][i%m]
        return nums1


class SolutionV4(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        listLength=len(nums)
        elementLength=len(nums[0])
        nums1=[]
        nums2=[]
        count=1
        if r*c==listLength*elementLength:
            for i in range(len(nums)):
                for j in range(len(nums[i])):
                    nums1.append(nums[i][j])
                    if count%c==0:
                        nums2.append(nums1)
                        nums1=[]
                    count+=1
            return nums2
        else:
            return nums


