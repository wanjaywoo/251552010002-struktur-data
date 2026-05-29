class binarynode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
root = binarynode("A")
root.left = binarynode("B")
root.right = binarynode("C")
root.left.left = binarynode("D")
root.left.right = binarynode("E")
def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)
print("binary tree - preorder traversal:")
preorder(root)