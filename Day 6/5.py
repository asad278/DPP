import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def verticalOrder(root, hd, mp):
    if not root:
        return
    try:
        mp[hd].append(root.data)
    except:
        mp[hd]=[root.data]
    verticalOrder(root.left, hd-1, mp)
    verticalOrder(root.right, hd+1, mp)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

mp = dict()
hd = 0
verticalOrder(root, hd, mp)
for i, v in enumerate(sorted(mp)):
    for j in mp[v]:
        print(j, end=" ")
    print()
