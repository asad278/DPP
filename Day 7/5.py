class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lca(root, n1, n2):
    if not root: return None
    if root.data==n1 or root.data==n2:
        return root
    lt = lca(root.left, n1, n2)
    rt = lca(root.right, n1, n2)
    if lt and rt: return root
    return lt if lt else rt

#  BT:
#        5
#      /  \
#    2     7
#  /  \   / \
# 1    3 5   9

root = Node(5)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(7)
root.right.left = Node(5)
root.right.right = Node(9)

print(lca(root, 3, 9).data)
