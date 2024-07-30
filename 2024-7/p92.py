# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if left == 1:
            left_pre = ListNode(0)
            left_pre.next = head
        else:
            left_pre = head
        for i in range(left - 2):
            left_pre = left_pre.next
        left0 = left_pre.next
        if left0:
            left1 = left0.next
            left0.next = None
        else:
            left1 = None
        if left1:
            left2 = left1.next
        else:
            left2 = left1
        for i in range(right - left):
            left1.next = left0
            left0 = left1
            left1 = left2
            if left1:
                left2 = left1.next
            else:
                left2 = left1
        if left_pre.next:
            left_pre.next.next = left1
        left_pre.next = left0
        if left == 1:
            return left_pre.next
        else:
            return head

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a6 = ListNode(6)
a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a5
a = Solution().reverseBetween(a1,1,2)
print(a.val)