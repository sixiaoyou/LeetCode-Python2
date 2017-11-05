class Solution(object):
    def removeDuplicates(self, nums,size):
        """
        :type nums: List[int]
        :type size:int
        :rtype: int
        """
        if len(nums)<size+1:
            return len(nums)
        else:
            j,k=size,size
            while(j<len(nums)):
                if nums[j]!=nums[k-size]:
                    nums[k]=nums[j]
                    k+=1
                j+=1
            return k