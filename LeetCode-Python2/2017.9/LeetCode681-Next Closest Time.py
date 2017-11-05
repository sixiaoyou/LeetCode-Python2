'''
【Python3代码不变,故此Python2代码可做参考】
LeetCode681. Next Closest Time
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
'''
class Solution(object):
    def getIndex(self, i, array):
        index = 0
        for j in range(len(array)):
            if array[j] == i:
                index = j
        return index

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        numbers = []
        for i in time:
            if i != ':':
                numbers.append(int(i))
        numbers.sort()
        lt = list(time)
        temp1 = self.getIndex(int(lt[-1]), numbers)
        if temp1 != 3:
            lt[-1] = str(numbers[temp1 + 1])
            return "".join(lt)
        else:
            lt[-1] = str(numbers[0])
            temp2 = self.getIndex(int(lt[-2]), numbers)
            if temp2 != 3 and numbers[temp2 + 1] < 6:
                lt[-2] = str(numbers[temp2 + 1])
                return "".join(lt)
            else:
                lt[-2] = str(numbers[0])
                temp3 = self.getIndex(int(lt[1]), numbers)
                if temp3 != 3:
                    if int(lt[0]) != 2 or numbers[temp3 + 1] < 5:
                        lt[1] = str(numbers[temp3 + 1])
                        return "".join(lt)
                lt[1] = str(numbers[0])
                if numbers[0] < numbers[1] and numbers[1] < 3:
                    lt[0] = str(numbers[1])
                return "".join(lt)
