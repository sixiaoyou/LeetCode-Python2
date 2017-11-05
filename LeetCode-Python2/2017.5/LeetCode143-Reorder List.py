'''
【极客学院版】
LeetCode143. Reorder List
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''



from ListNode import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getLength(self, head):
        n = 0
        while head != None:
            head = head.next
            n += 1
        return n

    def reverseListNode(self, p):
        pre = p.next
        p1 = p.next.next
        while p1 != None:
            next = p1.next
            p1.next = pre
            pre = p1
            p1 = next
        p.next.next = None
        p.next = None
        return pre

    def reorderProcess(self, head, pre):
        start = ListNode(0)
        start.next = head
        first = head
        flag = True
        next = None
        while pre != None:
            if flag:
                next = first.next
                first.next = pre
                first = next
            else:
                next = pre.next
                pre.next = first
                pre = next
            flag=not flag
        return head

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head != None and head.next != None and head.next.next != None:
            n = self.getLength(head)
            p = head
            half = n / 2
            if n % 2 != 0:
                half += 1
            for i in range(1, half):
                p = p.next
            head = self.reorderProcess(head, self.reverseListNode(p))