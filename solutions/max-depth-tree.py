def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        listAnswer = deque([root])
        level = 0

        while listAnswer:
            for x in range(len(listAnswer)):
                curr = listAnswer.popleft()
                if curr.left:
                    listAnswer.append(curr.left)
                if curr.right:
                    listAnswer.append(curr.right)
            level +=1
        return level