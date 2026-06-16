# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        if not head or not head.next:
            return

        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode

        # merge two halves
        first, second = head, prev
        while second:
            firstNext, secondNext = first.next, second.next
            first.next = second
            second.next = firstNext
            first, second = firstNext, secondNext
