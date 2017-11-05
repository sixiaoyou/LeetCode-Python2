'''

【极客学院版】
LeetCode142. Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        else:
            slow = head
            fast = head
            while fast!=None and fast.next!=None:
                slow = slow.next
                fast = fast.next
                fast = fast.next
                if slow == fast:
                    break
            if fast == None or fast.next == None:
                return None
            else:
                slow = head
                while fast!=slow:
                    slow = slow.next
                    fast = fast.next
                return fast