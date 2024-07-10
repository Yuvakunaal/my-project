class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert(root,key):
    if root is None:
        return TreeNode(key)
    if key > root.val:
        root.right = insert(root.right,key)
    else:
        root.left = insert(root.left,key)
    return root

def search(root, key):
    if root is None:
        return None 
    if root.val == key:
        return True
    elif key > root.val:
        return search(root.right, key)
    else: 
        return search(root.left, key)

def min_node(node):
    current = node
    while current.left is not None: 
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = min_node(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root

def display(root,arr):
    if root is not None:
        display(root.left,arr)
        arr.append(root.val)
        display(root.right,arr)

root = None

#insert
a = [10,20,5,2,6,30]
for i in a:
    root = insert(root,i)

# display
arr = []
display(root,arr)
print(arr)
        
# search
key = 6
a = search(root,key)
if a is None:
    print(f"{key} is not found in BST")
else:
    print(f"{key} is Found")

# delete
delete(root,2)
delete(root,20)

# display
arr = []
display(root,arr)
print(arr)

