'''
LeetCode 20: Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

#【极客学院版】
class SolutionV1(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) % 2 != 0:
            return False
        else:
            stack = []
            for i in s:
                if i == '(' or i == '[' or i == '{':
                    stack.append(i)
                else:
                    if i == ')':
                        if stack == [] or stack[-1] != '(':
                            return False
                        else:
                            stack.pop()
                    elif i == ']':
                        if stack == [] or stack[-1] != '[':
                            return False
                        else:
                            stack.pop()
                    elif i == '}':
                        if stack == [] or stack[-1] != '{':
                            return False
                        else:
                            stack.pop()
            return stack == []


class SolutionV2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype:
        """
        ok = True
        if len(s) % 2 != 0:
            ok = False
        dict = {}
        for i in xrange(len(s)):
            dict[s[i]] = i
            print i, dict
            if "(" in dict and ")" in dict:
                away = dict[")"] - dict["("]
                if away % 2 == 0:
                    ok = False
                dict.pop(")")
                dict.pop("(")
            if "[" in dict and "]" in dict:
                away = dict["]"] - dict["["]
                if away % 2 == 0:
                    ok = False
                dict.pop("[")
                dict.pop("]")
            if "{" in dict and "}" in dict:
                away = dict["}"] - dict["{"]
                if away % 2 == 0:
                    ok = False
                dict.pop("{")
                dict.pop("}")
        if s.count("(") != s.count(")"):
            ok = False
        if s.count("[") != s.count("]"):
            ok = False
        if s.count("{") != s.count("}"):
            ok = False
        return ok