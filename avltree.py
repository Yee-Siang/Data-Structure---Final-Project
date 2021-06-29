class AVLTree(object):
    # Function to insert a node
    def __init__(self):
        self.root=None
    def insert_node(self, root, user): #key is user

        # Find the correct location and insert the node
        if self.root==None:
            self.root=user
            return
        if not root:
            return user
        elif user.id < root.id:
            root.left_child = self.insert_node(root.left_child, user.id)
        else:
            root.right_child = self.insert_node(root.right_child, user.id)

        root.height = 1 + max(self.getHeight(root.left_child),
                              self.getHeight(root.right_child))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if user.id < root.left_child.id:
                return self.rightRotate(root)
            else:
                root.left_child = self.leftRotate(root.left_child)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if user.id > root.right_child.id:
                return self.leftRotate(root)
            else:
                root.right_child = self.rightRotate(root.right_child)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, user):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif user.id < root.id:
            root.left_child = self.delete_node(root.left_child, user.id)
        elif user.id > root.id:
            root.right_child = self.delete_node(root.right_child, user.id)
        else:
            if root.left_child is None:
                temp = root.right_child
                root = None
                return temp
            elif root.right_child is None:
                temp = root.left_child
                root = None
                return temp
            temp = self.getMinValueNode(root.right_child)
            root.id = temp.id
            root.right_child = self.delete_node(root.right_child,
                                          temp.id)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left_child),
                              self.getHeight(root.right_child))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left_child) >= 0:
                return self.rightRotate(root)
            else:
                root.left_child = self.leftRotate(root.left_child)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right_child) <= 0:
                return self.leftRotate(root)
            else:
                root.right_child = self.rightRotate(root.right_child)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right_child
        T2 = y.left_child
        y.left_child = z
        z.right_child = T2
        z.height = 1 + max(self.getHeight(z.left_child),
                           self.getHeight(z.right_child))
        y.height = 1 + max(self.getHeight(y.left_child),
                           self.getHeight(y.right_child))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right_child
        y.right_child = z
        z.left_child = T3
        z.height = 1 + max(self.getHeight(z.left_child),
                           self.getHeight(z.right_child))
        y.height = 1 + max(self.getHeight(y.left_child),
                           self.getHeight(y.right_child))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left_child) - self.getHeight(root.right_child)

    def getMinValueNode(self, root):
        if root is None or root.left_child is None:
            return root
        return self.getMinValueNode(root.left_child)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.id), end="")
        self.preOrder(root.left_child)
        self.preOrder(root.right_child)

   