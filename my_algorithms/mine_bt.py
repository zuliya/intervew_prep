print("Hello World!")


class Node:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.head = None

    def inset(self, value):
        new_leaf = Node(value)
        if self.root == None:
            self.root = new_leaf
        else:
            self._insert(self.root, new_leaf)

    def _insert(self, tree_value, new_leaf):
        if new_leaf < tree_value:
            if tree_value is not None:
                self._insert(tree_value.left, new_leaf)
            else:
                tree_value.left = new_leaf
                return tree_value

        elif new_leaf > tree_value:
            if tree_value is not None:
                self._insert(tree_value.right, new_leaf)
            else:
                tree_value.right = new_leaf
                return tree_value

    # def delete(self, value):
    #     self.find(value)
    #
    # def find(self, value):
    #     current_value = self.head
    #     found_value = self._find(current_value, value)
    #
    # def _find(self,current_node, value):
    #     if current_node == value:
    #         return current_node
    #     elif current_node < value:
    #         self._find(current_node.left, value)
    #     elif current_node > value:
    #         self._find(current_node.right, value)

    # Post order Left -> Right -> Root
    #  Pre order Root -> Left -> Right
    # In order Left -> Root -> Right

    def preorder_traversal(self, root):
        # Root-> Left -> Right
        if root:
            print(root.value)
            if root.left():
                self.preorder_traversal(root.left)
            if root.right():
                self.preorder_traversal(root.right)

    def delete(self, value):
        self.find(value) = None
        found_value = self._find(current_value, value)

        if found_value.left == None:
            temp = found_value.right

    def find(self, value):
        current_value = self.head
        return self._find(current_value, value))

    def _find(current_node, value):
        if current_node == value:
            return current_node
        elif current_node < value:
            self._find(current_node.left, value)
        elif current_node > value:
            self._find(current_node.right, value)

        # Post order Left -> Right -> Root
        #  Pre order Root -> Left -> Right
        # In order Left -> Root -> Right

    # def preorder_traversal(self, root):
    #     # Root-> Left -> Right
    #     if root:
    #         print(root.value)
    #         if current_node.left():
    #             preorder_traversal(root.left)
    #         if current_node.right():
    #             preorder_traversal(root.right)



