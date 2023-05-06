/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
  public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    
    // Time Complexity:  O(n)
    // Space Complexity: O(n)

    // ListNode thats points to a node before the start of new merged list
    ListNode dummy = new ListNode(0);
    // ListNode that points to the tail of merged list
    ListNode tail = dummy;
	  
    // Goes through both list1 and list2 until the end of one of them is reached
    while (list1 != null && list2 != null) {

      // If list1.val is less than list2.val, list1 is the next node to merge
      if (list1.val < list2.val) {
        tail.next = list1;
        list1 = list1.next; 
      // If list2.val is less than or equal to list1.val, list2 is the next node to merge
      } else {
        tail.next = list2;
        list2 = list2.next;
      }

      tail = tail.next;
    }

    // If list1 has ended, rest of merged list is equal to list 2
    if (list1 == null) {
      tail.next = list2;
    // If list2 has ended, rest of merged list is equal to list 1
    } else {
      tail.next = list1;
    }

    // Dummy next should equal the start of merged list
    return dummy.next;
    }
  }
