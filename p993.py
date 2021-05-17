
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        r = [root]
        while len(r)>0:
            a = []
            for i in r:
                if i.left:
                    a.append(i.left)
                if i.right:
                    a.append(i.right)
                if i.left and i.right:
                    if(i.left.val==x and i.right.val==y)or(i.left.val==y and i.right.val==x):
                        return False
            b = []
            for i in a:
                b.append(i.val)
            c = (x in b) + (y in b)
            if c == 2:
                return True
            elif c == 1:
                return False
            r = a[:]
        return True