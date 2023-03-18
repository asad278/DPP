class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def topView(root, hd, lvl, mp):
    if not root:  return
    if hd not in mp:
        mp[hd] = [root.data, lvl]
    elif(mp[hd][1]>lvl):
        mp[hd] = [root.data, lvl]
    topView(root.left, hd-1, lvl+1, mp)
    topView(root.right, hd+1, lvl+1, mp)

def bottomView(root, hd, lvl, mp):
    if not root: return
    if hd in mp:
        if lvl>=mp[hd][1]:
            mp[hd] = [root.data, lvl]
    else:
        mp[hd] = [root.data, lvl]
    bottomView(root.left, hd-1, lvl+1, mp)
    bottomView(root.right, hd+1, lvl+1, mp)        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

mp = dict()
hd = lvl = 0
topView(root, hd, lvl, mp)
print("Top View:")
for i in sorted(mp.keys()):
    print(mp[i][0], end=" ")

mp.clear()
hd = lvl = 0
bottomView(root, hd, lvl, mp)
print("\nBottom View:")
for i in sorted(mp.keys()):
    print(mp[i][0], end=" ")
