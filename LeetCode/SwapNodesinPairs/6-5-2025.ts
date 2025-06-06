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

function swapPairs(head: ListNode | null): ListNode | null {

    // Time Complexity:  O(n)
    // Space Complexity: O(1)

    // Checks if there are any pairs to swap, if not return what was given
    if (head == null || head.next == null) return head;

    let nodeA: ListNode | null = head;
    let nodeB: ListNode | null = nodeA.next;
    let previous: ListNode | null = null;

    while(nodeA != null && nodeB != null){
        
        // Swaps the two nodes
        nodeA.next = nodeB.next;
        nodeB.next = nodeA;
        
        // If there is no previous set head to the node now at the start
        if (previous == null) {
            head = nodeB;
        } else {
            previous.next = nodeB;
        }

        // If there are no more nodes in the list, break
        if(nodeA.next == null) break;

        // Moves onto to the next pair of nodes
        nodeB = nodeA.next.next;
        previous = nodeA;
        nodeA = nodeA.next;
    }

    return head;
};
