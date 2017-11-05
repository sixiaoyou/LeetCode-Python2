'''
LeetCode 61. Rotate List
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#【极客学院版】
class Solution(object):
    def getLength(self, head):
        n = 0
        p = head
        while p != None:
            p = p.next
            n += 1
        return n

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k == 0:
            return head
        n = self.getLength(head)
        if k >= n:
            k %= n
        if k == 0:
            return head
        pre = head
        index = 1
        while index < n - k:
            pre = pre.next
            index += 1
        start = pre.next
        last = start
        while last.next != None:
            last = last.next
        pre.next = None
        last.next = head
        return start
