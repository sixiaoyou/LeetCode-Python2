'''
LeetCode209. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''
# 网友实现
class SolutionV1(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        ans = len(nums)+1
        subsum = 0
        for i in xrange(len(nums)):
            subsum += nums[i]
            while subsum >= s:
                length = i-left+1
                if ans > length:
                    ans = length
                subsum -= nums[left]
                left += 1
        if ans == len(nums)+1:
            ans = 0
        return ans

class SolutionV2(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start, end, count, ln, min = 0, 0, 1, len(nums), float("Inf")
        if ln == 0:
            return 0
        sum = nums[0]
        while start < ln:
            if sum < s:
                if end < ln - 1:
                    end += 1
                else:
                    break
                sum += nums[end]
                count += 1
            else:
                if count < min:
                    min = count
                if end == ln - 1 and sum <= s:
                    return min
                while sum >= s:
                    sum -= nums[start]
                    count -= 1
                    if sum >= s and min > count:
                        min = count
                    start += 1
                if end < ln - 1:
                    end += 1
                    sum += nums[end]
                    count += 1
        return [0, min][min < ln]



