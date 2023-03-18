class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def ht(root):
    if root is None: return 0
    return 1+max(ht(root.left), ht(root.right))
 
def dia(root):
    if root is None: return 0
    lht = ht(root.left)
    rht = ht(root.right)
    ldia = dia(root.left)
    rdia = dia(root.right)
    return max(lht+rht+1, max(ldia, rdia))

def sz(root):
    if root is None:  return 0
    return sz(root.left)+sz(root.right)+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height:", ht(root))
print("Size:", sz(root))
print("Diameter:", dia(root))
