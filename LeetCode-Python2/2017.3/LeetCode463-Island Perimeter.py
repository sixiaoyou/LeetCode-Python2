'''
LeetCode 463:Island Perimeter
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''
grid=[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
# V1:
class Solution(object):
     def islandPerimeter(self, grid):
         """
         :type grid: List[List[int]]
         :rtype: int
         """
         sum=0
         if len(grid)<=100:
             if len(grid)==1:
                 for i in xrange(len(grid)):
                    for j in xrange(len(grid[i])):
                        if len(grid)==1 and len(grid[i])==1:
                            return 4
                        if grid[i][j]==1 and j==0:
                            if grid[i][j+1]==0:
                                sum+=1
                            sum+=3
                        elif grid[i][j]==1 and j==len(grid[i])-1:
                            if grid[i][j-1]==0:
                                sum+=1
                            sum+=3
                        elif grid[i][j]==1:
                            if grid[i][j-1]==0:
                                sum+=1
                            if grid[i][j+1]==0:
                                sum+=1
                            sum+=2
                 return sum
             else:
                 for i in xrange(len(grid)):
                     for j in xrange(len(grid[i])):
                         if len(grid[i])==1:
                             if i==0 and grid[i][j]==1:
                                 if grid[i+1][j]==0:
                                     sum+=1
                                 sum+=3
                             elif i==len(grid)-1 and grid[i][j]==1:
                                 if grid[i-1][j]==0:
                                     sum+=1
                                 sum+=3
                             elif grid[i][j]==1:
                                 if grid[i-1][j]==0:
                                     sum+=1
                                 if grid[i+1][j]==0:
                                     sum+=1
                                 sum+=2
                         elif i==j==0 and grid[i][j]==1:
                             if grid[i][j+1]==0:
                                 sum+=1
                             if grid[i+1][j]==0:
                                 sum+=1
                             sum+=2
                         elif i==0 and j==len(grid[i])-1 and grid[i][j]==1:
                             if grid[i][j-1]==0:
                                 sum+=1
                             if grid[i+1][j]==0:
                                 sum+=1
                             sum+=2
                         elif i==len(grid)-1 and j==0 and grid[i][j]==1:
                             if grid[i-1][j]==0:
                                 sum+=1
                             if grid[i][j+1]==0:
                                 sum+=1
                             sum+=2
                         elif i==len(grid)-1 and j==len(grid[i])-1 and grid[i][j]==1:
                             if grid[i-1][j]==0:
                                 sum+=1
                             if grid[i][j-1]==0:
                                 sum+=1
                             sum+=2
                         elif i==0 and j>0 and j<len(grid[i])-1 and grid[i][j]==1:
                             if grid[i + 1][j] == 0:
                                 sum += 1
                             if grid[i][j + 1] == 0:
                                 sum += 1
                             if grid[i][j - 1] == 0:
                                 sum += 1
                             sum += 1
                         elif i == len(grid)-1 and j > 0 and j < len(grid[i]) - 1 and grid[i][j]==1:
                             if grid[i - 1][j] == 0:
                                 sum += 1
                             if grid[i][j + 1] == 0:
                                 sum += 1
                             if grid[i][j - 1] == 0:
                                 sum += 1
                             sum += 1
                         elif j==0 and i>0 and i<len(grid)-1 and grid[i][j]==1 :
                             if grid[i - 1][j] == 0:
                                 sum += 1
                             if grid[i][j + 1] == 0:
                                 sum += 1
                             if grid[i+1][j]==0:
                                 sum+=1
                             sum+=1
                         elif j==len(grid[i])-1 and i > 0 and i<len(grid)-1 and grid[i][j]==1:
                             if grid[i - 1][j] == 0:
                                 sum += 1
                             if grid[i][j - 1] == 0:
                                 sum += 1
                             if grid[i + 1][j] == 0:
                                 sum += 1
                             sum += 1
                         elif i > 0 and i<len(grid)-1 and j>0 and j<len(grid[i])-1:
                             if grid[i][j] == 1 and grid[i - 1][j] == 0:
                                 sum += 1
                             if grid[i][j] == 1 and grid[i][j - 1] == 0:
                                 sum += 1
                             if grid[i][j] == 1 and grid[i + 1][j] == 0:
                                 sum += 1
                             if grid[i][j] == 1 and grid[i][j+1] == 0:
                                 sum+=1
                 return sum
#-----------------------------------------------------------------------------------------------------------------------
#V2:
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total=0
        for i in xrange(len(grid)):
                for j in xrange(len(grid[i])):
                    if grid[i][j]==1:
                        total+=4
                        if len(grid)==1 and len(grid[i])==1:
                            return 4
                        elif len(grid)==1 and j<len(grid[i])-1 and grid[i][j+1]==1:
                            total-=2
                        elif len(grid[i])==1 and i<len(grid)-1 and grid[i+1][j]==1:
                            total-=2
                        elif i==len(grid)-1 and j<len(grid[i])-1 and grid[i][j+1]==1:
                            total-=2
                        elif j==len(grid[i])-1 and i<len(grid)-1 and grid[i+1][j]==1:
                            total-=2
                        elif j<len(grid[i])-1 and i<len(grid)-1:
                            if grid[i][j+1]==1:
                                total-=2
                            if grid[i+1][j]==1:
                                total-=2
        return total
#-----------------------------------------------------------------------------------------------------------------------
#V3:
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h=len(grid)
        w=len(grid[0]) if h else 0
        sum=0
        for i in xrange(h):
            for j in xrange(w):
                if grid[i][j]==1:
                    sum+=4
                    if i>0 and grid[i-1][j]:
                        sum-=2
                    if j>0 and grid[i][j-1]:
                        sum-=2
        return sum

