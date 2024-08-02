# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        if head:
            fast = head.next
        else:
            return None
        slow = head
        total = 1
        while fast != slow:
            if fast and fast.next:
                fast = fast.next
            else:
                return None
            if fast and fast.next:
                fast = fast.next
            else:
                return None
            slow = slow.next
            total += 1
        circle = 1
        fast = fast.next
        while slow != fast:
            circle += 1
            fast = fast.next
        head_t = head
        circle_t = circle

        while 1:
            for i in range(total - circle):
                head_t = head_t.next
            t = head_t.next
            for i in range(circle):
                if t == head_t:
                    return head_t
                t = t.next
            circle_t = max(1, circle_t // 2)
            for i in range(circle_t):
                fast = fast.next
            total = 1
            t = head_t
            while t != fast:
                t = t.next
                total += 1


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
a = Solution().detectCycle(a1)
pass