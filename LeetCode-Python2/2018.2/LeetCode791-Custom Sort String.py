'''
【Python3代码不变，故可参照此Python2代码】
LeetCode791. Custom Sort String
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.


Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
'''
import collections


class SolutionV1(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        ls = list(S)
        dict = {}
        for i in T:
            if i in ls:
                if i not in dict:
                    index = ls.index(i)
                    ls = ls[:index]+T.count(i)*[i]+ls[index+1:]
                    dict[i] = i
            else:
                ls.append(i)
        return  "".join(ls)

# 【网友实现】http://bookshadow.com/weblog/2018/02/25/leetcode-weekly-contest-73/
class SolutionV2(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        counterT = collections.Counter(T)
        ans = ''
        for c in S:
            ans += c * counterT[c]
            del counterT[c]
        return ans + ''.join(k * v for k, v in counterT.items())