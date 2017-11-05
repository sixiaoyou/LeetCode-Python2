'''
LeetCode661. Image Smoother
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
'''
#【网友实现】:http://bookshadow.com/weblog/2017/08/21/leetcode-image-smoother/
class Solution(object):
    def imageSmootherV1(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        dx, dy = [-1, 0, 1], [-1, 0, 1]
        w, h = len(M), len(M[0])
        N = []
        for x in range(w):
            row = []
            for y in range(h):
                nbs = [M[x + i][y + j] for i in dx for j in dy \
                       if 0 <= x + i < w and 0 <= y + j < h]
                row.append(sum(nbs) / len(nbs))
            N.append(row)
        return N


    def imageSmootherV2(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        lm = len(M)
        ln = len(M[0])
        N = [[0] * ln for i in range(lm)]
        for i in range(len(M)):
            li = len(M[i])
            for j in range(li):

                if i == 0:
                    if j == 0:
                        if j == li - 1:
                            if i == lm - 1:
                                return M
                            else:
                                N[i][j] = (M[i][j] + M[i + 1][j]) / 2
                        else:
                            if i == lm - 1:
                                N[i][j] = (M[i][j] + M[i][j + 1]) / 2
                            else:
                                N[i][j] = (M[i][j] + M[i][j + 1] + M[i + 1][j] + M[i + 1][j + 1]) / 4
                    elif j == li - 1:
                        if i == lm - 1:
                            N[i][j] = (M[i][j] + M[i][j - 1]) / 2
                        else:
                            N[i][j] = (M[i][j] + M[i][j - 1] + M[i + 1][j] + M[i + 1][j - 1]) / 4
                    else:
                        if i == lm - 1:
                            N[i][j] = (M[i][j] + M[i][j - 1] + M[i][j + 1]) / 3
                        else:
                            N[i][j] = (M[i][j] + M[i][j - 1] + M[i][j + 1] + M[i + 1][j] + M[i + 1][j - 1] + M[i + 1][
                                j + 1]) / 6
                elif i == lm - 1:
                    if j == 0:
                        if li == 1:
                            N[i][j] = (M[i][j] + M[i - 1][j]) / 2
                        else:
                            N[i][j] = (M[i][j] + M[i][j + 1] + M[i - 1][j] + M[i - 1][j + 1]) / 4
                    elif j == li - 1:
                        N[i][j] = (M[i][j] + M[i][j - 1] + M[i - 1][j] + M[i - 1][j - 1]) / 4
                    else:
                        N[i][j] = (M[i][j] + M[i][j - 1] + M[i][j + 1] + M[i - 1][j] + M[i - 1][j - 1] + M[i - 1][
                            j + 1]) / 6
                else:
                    if j == 0:
                        if li == 1:
                            N[i][j] = (M[i][j] + M[i - 1][j] + M[i + 1][j]) / 3
                        else:
                            N[i][j] = (M[i][j] + M[i][j + 1] + M[i + 1][j] + M[i + 1][j + 1] + M[i - 1][j] + M[i - 1][
                                j + 1]) / 6
                    elif j == li - 1:
                        N[i][j] = (M[i][j] + M[i][j - 1] + M[i + 1][j] + M[i - 1][j] + M[i + 1][j - 1] + M[i - 1][
                            j - 1]) / 6
                    else:
                        N[i][j] = (M[i][j] + M[i][j - 1] + M[i][j + 1] + M[i + 1][j] + M[i + 1][j - 1] + M[i + 1][
                            j + 1] + M[i - 1][j] + M[i - 1][j - 1] + M[i - 1][j + 1]) / 9
        return N

