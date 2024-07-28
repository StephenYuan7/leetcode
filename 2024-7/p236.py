
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        def lowest(r, x):
            if r is None:
                return []
            if r == x:
                return [x]
            left = lowest(r.left, x)
            if left:
                left.append(r)
                return left
            right = lowest(r.right, x)
            if right:
                right.append(r)
                return right
            return []


        p_parent = lowest(root, p)
        q_parent = lowest(root, q)
        i = 0
        for i in range(len(p_parent)):
            if i >= len(q_parent):
                return q_parent[-i]
            if p_parent[-i-1] != q_parent[-i-1]:
                return p_parent[-i]
        return p_parent[0]



tree3 = TreeNode(3)
tree5 = TreeNode(5)
tree1 = TreeNode(1)
tree6 = TreeNode(6)
tree2 = TreeNode(2)
tree0 = TreeNode(0)
tree8 = TreeNode(8)
tree7 = TreeNode(7)
tree4 = TreeNode(4)
tree3.left = tree5
tree5.left = tree6
tree1.left = tree0
tree3.right = tree1
tree5.right = tree2
tree1.right = tree8
tree2.left = tree7
tree2.right = tree4
x = Solution().lowestCommonAncestor(tree3,tree5,tree4)
print(x.val)