
class tree():
    def __init__(self):
        self.root=None

    def insert(self,node):
        end=False
        if self.root==None:
            self.root=node
            end=True
        present=self.root
        while end==False:
            if node.id>present.id and present.right_child==None:
                present.right_child=node
                end=True
            elif node.id>present.id and present.right_child!=None:
                present=present.right_child
            elif node.id<present.id and present.left_child==None:
                present.left_child=node
                end=True
            elif node.id<present.id and present.left_child!=None:
                present=present.left_child
    def search(self,index):
        current=self.root
        while current.id!=index:
            if index>current.id:
                current=current.right_child
            else:
                current=current.left_child
        return current
    def change(self,node1,node2):
        node1.id=node2.id
        node1.name=node2.name
        node1.interest=node2.interest
        node1.gender=node2.gender
        node1.age=node2.age
    def delete(self, root, user):
    
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
            root.right_child = self.delete(root.right_child,
                                          temp.id)
        if root is None:
            return root
    def getMinValueNode(self, root):
        if root is None or root.left_child is None:
            return root
        return self.getMinValueNode(root.left_child)