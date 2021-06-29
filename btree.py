
class tree():
    def __init__(self):
        self.root=None

    def insert(self,data):
        end=False
        node=user(data[0],data[1],data[2],data[3])
        if self.root==None:
            self.root=node
            end=True
        present=self.root
        while end==False:
            if node.id>present.value and present.right_child==None:
                present.right_child=node
                end=True
            elif node.id>present.value and present.right_child!=None:
                present=present.right_child
            elif node.id<present.value and present.left_child==None:
                present.left_child=node
                end=True
            elif node.id<present.value and present.left_child!=None:
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
        node1.hobby=node2.hobby
        node1.gender=node2.gender
        node1.age=node2.age
    def delete(self,index):
        end=False
        present=self.root
        parent=None
        while end==False: #search
            if index>present.id and present.right_child==None:
                break
            elif index>present.id and present.right_child!=None:
                parent=present
                present=present.right_child
            elif index<present.id and present.left_child==None:
                break
            elif index<present.id and present.left_child!=None:
                parent=present
                present=present.left_child
            elif index==present.id:
                end=True
        if end==True: #do delete
            if present.left_child!=None and present.right_child!= None: #for delete node has two children
                right_min=present.right_child
                while right_min.left_child:
                    right_min=right_min.left_child
                if present==self.root:
                    self.change(self.root,right_min)
                    self.delete(right_min.id)
                else:
                    self.change(parent,right_min)
                    self.delete(right_min.id)
            elif present.left_child==None and present.right_child==None: #for delete node has no child
                if parent.right_child==present:
                    parent.right_child=None
                else:
                    parent.left_child=None
            else: #for delete node has one child
                if present==self.root:
                    if present.left_child!=None:
                        self.root=present.left_child
                    else:
                        self.root=present.right_child
                elif present.left_child!=None:
                    if parent.left_child==present:
                        parent.left_child=present.left_child
                    else:
                        parent.right_child=present.left_child
                elif present.right_child!=None:
                    if parent.left_child==present:
                        parent.left_child=present.right_child
                    else:
                        parent.right_child=present.right_child