class Node:
    def __init__(self, val, left=None, right=None):
        self.val =  val
        self.left = left
        self.right = right

###################################################### 

# Brute Force
def depthFirstSearch(root):
    if root == None: return []
    stack = [ root ]
    result = []
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)
        
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
    return result

###################################################### 

# Recursive
def depthFirstSearchRecursive(root):
    if root == None: return []
    leftValues = depthFirstSearchRecursive(root.left)
    rightValues = depthFirstSearchRecursive(root.right)
    return [root.val, *leftValues, *rightValues]
        
###################################################### 

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
print(depthFirstSearch(root))
print(depthFirstSearchRecursive(root))