'''
LeetCode19:Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.


'''



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


#【极客学院版
class SolutionV1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None:
            return head
        else:
            p1=head
            p2=head
            for i in range(1,n+2):
                if p2==None:
                    return head.next
                p2=p2.next
            while p2!=None:
                p1=p1.next
                p2=p2.next
            p1.next=p1.next.next
            return head


#【网友实现】：https://discuss.leetcode.com/topic/7031/simple-java-solution-in-one-pass/2
class SolutionV2(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start=ListNode(0)
        slow=start
        fast=start
        slow.next=head
        for i in range(1,n+2):
            fast=fast.next
        while fast!=None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return start.next

#【极客学院版】
class SolutionV3(object):
    def getLength(self, head):
        m = 0
        while head != None:
            m += 1
            head = head.next
        return m

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        m = self.getLength(head)
        if head == None:
            return head
        elif head.next == None or m == n:
            head = head.next
            return head
        else:
            p = head
            for i in range(1, m - n):
                p = p.next
            p.next = p.next.next
        return head