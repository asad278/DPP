import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def leftView(root, view, lvl):
    if not root:
        return
    if lvl==len(view):
        view.append(root.data)
    leftView(root.left, view, lvl+1)
    leftView(root.right, view, lvl+1)

def rightView(root, view, lvl):
    if not root:
        return
    if lvl==len(view):
        view.append(root.data)
    rightView(root.right, view, lvl+1)
    rightView(root.left, view, lvl+1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

view = []
leftView(root, view, 0)
print(view)
view.clear()
rightView(root, view, 0)
print(view)
