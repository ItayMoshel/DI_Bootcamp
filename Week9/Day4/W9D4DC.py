class Node:
    def __init__(self, left, right, value):
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