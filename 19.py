# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        end = dummy
        count = 0
        while (count < n):
            if end.next:
                end = end.next
                count += 1
            else:
                return

        while end.next:
            start = start.next
            end = end.next
        start.next = start.next.next

        # This is important if first element of the node was removed. we shift
        # head to next node.
        if start == dummy:
            head = head.next
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        return result
