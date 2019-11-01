class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current != None:
            current = current.next
        current.next = new_node

    def length(self):
        length = 0
        current = self.head
        while current.next is not None:
            length += 1
            current = current.next
        return length

    def delete_node(self, data):
        # Find it first
        current = self.head

        while current.value != data:
            current = current.next

        if current is None:
            return "No value found"

        else:
            current.next = current.next.next
            current = current.next
