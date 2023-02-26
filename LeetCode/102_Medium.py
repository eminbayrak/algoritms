# Given a binary tree, check if the target node exists in the tree
class Node:
    def __init__(self, val, left=None, right=None):
        self.val =  val
        self.left = left
        self.right = right


# 102. Binary Tree Level Order Traversal
# Medium

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:

# Input: root = [1]
# Output: [[1]]

# Example 3:

# Input: root = []
# Output: []
def levelOrder(root):
        if root:
            queue = [root]
            result = []
            while len(queue) > 0:
                level = []
                for i in range(len(queue)):
                    current = queue.pop(0)
                    level.append(current.val)
                    if current.left: queue.append(current.left)
                    if current.right: queue.append(current.right)
                result.append(level)
            
        return result



if __name__ == '__main__':

    ''' Construct the following tree
              3
            /   \
           9     20
                 / \
                15  7
    '''

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.left.right = Node(7)

print(levelOrder(root)) # Expected output: [[3],[9,20],[15,7]]