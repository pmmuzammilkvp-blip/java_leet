import java.util.*;

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        
        if(lists == null || lists.length == 0) return null;

        PriorityQueue<ListNode> pq = new PriorityQueue<>(
            (a, b) -> a.val - b.val
        );

        // add first node of each list
        for(ListNode node : lists) {
            if(node != null) {
                pq.add(node);
            }
        }

        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;

        while(!pq.isEmpty()) {

            ListNode node = pq.poll();
            current.next = node;
            current = current.next;

            if(node.next != null) {
                pq.add(node.next);
            }
        }

        return dummy.next;
    }
}
