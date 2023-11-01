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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // slow and fast pointer
        if (head == null || head.next == null) return null;
        ListNode tmp = new ListNode(0);
        tmp.next = head;
        ListNode fast = tmp,slow = tmp;
        while (n != 0){
            fast = fast.next;
            n--;
        }

        while (fast.next!=null){
            fast = fast.next;
            slow = slow.next;
        }
        // connect the new two again
        slow.next = slow.next.next;
        return tmp.next;
    }
    
}