'''
LeetCode56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    #【网友实现】
    def mergeV1(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        container = sorted(intervals, key=lambda x: x.start)
        for interval in container:
            if not ans:
                ans.append(interval)
            else:
                pre = ans[-1]
                if pre.end >= interval.start:
                    pre.end = max(pre.end, interval.end)
                else:
                    ans.append(interval)
        return ans

class SolutionV2(object):
   def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals,key = lambda interval:(interval.start,interval.end))
        length = len(intervals)
        count = 0
        for i in range(length):
            mark = True
            i =max(0,i-count)
            while i+1 < length and intervals[i].end >= intervals[i+1].end:
                del intervals[i+1]
                length-=1
                if mark:
                    count+=1
                    mark = False
            if i+1 < length and intervals[i].end >= intervals[i+1].start:
                intervals[i].end = intervals[i+1].end
                del intervals[i+1]
                length -= 1
                count+=1
        return intervals
