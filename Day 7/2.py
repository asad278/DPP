class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def ceil(root, key):
    if not root: return -1
    if key == root.data: root.data
    if root.data<key:
        return ceil(root.right, key)
    c = ceil(root.left, key)
    return c if c>=key else root.data

def floor(root, key):
    if not root: return -1
    if key == root.data: root.data
    if root.data>key:
        return floor(root.left, key)
    f = floor(root.right, key)
    return f if f<=key and f!=-1 else root.data

#  BST:
#     5
#   2   7
# 1   3

root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)

print(floor(root, 4))
print(ceil(root, 4))
