# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t = head
        n = head
        x = 1
        i = 0
        while n:
            n = n.next
            i = i + 1
            if n == t:
                return True
            if i == x:
                x += 1
                i = 0
                t = n
        return False