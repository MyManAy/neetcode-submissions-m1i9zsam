# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            merged = ListNode(list1.val, None)
            list1 = list1.next
        elif list2.val < list1.val:
            merged = ListNode(list2.val, None)
            list2 = list2.next
        saved = merged
        while list1 and list2:
            if list1.val <= list2.val:
                merged.next = list1
                merged = merged.next
                list1 = list1.next
            elif list2.val < list1.val:
                merged.next = list2
                merged = merged.next
                list2 = list2.next
        if list1:
            merged.next = list1
        elif list2:
            merged.next = list2
        
        return saved