# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def delete(self,node):
        # Set VALUE and POINTER
        node.val = node.next.val
        node.next = node.next.next


 # Remove Nth Node From End of List