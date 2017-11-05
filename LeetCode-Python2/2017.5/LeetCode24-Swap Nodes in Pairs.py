'''
【极客学院版】
LeetCode24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

from ListNode import ListNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            start = ListNode(0)
            zero = start
            pre = head
            p = pre.next
            next = None
            start.next = head
            while p != None and pre != None:
                next = p.next
                p.next = pre
                pre.next = next
                zero.next = p
                if next == None:
                    break
                else:
                    zero = pre
                    pre = next
                    p = pre.next
            return start.next
