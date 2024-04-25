/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    
    // Time Complexity: O(N)
    // Space Complexity: O(1)

    // If head is invalid, return head
    if (head == NULL) {
        return head;
    }
    
    // lead is used to stay n ahead of follow,
    // allows the finding of the Nth node from the end in one pass
    // temp is used in freeing node memory
    struct ListNode *lead, *follow, *temp;
    lead = follow = head;
    temp = NULL;

    // Puts lead n ahead of follow
    for (int i = 0; i < n; i++) lead = lead->next;

    // Checks if lead has reached end of list, if it has
    // the node to be removed is the head
    if (!lead) {
        temp = head, head = head->next;
        free(temp), temp = NULL;
        return head;
    }

    // Continues advancing lead and follow until end of list
    while(lead->next) lead = lead->next, follow = follow->next;

    // Removes nth node and sets list properly
    temp = follow->next, follow->next = follow->next->next;
    free(temp), temp = NULL;
    return head;
}
