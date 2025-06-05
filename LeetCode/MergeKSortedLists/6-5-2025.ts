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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {

    // Time Complexity:  O(nlog n)
    // Space Complexity: O(n)

    // Verifies there is a list to work with
    if (lists.length === 0) return null;

    let nodesArray: ListNode[] = [];

    // Adds all individual nodes from the lists to the array
    lists.forEach((node) => {
        while (node) {
            nodesArray.push(node);
            node = node.next;
        }
    });

    // Sorts the node in ascending value
    nodesArray.sort((node1, node2) => node1.val - node2.val);

    // If nodesArray is empty, sets resultNode to null
    let resultNode = nodesArray[0] ?? null;

    // Sets each node to the following one in the array
    nodesArray.forEach((node, index, array) => {
        // If the array is defined at that index, sets it to the node, otherwise null
        node.next = array[index + 1] ?? null;
    });
    
    return resultNode;
};
