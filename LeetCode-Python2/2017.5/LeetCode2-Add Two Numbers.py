#-*-coding:utf-8-*-

'''
【九章算术实现】:http://www.jiuzhang.com/solutions/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        ptr=head
        carry=0
        while True:
            if l1!=None:
                carry+=l1.val
                l1=l1.next
            if l2!=None:
                carry+=l2.val
                l2=l2.next
            ptr.val = carry%10
            carry/=10

            if l1!=None or l2!=None or carry!=0:
                ptr.next=ListNode(0)
                ptr=ptr.next
            else:
                break
        return head



if __name__=="__main__":
    idx = ListNode(2)
    n = idx
    n.next = ListNode(4)
    n = n.next
    n.next = ListNode(3)
    n = n.next

    idx1 = ListNode(5)
    n = idx1
    n.next = ListNode(6)
    n = n.next
    n.next = ListNode(4)
    n = n.next

    a=Solution()
    b=a.addTwoNumbers(idx,idx1)
    while b!=None:
        print b.val
        b=b.next


