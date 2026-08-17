# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow
        second_head = middle.next
        middle.next = None
        prev = None

        while second_head:
            temp_next = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = temp_next

        l1 = head
        l2 = prev

        while l2:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = l1_next
            l2 = l2_next
            l1 = l1_next
        
        return


