# Author: Kyoshi Noda
# Link: https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
  if root is None:
    return None
  
  temp = root.left
  root.left = root.right
  root.right = temp
  
  self.invertTree(root.left)
  self.invertTree(root.right)
  return root