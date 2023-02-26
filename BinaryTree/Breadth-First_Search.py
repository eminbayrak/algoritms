class Node:
    def __init__(self, val, left=None, right=None):
        self.val =  val
        self.left = left
        self.right = right
        
# Simple BFS algorithm, since it based on queue structure,
# recursion cannot be done on BFS
def breadthFistValues(root):
  if root == None: return []
  queue = [ root ]
  values = []
  while len(queue) > 0:
    current = queue.pop(0)
    values.append(current.val)
    if current.left != None: queue.append(current.left)
    if current.right != None: queue.append(current.right)
  return values

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
print(breadthFistValues(root)) # Expected output: [1, 2, 3, 4, 5, 6, 7, 8]
