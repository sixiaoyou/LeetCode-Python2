'''
LeetCode231. Power of Two
Given an integer, write a function to determine if it is a power of two.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
'''

Java:
public class Solution {
    public boolean isPowerOfTwo(int n) {
        boolean ok=false;
        for(int i=-32;i<32;i++)
        {
            if (Math.pow(2,i)==n){
                ok=true;
            }
        }
        return ok;
    }
}

Python:
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict={}
        ok=False
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]=2
                ok=True
        return ok