# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Two-Pointer Solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False


# Hash Solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        nodeSet = set()

        while head:
            if head in nodeSet:
                return True
            nodeSet.add(head)
            head = head.next

        return False
