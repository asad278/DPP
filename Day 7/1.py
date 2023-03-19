class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, tar):
    if not root:        return False
    if tar==root.data:  return True
    elif tar>root.data: return search(root.right, tar)
    else:               return search(root.left, tar)

def insertNode(root, key):
    if not root: return Node(key)
    else:
        if root.data == key: return root
        elif root.data<key:  root.right = insertNode(root.right, key)
        else:                root.left = insertNode(root.left, key)
    return root

def deleteNode(root, key):
    if not root:
        return root
 
    if key<root.data:
        root.left = deleteNode(root.left, key)
        return root
    elif key>root.data:
        root.right = deleteNode(root.right, key)
        return root
 
    if not root.left and not root.right:
        return None
 
    if not root.left:
        temp = root.right
        root = None
        return temp
    elif not root.right:
        temp = root.left
        root = None
        return temp
 
    node = root
    next = root.right
    while next.left:
        node = next
        next = next.left
    if node!=root: node.left=next.right
    else:          node.right=next.right
    root.data = next.data
    return root

root = Node(1)
root = insertNode(root, 2)
root = insertNode(root, 3)
root = insertNode(root, 4)
root = insertNode(root, 5)
root = insertNode(root, 6)
print(search(root, 6))
root = deleteNode(root, 6)
print(search(root, 6))