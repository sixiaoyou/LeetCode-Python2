'''
Leet551. Student Attendance Record I
You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False

'''


class SolutionV1(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        countA = 0
        countL = 0
        index = -1
        for i in range(len(s)):
            if s[i] == 'A':
                countA+=1
            if countA > 1:
                return False
            if s[i] == 'L':
                if index == -1:
                    index = i
                elif i - index == 1:
                    countL+=1
                    index = i
                else:
                    index=i
                    countL = 0
            if countL>1:
                return False
        return True


class SolutionV2(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return list(s).count('A')<=1 and not "LLL" in s