'''
LeetCode 350:Intersection of Two Arrays II
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

#V1
class Solution1(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums=list(set(nums1).intersection(set(nums2)))
        nums3=[]
        for i in nums:
            if nums1.count(i) >0 and nums2.count(i)>0:
                count=nums1.count(i) if nums1.count(i)<=nums2.count(i) else nums2.count(i)
                for j in range(count):
                    nums3.append(i)
        return nums3





#V2
import copy
class Solution2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3=[]
        index=-1
        shortNums=copy.deepcopy(nums1) if len(nums1) <= len(nums2) else nums2
        longNums=copy.deepcopy(nums2) if len(nums2)>= len(nums1) else nums1
        shortNums.sort()
        longNums.sort()
        for i in shortNums:
            for j in range(len(longNums)):
                if i==longNums[j] and j>index:
                    index=j
                    nums3.append(i)
                    break
        return nums3



#V3
import collections


class Solution4(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3 = []
        countNums1 = collections.Counter(nums1)
        countNums2 = collections.Counter(nums2)
        for i in countNums1.keys():
            if countNums2[i]!=0:
                count = countNums1[i] if countNums1[i] <= countNums2[i] else countNums2[i]
                for j in range(count):
                    nums3.append(i)
        return nums3


#V4
import collections


class Solution4(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3 = []
        countNums1 = collections.Counter(nums1)
        countNums2 = collections.Counter(nums2)
        for i in countNums1.keys():
            if countNums1[i] != 0:
                count = countNums1[i] if countNums1[i] <= countNums2[i] else countNums2[i]
                nums3.append([i] * count)
#网友实现
        return [y for x in nums3 for y in x]

#V5(网友实现)
class Solution5(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1,nums2=sorted(nums1),sorted(nums2)
        p1=p2=0
        ans=[]
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]<nums2[p2]:
                p1+=1
            elif nums1[p1]>nums2[p2]:
                p2+=1
            else:
                ans.append(nums1[p1])
                p1+=1
                p2+=1
        return ans

#V6（网友实现)
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1,nums2=nums2,nums1
        ans=[]
        c=collections.Counter(nums1)
        for x in nums2:
            if c[x]>0:
                ans.append(x)
                c[x]-=1
        return ans