# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 1 2 3 4 5 n == 2 >> 1 2 3 5
        dummy = ListNode()
        dummy.next = head
        slow,fast = dummy,dummy
        while n > 0:
            # update fast pointer first
            fast = fast.next
            n -= 1
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        # update slow pointer
        slow.next = slow.next.next

        return dummy.next


def print_linked_list(head):
    # Helper function to print the linked list
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

one = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
print_linked_list(Solution.removeNthFromEnd(one,2))