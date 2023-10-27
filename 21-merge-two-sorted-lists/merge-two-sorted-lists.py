# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = current = ListNode()
        # Do this while both list 1 and list 2 have items
        while list1 and list2:
            # Whichever list has the smaller number, get put onto the merged list
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else :
                current.next = list2
                list2 = list2.next
            current = current.next
        # Add in the rest of list1 or list2 once the other list is empty
        current.next = list1 or list2
        return mergedList.next

        