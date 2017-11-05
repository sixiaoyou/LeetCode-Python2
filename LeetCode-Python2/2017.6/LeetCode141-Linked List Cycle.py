'''
【极客学院版】
 LeetCode141. Linked List Cycle
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        else:
            slow = head
            fast = head
            while fast!=None and fast.next!=None:
                slow = slow.next
                fast = fast.next
                fast = fast.next
                if slow == fast:
                    return True
            return False