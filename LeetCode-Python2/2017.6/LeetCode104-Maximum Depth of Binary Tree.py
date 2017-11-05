'''
【极客学院】
 LeetCode104. Maximum Depth of Binary Tree
 Given a binary tree, find its maximum depth.

 The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    global max1

    def order(self, p, level):
        global max1
        if p != None:
            if p.left == None and p.right == None:
                if max1 < level:
                    max1 = level
            self.order(p.left, level + 1)
            self.order(p.right, level + 1)
        return max1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global max1
        max1 = 0
        return self.order(root, 1)











