'''
【极客学院版】
LeetCode160. Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''


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

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        m = self.getLength(headA)
        n = self.getLength(headB)
        if m == 0 or n == 0:
            return None
        else:
            p = headA
            q = headB
            if m > n:
                k = m - n
                for i in range(1, k + 1):
                    p = p.next
            elif m < n:
                k = n - m
                for i in range(1, k + 1):
                    q = q.next
            while p != None or q != None:
                if p == q:
                    return p
                else:
                    p = p.next
                    q = q.next
            return None



