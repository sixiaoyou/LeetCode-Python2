'''
LeetCode 442:Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''
nums=[4,3,2,7,8,2,3,1]
dict={}
list=[]
for i in nums:
    if i not in dict:
        dict[i]=i
    else:
        list.append(i)
print list
