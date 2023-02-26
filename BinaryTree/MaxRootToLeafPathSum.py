# Max Root to Leaf Path Sum

class Node:
    def __init__(self, val, left=None, right=None):
        self.val =  val
        self.left = left
        self.right = right

### SOLUTION ###
# Complexity: n = number of nodes
# Time: 0(n)
# Space: 0(n)

# Recursive
def maxPathSumRecursive(root):
    if not root: return float('-inf')
    if not root.left and not root.right: return root.val
    maxChildPathSum = max(maxPathSumRecursive(root.left), maxPathSumRecursive(root.right))
    return root.val + maxChildPathSum

################

if __name__ == '__main__':

    ''' Construct the following tree
              1
            /   \
           /     \
          2       3
           \     / \
            4   5   6
               / \
              7   8
    '''
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

node = root.right.left.left
print(maxPathSumRecursive(root)) # Expected output: 17
