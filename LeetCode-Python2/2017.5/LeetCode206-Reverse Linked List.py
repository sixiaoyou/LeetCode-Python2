'''
【极客学院版】
LeetCode206:Reverse Linked List
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#非递归
class SolutionV1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        else:
            pre=head
            p=head.next
            next=None
            while p != None:
                next=p.next
                p.next=pre
                pre=p
                p=next
            head.next=None
            return pre


#递归
class SolutionV2(object):
    def recursive(self, p):
        if p.next == None:
            return p
        else:
            next = p.next
            tail = self.recursive(next)
            next.next = p
            return tail

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            tail = self.recursive(head)
            head.next = None
            return tail