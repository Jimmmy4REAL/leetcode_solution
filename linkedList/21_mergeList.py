# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # merge into one sorted list
        # compare the two pointer
        curr = dummy = ListNode()
        # return dummy.next
        while list1 and list2: # only one - > curr.next = remain_list
            # assign curr.next value
            # compare the two list_val
            if list1.val >= list2.val: # put in list2
                curr.next = list2
                # update the two pointer
                curr = curr.next
                list2 = list2.next
            else:
                curr.next = list1
                # update the two pointer
                curr = curr.next
                list2 = list1.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        return dummy.next