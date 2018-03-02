# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Guide:
    def __init__(self, opr, node):
        self.opr = opr # 0, print; 1, visit
        self.node = node

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        path = []
        path.append(Guide(1, root))
        while len(path)!= 0:
            current = path.pop()
            if current.node is None: # defence..
                continue
            if current.opr == 0:
                result.append(current.node.val)
            else:
                path.append(Guide(1, current.node.right))
                path.append(Guide(1, current.node.left))
                path.append(Guide(0, current.node))
        return result
