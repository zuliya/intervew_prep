class Node:

    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        # checking if the insert has been already called to eliminate duplicates
        if self.value == data:
            return False

        # check if the value we try to insert is less then a current node.
        elif self.value > data:
            # check if node already has a left child
            if self.leftChild:

                # insert into a left child
                return self.leftChild.insert(data)
            else:
                # add new node as a left child to the current node
                self.leftChild = Node(data)
                return True

        else:
            # checks if node already has right child
            if self.rightChild:

                # inserts as a right child to a right child
                return self.rightChild.insert(data)
            else:
                # add new node as a Right child to a current node
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            # Root -> Left -> Right
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            # Left -> Right -> Root
            if self.leftChild:
                print(self.value)
                self.leftChild.postorder()
            if self.rightChild:
                print(self.value)
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            # Left -> Root -> Right
            if self.leftChild:
                self.leftChild.inorder()
            if self.rightChild:
                self.rightChild.inorder()



class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Checks if the root exists and calls recursively
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        # If there is no root means no value
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()

bst = Tree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

bst.postorder()
bst.preorder()
bst.inorder()
