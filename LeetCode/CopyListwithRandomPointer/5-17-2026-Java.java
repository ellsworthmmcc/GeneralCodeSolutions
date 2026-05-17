/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {

        // Time Complexity: O(n)
        // Space Complexity: O(n)

        if (head == null) return null;

        // Interweave
        Node current = head;
        while (current != null) {
            Node copy = new Node(current.val);
            copy.next = current.next;
            current.next = copy;
            current = copy.next;
        }

        // Wire random
        current = head;
        while(current != null) {
            if (current.random != null) {
                current.next.random = current.random.next;
            }
            current = current.next.next;
        }

        // Seperate
        Node newHead = head.next;
        current = head;
        while(current != null) {
            Node copy = current.next;
            current.next = copy.next;
            copy.next = copy.next != null ? copy.next.next : null;
            current = current.next;
        }

        return newHead;
    }
}
