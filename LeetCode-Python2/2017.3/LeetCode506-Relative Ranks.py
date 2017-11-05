'''
LeetCode 506:Relative Ranks
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''
#V1
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums1=copy.deepcopy(nums)
        nums1.sort()
        nums1.reverse()
        nums2=["Gold Medal","Silver Medal","Bronze Medal"]
        dict={}
        for i in range(len(nums1)):
            if i>=3:
                dict[nums1[i]]=str(i+1)
            else:
                dict[nums1[i]] = nums2[i]
        for j in range(len(nums)):
                nums[j]=dict[nums[j]]
        return nums

#V2
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dmap = {v : k for k, v in enumerate(sorted(nums, reverse=True))}
        return [str(dmap[n] + 1) \
               if dmap[n] > 2 \
               else ['Gold', 'Silver', 'Bronze'][dmap[n]] + ' Medal' for n in nums]