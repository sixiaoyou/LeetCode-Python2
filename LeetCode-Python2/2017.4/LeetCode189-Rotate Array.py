'''
【极客学院版】
LeetCode189:Rotate Array
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II
'''




class Solution(object):
    t = -1

    def swap(self, nums, a, b):
        t = nums[a]
        nums[a] = nums[b]
        nums[b] = t

    def reverse(self, nums, start, end):
        if nums is None or len(nums) <= 1:
            return
        n = len(nums)
        i = start
        j = end
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        n = len(nums)
        if k >= len(nums):
            k = k % n
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)