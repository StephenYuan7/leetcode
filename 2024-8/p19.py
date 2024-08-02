# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        t = slow
        while fast:
            fast = fast.next
            t = slow
            slow = slow.next
        if slow == head:
            return slow.next
        else:

            t.next = slow.next

            return head


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
# a5 = ListNode(5)
# a6 = ListNode(6)
a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a2
a = Solution().removeNthFromEnd(a1, 1)
pass