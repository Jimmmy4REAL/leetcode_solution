package linkedList;

public /**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
//Use three pointers and so you can change the next of the mid to the first one without losing the track of the original left.
//Iterative version
class Solution {

    public ListNode reverseList(ListNode head) {
        ListNode current = head;
        ListNode previous = null;
        ListNode nextCurrent = null;
    
        while (current != null) {
            nextCurrent = current.next;
            current.next = previous;
            previous = current;
            current = nextCurrent;
        }

        return previous;
    }
}

//Recursive version
// class Solution {

//     public ListNode reverseList(ListNode head) {
//         return rev(head, null);
//     }

//     public ListNode rev(ListNode node, ListNode pre) {
//         if (node == null) return pre;
//         ListNode temp = node.next;
//         node.next = pre;
//         return rev(temp, node);
//     }
// }
 {
    
}
