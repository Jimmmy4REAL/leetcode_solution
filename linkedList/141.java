/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        // have fast and slow pointer - > nodes_num can be 0
        if (head == null || head.next == null){
            return false;
        }
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode fast = dummy, slow = dummy;
        while (fast!=null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow){
                return true;
            }
        }
        return false;
    }
}