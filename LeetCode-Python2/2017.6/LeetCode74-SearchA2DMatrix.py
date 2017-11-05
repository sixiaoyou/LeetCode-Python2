'''
【极客学院版】
LeetCode74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution(object):
    def searchRow(self, matrix, m, n, target):
        start = 0
        end = m - 1
        while start <= end:
            mid = (start + end) / 2
            if target == matrix[mid][n - 1]:
                return mid
            elif target < matrix[mid][n - 1]:
                end -= 1
            else:
                start += 1
        return start

    def searchCol(self, matrix, row, n, target):
        start = 0
        end = n - 1
        while start <= end:
            mid = (start + end) / 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                end -= 1
            else:
                start += 1
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        row = self.searchRow(matrix, m, n, target)
        if row < 0 or row >= m:
            return False
        return self.searchCol(matrix, row, n, target)
