'''
LeetCode 219：Contains Duplicate II
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype
        """
        class Solution(object):
            def containsNearbyDuplicate(self, nums, k):
                """
                :type nums: List[int]
                :type k: int
                :rtype: bool
                """
                dict={}
                ok=False
                for i in xrange(len(nums)):
                    if nums[i] not in dict:
                        dict[nums[i]]=i
                    else:
                        if i-dict[nums[i]]<=k:
                            ok=True
                        else:
                            dict[nums[i]]=i
                return ok