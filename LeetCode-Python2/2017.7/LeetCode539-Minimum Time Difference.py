'''
LeetCode539. Minimum Time Difference
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
'''
import time
#【网友实现】:http://bookshadow.com/weblog/2017/03/12/leetcode-minimum-time-difference/
class SolutionV1(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        tp = sorted(map(int, p.split(':')) for p in timePoints)
        tp += [[tp[0][0] + 24, tp[0][1]]]
        return min((tp[x+1][0] - tp[x][0]) * 60 + tp[x+1][1] - tp[x][1] \
                   for x in range(len(tp) - 1))

class SolutionV2(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        convert = []
        minDiff = float("Inf")
        for i in range(len(timePoints)):
            if int(timePoints[i][:2])<12:
                convert.append(int(timePoints[i][:2])*60+int(timePoints[i][3:])+1440)
            convert.append(int(timePoints[i][:2])*60+int(timePoints[i][3:]))
        convert.sort()
        for i in range(len(convert)-1):
            minDiff = min(convert[i+1]-convert[i],minDiff)
        return minDiff