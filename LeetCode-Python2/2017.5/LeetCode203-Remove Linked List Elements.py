'''
LeetCode203:Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#【极客学院】版
class SolutionV1(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start=ListNode(0)
        pre=start
        p=head
        start.next=head
        while p!=None:
            if p.val==val:
                pre.next=p.next
                p=p.next
            else:
                pre=pre.next
                p=p.next
        return start.next

#【网友实现】:http://bookshadow.com/weblog/2015/04/24/leetcode-remove-linked-list-elements/
class SolutionV2(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start=ListNode(0)
        p=start
        start.next=head
        while p and p.next:
            if p.next.val==val:
                p.next = p.next.next
            else:
                p=p.next
        return start.next


