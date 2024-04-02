from collections import deque
class TreeNode:
  def __init__(self,data):
    self.key = data
    self.left = None
    self.right = None

def inorder_traversal(root):
  if root:
    inorder_traversal(root.left)
    print(root.key,end=' ')
    inorder_traversal(root.right)
def insert(root, key):
  if not root:
    return TreeNode(key)
  queue = deque([root])
  while queue:
    node = queue.pop()  
    if not node.left:
      node.left = TreeNode(key)
      break
    else:
      queue.append(node.left)
    if not node.right:
      node.right = TreeNode(key)
      break
    else:
      queue.append(node.right)


if __name__=='__main__':
  root = TreeNode(50)
  root.left = TreeNode(30)
  root.right = TreeNode(70)
  root.left.left = TreeNode(20)
  root.left.right = TreeNode(40)
  root.right.right = TreeNode(80)

  print("Inorder traversal before insertion:", end=" ")
  inorder_traversal(root)
  insert(root, 60)
  print("\nInorder traversal after insertion:", end=" ")
  inorder_traversal(root)
