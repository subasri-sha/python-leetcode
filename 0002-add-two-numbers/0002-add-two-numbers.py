# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode() # new linked list
        temp = dummy # stores the result list
        carry = 0 # Initialize carry to 0

        while (l1 != None or l2 != None) or carry: # This loop runs as long as at least one of these is true
            sum = 0 # Resets the sum for this loop iteration.
            if l1 != None: # Checks if the first linked list still has nodes left.
                sum += l1.val # Adds the current digit from list l1 to sum.
                l1 = l1.next # Moves the l1 pointer to the next node for the next iteration.
            if l2 != None: # Checks if the second linked list still has nodes left.
                sum += l2.val # Adds the current digit from list l2 to sum.
                l2 = l2.next # Moves l2 pointer to the next node.
                sum += carry # Adds the carry from the previous addition to the sum.
                carry = sum // 10
                node = ListNode(sum % 10)
                temp.next = node
                temp = temp.next
        return dummy.next




