class Node:
    def __init__(self, val=  None, next_node = None):
        self.value = val
        self.next_node = next_node # the pointer initially points to nothing

    def set_next(self, new_node):
        self.next_node = new_node


class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def find(self,data):
        i = 0
        while self.head:
            if data == self.head.value:
                print(i)
                return True
            else:
                i += 1
                self.head = self.head.next_node
        print ("Data not in the linked list ")
        return False

    def delete(self,data):
        # Find first
        found = False
        previous = None
        current = self.head
        while current and found is False:
            if data == current.value:
                found = True
            else:
                previous = current
                current = current.next_node

        if current is None:
            return "Data not in the list"

        if previous is None:
            self.head = current.next_node()

        else:
            print ("Deleted")
            previous.set_next(current.next_node)

    def size(self):
        current = self.head
        size = 0
        while current:
            size +=1
            current = current.next_node
        return size



a = LinkedList()
a.insert(5)
a.insert(3)
a.insert(13)
a.insert(12)
a.insert(32)
print(a.size())
print(a.delete(3))
print(a.size())