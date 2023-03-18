import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def lvlord(root, lvl):
    if root is None:
        return
    q = []
    q.append(root)
    while len(q)>0:
        lvl.append(q[0].data)
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

lvl = []
lvlord(root, lvl)
print(lvl)
