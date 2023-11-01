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
        // already sorted | nodes could be 0
        if (list1 == null && list2 == null){
            return null;
        }

        // GOOD ONE curr.next cannot go out the block
        
        // starting point - init a dummy node
        ListNode dummy = new ListNode();
        ListNode curr = dummy;
        while (list1 != null && list2 != null){
            // compare the two val and create the smaller one
            int oneVal = list1.val;
            int twoVal = list2.val;
            if (oneVal > twoVal){
                ListNode newNode = new ListNode(twoVal);
                list2 = list2.next;
                curr.next = newNode;
            }
            else{
                ListNode newNode = new ListNode(oneVal);
                list1 = list1.next;
                curr.next = newNode;
            }
            
            curr = curr.next;
        }
        // if remaining
        if (list1 != null){
            curr.next = list1;
        }else{
            curr.next = list2;
        }
        return dummy.next;
    }
}