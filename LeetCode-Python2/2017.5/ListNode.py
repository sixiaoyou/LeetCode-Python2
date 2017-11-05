# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def arrayToList(self,list):
        head = ListNode(0)
        p = head
        for i in list:
            p.next = ListNode(i)
            p = p.next
        return head.next