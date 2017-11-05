'''
LeetCode274. H-Index
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''
#【网友实现】:http://bookshadow.com/weblog/2015/09/03/leetcode-h-index/
class SolutionV1(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        cnts = [0] * (N + 1)
        for c in citations:
            cnts[[c, N][c > N]] += 1
        sums = 0
        for h in range(N, 0, -1):
            if cnts[h] + sums >= h:
                return h
            sums += cnts[h]
        return 0


class SolutionV2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations == []:
            return 0
        citations.sort()
        max1 = 0
        for i in range(len(citations)):
            max1 = max(max1, min(citations[i], len(citations) - i))
        return max1
