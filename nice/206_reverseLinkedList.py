class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        # Customize the representation to display the value of the node
        return f"ListNode({self.val})"
class Solution(object):
    def reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1 - 2 - 3
        # 2 -> 1  3
        #   -----> 

        # 3 -> 2 -> 1
        prev, curr = None, head
        while curr:
            tmp = curr.next # final edge case would stand for 'None'
            curr.next = prev
            # move two pointer together
            prev = curr
            curr = tmp
        return prev
    
    def reverseList1(self,head): # recursive function
        # recursion 
        if not head:
            return None
        # modify connection Then deeper recursion
        newHead = head
        if head.next:
            newHead = self.reverseList1(head.next)
            head.next.next = head
        head.next = None
        return newHead

def print_linked_list(head):
    # Helper function to print the linked list
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

node = ListNode(1, ListNode(2, ListNode(3, None)))
reversed_head = Solution.reverseList1(self,node)
print_linked_list(reversed_head)  # Output: 3 -> 2 -> 1 -> None