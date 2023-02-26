# Calculate the sum of binary tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val =  val
        self.left = left
        self.right = right

### SOLUTION ###
# Complexity: n = number of nodes
# Time: 0(n)
# Space: 0(n)

# Using BFS
def treeSum(root):
    if not root: return 0
    queue = [root]
    totalSum = 0
    while len(queue) > 0:
        current = queue.pop(0)
        totalSum += current.val
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return totalSum

# Recursive (DFS)
def treeSumRecursive(root):
    if not root: return 0
    return root.val + treeSumRecursive(root.left) + treeSumRecursive(root.right)

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
print('BFS - ', treeSum(root)) # Expected Result: 36
print('DFS (Recursive) - ', treeSumRecursive(root)) # Expected Result: 36
