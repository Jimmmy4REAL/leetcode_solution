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
    public void reorderList(ListNode head) {


        // find half point - can both start from dummyNode
        ListNode slow = head;
        ListNode fast = head.next;
        while(fast != null && fast.next !=null){
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // reverse second half
        // slow.next is the second half
        ListNode curr = slow.next;
        slow.next =null;
        ListNode secondHead = helper(curr);
        // one by one connected - > head and secondHead
        // 1 - 2
        // 5 - 4 - 3
        // 1-5-2-4-3
        ListNode first = head;
        while (secondHead != null){
            // store laterVal
            ListNode tmp1 = first.next;
            ListNode tmp2 = secondHead.next;
            first.next = secondHead;
            secondHead.next = tmp1;
            first = tmp1;
            secondHead = tmp2;
        }

    }
    public ListNode helper(ListNode head){
        ListNode prev = null;
        ListNode tmp = null;
        while (head != null){
            tmp = head.next;
            head.next = prev;
            // update pointer
            prev = head;
            head = tmp;
        }
        return prev;
    }
}