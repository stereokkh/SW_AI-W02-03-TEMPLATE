
class Node:
    data : int
    next : None
    prv : None
    key : int
    def __init__(self, key = None, data = None, next = None, prv = None):
        self.data = data
        self.next = next
        self.prv = prv
        self.key = key

        pass

class double_linked_list:
    
    def __init__(self):
        self.head = self.current = None
        self.no = 0
        pass
    def h_append(self, key, data):
        new_node = Node(key, data)
        if self.head == None:
            self.head = new_node
            new_node.prv = new_node
            new_node.next = new_node
            self.no += 1
            return new_node
        else :
            tail = self.head.prv
            self.head.prv = new_node
            new_node.next = self.head
            tail.next = new_node
            new_node.prv = tail
            self.head = new_node
            self.no += 1
            return new_node

    def t_delete(self):
        if self.no == 1:
            key = self.head.key
            self.head = None
            self.no -= 1
            return key
        tail = self.head.prv
        tail.prv.next = self.head
        self.head.prv = tail.prv
        self.no -= 1
        return tail.key

    def move_to_head(self, data : Node):
        if self.head == data:
                return
        temp = data.next
        data.next.prv = data.prv
        data.prv.next = temp
        data.next = self.head
        data.prv = self.head.prv
        data.prv.next = data
        self.head.prv = data
        self.head = data
        return

class LRUCache:

    def __init__(self, capacity: int):
        self.dl = double_linked_list()
        self.dic = {}
        self.capacity = capacity   

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dl.move_to_head(self.dic[key])
            return self.dic[key].data
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].data = value
            self.dl.move_to_head(self.dic[key])
            return

        if self.capacity == self.dl.no:
            key_l = self.dl.t_delete()
            self.dic.pop(key_l)
        node = self.dl.h_append(key ,value)
        self.dic[key] = node
    
        return None


