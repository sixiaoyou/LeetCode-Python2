'''
LeetCode92:Reverse Linked List II
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''
from ListNode import ListNode


# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next==None:
            return head
        elif m==n:
            return head
        else:
            start = ListNode(0)
            first = start
            start.next=head
            k = 1
            while k < m :
                first=first.next
                k+=1
            pre = first.next
            p = pre.next
            next = None
            top = first.next
            while k < n:
                next = p.next
                p.next = pre
                pre = p
                p = next
                k+=1
            top.next =p
            first.next = pre
            return start.next




