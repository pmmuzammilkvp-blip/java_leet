function deleteDuplicates(head) {
    let dummy = new ListNode(0);
    dummy.next = head;

    let prev = dummy; // last node before duplicates

    while (head !== null) {
        // Check if duplicate exists
        if (head.next !== null && head.val === head.next.val) {
            // Skip all nodes with same value
            while (head.next !== null && head.val === head.next.val) {
                head = head.next;
            }
            prev.next = head.next; // remove duplicates
        } else {
            prev = prev.next; // move prev if no duplicate
        }
        head = head.next;
    }

    return dummy.next;
}
