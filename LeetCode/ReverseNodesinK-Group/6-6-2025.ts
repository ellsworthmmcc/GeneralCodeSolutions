/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    
    // Time Complexity:  O(n^2)
    // Space Complexity: O(1)

    // Verifies there is a list to manipulate
    if (head == null || k <= 1) return head;

    // Dummy head to hold list start
    const dummy: ListNode = new ListNode(0, head);
    
    let currentNode: ListNode | null = dummy;
    let nextNode: ListNode | null = dummy;
    let previousNode: ListNode | null = dummy;

    let count: number = 0;


    // Retrieves the list length, 
    // necessary not to reverse portions of the list that do not need to be
    while (currentNode.next != null) {
        currentNode = currentNode.next;
        count++;
    }
    
    // Goes through the list until every subsection has been reversed
    while (count >= k) {

        currentNode = previousNode.next;
        nextNode = currentNode.next;

        for (let i = 1; i < k; i++) {
            // Performs the swap
            currentNode.next = nextNode.next;
            nextNode.next = previousNode.next;
            previousNode.next = nextNode;
            // Sets nextNode correctly
            nextNode = currentNode.next;
        }

        previousNode = currentNode;
        count -= k;
    }

    return dummy.next;
};
