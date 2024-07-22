# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        list3 = 0
        list1_temp = list1
        list2_temp = list2
        if list1.val <= list2.val:
            list3 = list1
            list1_temp = list1.next
        else:
            list3 = list2
            list2_temp = list2.next
        list3_temp = list3
        while list1_temp or list2_temp:
            if not list1_temp:
                list3_temp.next = list2_temp
                break
            if not list2_temp:
                list3_temp.next = list1_temp
                break
            if list1_temp.val <= list2_temp.val:
                list3_temp.next = list1_temp
                list3_temp = list1_temp
                list1_temp = list1_temp.next
            else:
                list3_temp.next = list2_temp
                list3_temp = list2_temp
                list2_temp = list2_temp.next
        return list3