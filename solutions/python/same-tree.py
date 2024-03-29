# Author: Kyoshi Noda
# Link: https://leetcode.com/problems/same-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p,q):
    if not p and not q:
        return True
    
    if p and q and p.val == q.val:
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
    else:
        return False