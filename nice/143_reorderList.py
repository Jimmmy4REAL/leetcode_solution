# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 1 2 3 4 >> 1 4 2 3 
        # 1 2 || 3 4 >> 1 4 2 3
        # 1 2 3 4 5 >> 1 2 3 || 4 5 - second half starting point should be 4 >> ending point is 3
        # 1 5 2 4 3
        # find mid-half point first >> reverse second-half - > assign new val one by one into original firstPart

# edge case consideration
        dummy = ListNode()
        slow = fast = dummy.next = head
        # determine tail of first half
        while fast and fast.next:
            fast = fast.next.next # because of .next.next attribute >> has to make sure fast.next exist
            slow = slow.next
        secondHalf = slow.next
        
        slow.next = None

        # reverse the secondHalf
        # reverse LinkedList
        prev = None
        curr = secondHalf
        while curr:
            tmp = curr.next
            curr.next=prev
            # update both pointer
            prev = curr
            curr = tmp
        
        # prev is the new head of secondHalf
        # 1 2 And 4 3 combination - dummy.next and prev >> 1 4 2 3
        one,two = dummy.next,prev

        while two:
            oneNext = one.next
            twoNext = two.next
            one.next = two # assign one.next var to be two_val
            two.next = oneNext
            one = oneNext
            two = twoNext
        return dummy.next


def printListNode(head):
    curr = head
    while head:
        # print in val - > format
        print(str(head.val) + '- >')
        head = head.next
    print('None')
    return
node = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))) # 1 2 3 4 5
# 1 5 2 4 3
printListNode(Solution.reorderList(node))