class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_value(self):
        return self.value

    def set_right(self, right):
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_value(self, value):
        self.value = value

    def add_node(self, node):
        if node.value < self.value:
            if not self.left:
                self.left = node
        else:
            if not self.right:
                self.right = node

root = Node(8)
print(root)

node_10 = Node(10)
root.add_node(node_10)


node_3 = Node(3)
root.add_node(node_3)
