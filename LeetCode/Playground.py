# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def invertTree(root):
#     if root == None:
#         return None
#     temp = root.left
#     root.left = root.right
#     root.right = temp
    
#     invertTree(root.left)
#     invertTree(root.right)
#     return root.val

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d


def printLinkedList(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next
printLinkedList(a)