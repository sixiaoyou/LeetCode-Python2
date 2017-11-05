'''
LeetCode82:Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionV1(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            start=ListNode(0)
            pre=start
            p=head
            next=None
            start.next=head
            while p!=None and p.next!=None:
                next=p.next
                if p.val==next.val:
                    while next!=None and next.val==p.val:
                        next=next.next
                    p=next
                    pre.next=next
                else:
                    pre=p
                    p=p.next
            return start.next


class SolutionV2(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            start=ListNode(0)
            pre=start
            p=head
            flag=0
            start.next=head
            while p!=None:
                if p.next==None:
                  if flag==1:
                    pre.next=p.next
                  p=p.next
                  break
                if p.val==p.next.val:
                    flag=1
                elif flag==1:
                    pre.next=p.next
                    flag=0
                else:
                    pre=pre.next
                p=p.next
            if pre==start:
                return start.next
            return start.next