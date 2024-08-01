# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l1 = head.next
        if not l1 or not l1.next:
            return head
        l = 1
        t = head
        while t.next:
            l += 1
            t = t.next
        l2_last = t
        t = head
        l = l//2
        while l:
            t = t.next
            l -= 1
        l2 = t.next
        t.next = None
        l2_t = l2
        while l2_t != l2_last:
            x = l2_last.next
            t = l2_t.next
            l2_last.next = l2_t
            l2_t.next = x
            l2_t = t
        l2 = l2_last
        t = head
        while l1 and l2:
            l1_t = l1.next
            l2_t = l2.next
            t.next = l2
            l2.next = l1
            t = l1
            l1 = l1_t
            l2 = l2_t
        return head

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
# a6 = ListNode(6)
# a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a5
a = Solution().reorderList(a1)