# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If head is empty return nothing
        if head == None:
            return
        temp = head
        # Check to see if the current val is none or if the next val is none end the while loop
        while (temp and temp.next):
            # Check the current value to the next value
            # If the value are the same skip the next value
            if (temp.val == temp.next.val):
                temp.next = temp.next.next
            # If the next value is not the same as current, proceed to the next value
            else :
                temp = temp.next
        # Return the head from the beginning
        return head