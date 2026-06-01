# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative Solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        prevNode = None
        currNode = head

        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        return prevNode

# Recursive Solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity:  O(1)
        # Space Complexity: O(n)
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head
