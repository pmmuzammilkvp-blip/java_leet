class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode prevGroup = dummy;
        
        while(true) {
            
            ListNode kth = getKthNode(prevGroup, k);
            if(kth == null) break;
            
            ListNode groupNext = kth.next;
            
            // reverse group
            ListNode prev = groupNext;
            ListNode curr = prevGroup.next;
            
            while(curr != groupNext) {
                ListNode temp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = temp;
            }
            
            ListNode temp = prevGroup.next;
            prevGroup.next = kth;
            prevGroup = temp;
        }
        
        return dummy.next;
    }
    
    private ListNode getKthNode(ListNode curr, int k) {
        while(curr != null && k > 0) {
            curr = curr.next;
            k--;
        }
        return curr;
    }
}
