'''
【Python3代码不变，故此Python2代码可做参考】
LeetCode565. Array Nesting
A zero-indexed array A consisting of N different integers is given. The array contains all integers in the range [0, N - 1].

Sets S[K] for 0 <= K < N are defined as follows:

S[K] = { A[K], A[A[K]], A[A[A[K]]], ... }.

Sets S[K] are finite for each K and should NOT contain duplicates.

Write a function that given an array A consisting of N integers, return the size of the largest set S[K] for this array.

Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
Note:
N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of array A is an integer within the range [0, N-1].
'''
#【网友实现】:http://bookshadow.com/weblog/2017/05/28/leetcode-array-nesting/
class SolutionV1(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        def search(number):
            count = 0
            while nums[number]>=0:
                next=nums[number]
                nums[number]=-1
                number=next
                count+=1
            return count
        for i in range(len(nums)):
            if nums[i]>=0:
                ans=max(ans,search(i))
        return ans


class SolutionV2(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict ={}
        list = []
        for i in range(len(nums)):
            count = 0
            a = i
            while a not in dict and i>=0:
                dict[a] = nums[a]
                next=nums[a]
                nums[a]=-1
                a=next
                count+=1
            list.append(count)
        return max(list)