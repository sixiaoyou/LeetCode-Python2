'''
 LeetCode234-Palindrome Linked List
 Given a singly linked list, determine if it is a palindrome.

 Follow up:
 Could you do it in O(n) time and O(1) space?
'''

from ListNode import ListNode



class Solution(object):
    def getLength(self,head):
        n = 0
        while head != None:
            head = head.next
            n += 1
        return n


    def judgeProcess(self,head,p2):
        pre = p2.next
        p4 = p2.next.next
        while p4 != None:
            next = p4.next
            p4.next = pre
            pre = p4
            p4 = next
        p2.next.next = None
        p2.next = pre
        while pre != None:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n=self.getLength(head)
        p2 = head.next
        count = 0
        if n % 2 == 0:
            if n == 2:
                if head.val == head.next.val:
                    return True
                else:
                    return False
            while 2 + count != n / 2:
                p2 = p2.next
                count += 1
        else:
            if n == 1:
                return True
            while count != n / 2 - 1:
                p2 = p2.next
                count += 1
        return self.judgeProcess(head,p2)











