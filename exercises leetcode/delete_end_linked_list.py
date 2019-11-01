class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None and n == 1:
            return None

        p1 = head
        for i in range(n - 1):
            if p1.next is not None:
                p1 = p1.next
            else:
                return None

        n_ptr = head
        prev = None
        while p1.next is not None:
            p1 = p1.next
            prev = n_ptr
            n_ptr = n_ptr.next

        if n_ptr == head:
            temp = head
            head = head.next
            temp = None
        else:
            prev.next = n_ptr.next
            n_ptr = None
        return head