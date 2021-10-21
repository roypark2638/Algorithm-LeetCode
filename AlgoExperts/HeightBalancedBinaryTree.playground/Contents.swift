/*
 You're given the root node of a Binary Tree. Write a function that returns true if this Binary Tree is height balanced and false if it isn't.
 
 A Binary Tree is height balanced if for each node in the tree, the difference between the height of its left subtree and the height of its right subtree is at most 1.
 
 Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null
 
 input:
 tree = 1
       / \
      2   3
     / \   \
    4   5   6
       / \
      7   8
 
 output: true
 */

class BinaryTree {
    var value: Int
    var left: BinaryTree?
    var right: BinaryTree?
    
    init(value: Int) {
        self.value = value
        self.left = nil
        self.right = nil
    }
}

struct TreeInfo {
    var isBalanced: Bool
    var height: Int
}

func heightBalancedBinaryTree(_ tree: BinaryTree) -> Bool {
    let treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced
}

func getTreeInfo(_ node: BinaryTree?) -> TreeInfo {
    if node == nil {
        return TreeInfo(isBalanced: true, height: -1)
    }
    
    let leftSubtreeInfo = getTreeInfo(node!.left)
    let rightSubtreeInfo = getTreeInfo(node!.right)
    
    // Check if current node is balanced
    
    let isBalanced = leftSubtreeInfo.isBalanced && rightSubtreeInfo.isBalanced && abs(leftSubtreeInfo.height - rightSubtreeInfo.height) <= 1
    
    let height = max(leftSubtreeInfo.height, rightSubtreeInfo.height)
    
    return TreeInfo(isBalanced: isBalanced, height: height)
}
