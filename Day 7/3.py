class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mxSum(root):
    if not root:
        return 0

    lt = max(0, mxSum(root.left))
    rt = max(0, mxSum(root.right))
    curr = max(lt, rt)+root.data
    mx = max(curr, root.data+lt+rt)
    mxSum.mx = max(mxSum.mx, mx)
    return curr

#  BT:
#        5
#      /  \
#    2     7
#  /  \   / \
# 1    3 5   9

root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(9)

mxSum.mx = float("-inf")
mxSum(root)
print(mxSum.mx)
