class Node:
    def __init__(self, key = None, color = "red"):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.color = color

class RB_Tree:
    
    T_null = Node(color="black")

    def __init__(self):
        self.root = self.T_null
        
        

        pass
    def delete(self):
        pass
    def insert(self, key):
        current = self.root
        
        #노드 처음 삽입시 root 생성 
        if self.root == self.T_null:
            new_node = Node(key=key, color="black")
            self.root = new_node
            self.root.left = self.T_null
            self.root.right = self.T_null
            self.root.p = self.T_null
        else:
            new_node = Node(key= key, color="red")
            new_node.right = self.T_null
            new_node.left = self.T_null
            
            while 1:
                if current.key == key:
                    return 
                if current.key < key:
                    if current.right != self.T_null:
                        current = current.right
                    else:
                        current.right = new_node
                        
                        break
                elif current.key > key:
                    if current.left != self.T_null:
                        current = current.left
                    else:
                        current.left = new_node
                        break
            new_node.p = current
            #new node 기준
            check_balance(new_node)

    def check_balance(self, node : Node):
        while node.p.color == "red":
            if node.p == node.p.p.left:
                u = node.p.p.right
                if u.color == "red":
                    node.p.color = "black"
                    u.color = "black"
                    node.p.p.color = "red"
                    node = node.p.p
                else:
                    if node == node.p.right:
                        node = node.p
                        self.left_rotate(node)
                    node.p.color = "black"                    
                    node.p.p.color = "red"
                    self.right_rotate(node.p.p)
                    
            else:
                u = node.p.p.left
                if u.color == "red":
                    node.p.color = "black"
                    u.color = "black"
                    node.p.p.color = "red"
                    node = node.p.p
                else:
                    if node == node.p.left:
                        node = node.p
                        self.right_rotate(node)
                    node.p.color = "black"                    
                    node.p.p.color = "red"
                    self.left_rotate(node.p.p)
        self.root.color == "black"

                    


            
#####################회전부터 구현하시면 됩니다이~
        pass
    def right_rotate(self):
        pass
    def left_rotate(self):
        pass