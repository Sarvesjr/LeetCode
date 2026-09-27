# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        Recursive Method:
        
        if head is None or head.next is None:
            return head
        newHead=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return newHead
        """

        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev