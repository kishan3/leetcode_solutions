# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy=ListNode(0)
        curr=dummy
        p=l1
        q=l2

        while p!=None and q!=None:
            digit = p.val+q.val

            curr.next = ListNode(carry+(digit%10))
            carry=digit/10
            curr=curr.next
            p=p.next
            q=q.next
        if carry:
            curr.next=ListNode(carry)
        return dummy.next
