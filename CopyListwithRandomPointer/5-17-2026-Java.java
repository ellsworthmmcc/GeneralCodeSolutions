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

        Map<Node, Node> map = new HashMap<>();

        // First pass, creates all copied nodes
        Node current = head;
        while (current != null) {
            map.put(current, new Node(current.val));
            current = current.next;
        }

        // Second pass, wires next and random
        current = head;
        while (current != null) {
            if (current.next != null) {
                map.get(current).next = map.get(current.next);
            }
            if (current.random != null) {
                map.get(current).random = map.get(current.random);
            }
            current = current.next;
        }

        return map.get(head);
    }
}
