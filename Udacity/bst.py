class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root
        while True:
            if current.value < new_val:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(new_val)
                    break
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(new_val)
                    break

    def search(self, find_val):
        current = self.root
        while current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                current = current.right
            else:
                current = current.left
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
