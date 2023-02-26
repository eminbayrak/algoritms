# Given a binary tree, check if the target node exists in the tree
class Node:
    def __init__(self, val, left=None, right=None):
        self.val =  val
        self.left = left
        self.right = right

### SOLUTION ###
# Using BFS
# Complexity: n = number of nodes
# Time: 0(n)
# Space: 0(n)
def treeIncludesBFS(root, target) -> bool:
    if root == None: return False
    queue = [root]
    
    while len(queue) > 0:
       current = queue.pop(0)
       if current.val == target: return True
       if current.left != None:  queue.append(current.left)
       if current.right != None:  queue.append(current.right)
    return False

# Using DFS - Recursive
# Complexity: n = number of nodes
# Time: 0(n)
# Space: 0(n)
def treeIncludesDFS(root, target) -> bool:
    if root == None: return False
    if root.val == target: return True
    return treeIncludesDFS(root.left, target) or treeIncludesDFS(root.right, target)

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
print(treeIncludesBFS(root, 10)) # Expected Result: False
print(treeIncludesDFS(root, 8)) # Expected Result: True
