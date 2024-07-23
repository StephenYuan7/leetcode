# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            len_a = 0
            temp_a = headA
            while temp_a.next:
                len_a = len_a + 1
                temp_a = temp_a.next
            len_b = 0
            temp_b = headB
            while temp_b.next:
                len_b = len_a + 1
                temp_b = temp_b.next
            temp_a = headA
            temp_b = headB
            if len_a >= len_b:
                for i in range(len_a - len_b):
                    temp_a = temp_a.next
            else:
                for i in range(len_b - len_a):
                    temp_b = temp_b.next
            while temp_a and temp_b and temp_a != temp_b:
                temp_a = temp_a.next
                temp_b = temp_b.next
            return temp_a