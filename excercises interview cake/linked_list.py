# Delete a node from a singly linked list

class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def delete_node(self, value):
        current = self.head
        previous = None
        found = False

        while current is not None and found is False:
            if self.head == value:
                found = True
            else:
                previous = current
                current = current.next

        #     if the node is in the beginning of the list
        if previous is None:
            self.head = self.head.next

        if found is False:
            return "Matching node is not found"

        current.next = current.next.next
        current = current.next

    # Delete a node from a singly-linked list, ↴ given only a variable pointing to that node.
    def delete_using_variable_pointer(self,var):
        return self.head


    def reverse_linked_list(self):
        current = self.head
        length = 0
        while current.next is not None:
            length +=1
            current = current.next

        for i in range(length//2):
            current_node = self.head
            previous_node = None
            next_node = None

            next_node = current_node.next

            current_node = previous_node

            previous_node = current_node
            current_node = next_node

#         do 1st run to find out how many we need to do

#         then -1 until its halved is achieved


1 2 3 4 5

2 1 3 4 5
3 2 1 4 5
