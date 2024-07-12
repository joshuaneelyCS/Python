# Print the inorder traversal given a root node of a BST

def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def isLeaf(root):
            if root.left == None and root.right == None:
                return True
            return False

        def inOrderTraversalRec(root):
            if root == None:
                return []

            if isLeaf(root):
                return [root.val]

            return inOrderTraversalRec(root.left) + [root.val] + inOrderTraversalRec(root.right)
        
        return inOrderTraversalRec(root)
