'''
【极客学院版】
LeetCode111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    global min

    def order(self, p, level):
        global min
        if p != None:
            if p.left == None and p.right == None:
                if min > level:
                    min = level
            self.order(p.left, level + 1)
            self.order(p.right, level + 1)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        global min
        min = float("inf")
        self.order(root, 1)
        return min