'''
注意遍历的顺序，以及提前用dict减少运算
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            inorder_root = index[preorder[preorder_left]]
            left = build(preorder_left + 1, preorder_left + inorder_root - inorder_left, inorder_left, inorder_root-1)
            right = build(preorder_left + inorder_root - inorder_left + 1, preorder_right, inorder_root + 1, inorder_right)
            return TreeNode(preorder[preorder_left], left, right)

        index = {element: i for i, element in enumerate(inorder)}
        return build(0, len(preorder)-1, 0, len(preorder)-1)
