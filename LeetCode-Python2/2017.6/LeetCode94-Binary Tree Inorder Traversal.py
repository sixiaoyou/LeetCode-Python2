'''
【极客学院版】
LeetCode94. Binary Tree Inorder Traversal
 Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrder(self, p):
        if p != None:
            self.inOrder(p.left)
            res.append(p.val)
            self.inOrder(p.right)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        global res
        self.inOrder(root)
        return res
